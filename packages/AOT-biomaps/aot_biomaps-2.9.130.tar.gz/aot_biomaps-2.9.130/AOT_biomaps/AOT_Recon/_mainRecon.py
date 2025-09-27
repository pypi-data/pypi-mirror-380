from AOT_biomaps.Config import config
from AOT_biomaps.AOT_Experiment.Tomography import Tomography
from .ReconEnums import ReconType
from .ReconTools import mse, ssim

import os
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class Recon(ABC):
    def __init__(self, experiment, saveDir = None, isGPU = config.get_process() == 'gpu',  isMultiGPU =  True if config.numGPUs > 1 else False, isMultiCPU = True):
        self.reconPhantom = None
        self.reconLaser = None
        self.experiment = experiment
        self.reconType = None
        self.saveDir = saveDir
        self.MSE = None
        self.SSIM = None

        self.isGPU = isGPU
        self.isMultiGPU = isMultiGPU
        self.isMultiCPU = isMultiCPU

        if str(type(self.experiment)) != str(Tomography):
            raise TypeError(f"Experiment must be of type {Tomography}")

    @abstractmethod
    def run(self,withTumor = True):
        pass

    def calculateCRC(self,iteration,ROI_mask = None):
        """
        Computes the Contrast Recovery Coefficient (CRC) for a given ROI.
        """
        if self.reconType is ReconType.Analytic:
            raise TypeError(f"Impossible to calculate CRC with analytical reconstruction")
        elif self.reconType is None:
            raise ValueError("Run reconstruction first")
        
        if self.reconLaser is None or self.reconLaser == []:
            raise ValueError("Reconstructed laser is empty. Run reconstruction first.")
        if isinstance(self.Laser,list) and len(self.Laser) == 1:
            raise ValueError("Reconstructed Image without tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        if self.reconPhantom is None or self.reconPhantom == []:
            raise ValueError("Reconstructed phantom is empty. Run reconstruction first.")
        if isinstance(self.reconPhantom, list) and len(self.reconPhantom) == 1:
            raise ValueError("Reconstructed Image with tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        
        if self.reconLaser is None or self.reconLaser == []:
            print("Reconstructed laser is empty. Running reconstruction without tumor...")
            self.run(withTumor = False, isSavingEachIteration=True)
        if ROI_mask is not None:
            recon_ratio = np.mean(self.reconPhantom[iteration][ROI_mask]) / np.mean(self.reconLaser[iteration][ROI_mask])
            lambda_ratio = np.mean(self.experiment.OpticImage.phantom[ROI_mask]) / np.mean(self.experiment.OpticImage.laser[ROI_mask]) 
        else:
            recon_ratio = np.mean(self.reconPhantom[iteration]) / np.mean(self.reconLaser[iteration])
            lambda_ratio = np.mean(self.experiment.OpticImage.phantom) / np.mean(self.experiment.OpticImage.laser)
        
        # Compute CRC
        CRC = (recon_ratio - 1) / (lambda_ratio - 1)
        return CRC
    
    def calculateMSE(self):
        """
        Calculate the Mean Squared Error (MSE) of the reconstruction.

        Returns:
            mse: float or list of floats, Mean Squared Error of the reconstruction
        """
                
        if self.reconPhantom is None or self.reconPhantom == []:
            raise ValueError("Reconstructed phantom is empty. Run reconstruction first.")

        if self.reconType in (ReconType.Analytic, ReconType.DeepLearning):
            self.MSE = mse(self.experiment.OpticImage.phantom, self.reconPhantom)

        elif self.reconType in (ReconType.Algebraic, ReconType.Bayesian):
            self.MSE = []
            for theta in self.reconPhantom:
                self.MSE.append(mse(self.experiment.OpticImage.phantom, theta))
  
    def calculateSSIM(self):
        """
        Calculate the Structural Similarity Index (SSIM) of the reconstruction.

        Returns:
            ssim: float or list of floats, Structural Similarity Index of the reconstruction
        """

        if self.reconPhantom is None or self.reconPhantom == []:
            raise ValueError("Reconstructed phantom is empty. Run reconstruction first.")
    
        if self.reconType in (ReconType.Analytic, ReconType.DeepLearning):
            data_range = self.reconPhantom.max() - self.reconPhantom.min()
            self.SSIM = ssim(self.experiment.OpticImage.phantom, self.reconPhantom, data_range=data_range)

        elif self.reconType in (ReconType.Algebraic, ReconType.Bayesian):
            self.SSIM = []
            for theta in self.reconPhantom:
                data_range = theta.max() - theta.min()
                ssim_value = ssim(self.experiment.OpticImage.phantom, theta, data_range=data_range)
                self.SSIM.append(ssim_value)
 
    def show(self, withTumor=True, savePath=None):
        """Display the original and reconstructed images side by side.

        Args:
            withTumor (bool): If True, show phantom with tumor. Otherwise, show laser without tumor.
            savePath (str, optional): Directory to save the figure. If None, figure is not saved.
        """
        fig, axs = plt.subplots(1, 2, figsize=(20, 10))

        # --- Data selection ---
        if withTumor:
            if self.reconPhantom is None or self.reconPhantom == []:
                raise ValueError("Reconstructed phantom with tumor is empty. Run reconstruction first.")
            original_image = self.experiment.OpticImage.phantom
            recon_image = self.reconPhantom[-1] if isinstance(self.reconPhantom, list) else self.reconPhantom
            original_title = "Phantom with tumor"
            recon_title = "Reconstructed phantom with tumor"
            vmax = 1  # Normalized intensity for phantom
        else:
            if self.reconLaser is None or self.reconLaser == []:
                raise ValueError("Reconstructed laser without tumor is empty. Run reconstruction first.")
            original_image = self.experiment.OpticImage.laser.intensity
            recon_image = self.reconLaser[-1] if isinstance(self.reconLaser, list) else self.reconLaser
            original_title = "Laser without tumor"
            recon_title = "Reconstructed laser without tumor"
            vmax = np.max(self.experiment.OpticImage.laser.intensity)  # Use max intensity for laser

        # --- Common extent and axis parameters ---
        extent = (
            self.experiment.params.general['Xrange'][0],
            self.experiment.params.general['Xrange'][1],
            self.experiment.params.general['Zrange'][1],
            self.experiment.params.general['Zrange'][0]
        )
        axis_params = {
            'xlabel': "x (mm)",
            'ylabel': "z (mm)",
            'fontsize': 12,
            'tick_params': {'axis': 'both', 'which': 'major', 'labelsize': 8}
        }

        # --- Plot original image ---
        im0 = axs[0].imshow(
            original_image,
            cmap='hot',
            vmin=0,
            vmax=vmax,
            extent=extent,
            aspect='equal'
        )
        axs[0].set_title(original_title)
        axs[0].set_xlabel(**{'label': axis_params['xlabel'], 'fontsize': axis_params['fontsize']})
        axs[0].set_ylabel(**{'label': axis_params['ylabel'], 'fontsize': axis_params['fontsize']})
        axs[0].tick_params(**axis_params['tick_params'])

        # --- Plot reconstructed image ---
        im1 = axs[1].imshow(
            recon_image,
            cmap='hot',
            vmin=0,
            vmax=vmax,
            extent=extent,
            aspect='equal'
        )
        axs[1].set_title(recon_title)
        axs[1].set_xlabel(**{'label': axis_params['xlabel'], 'fontsize': axis_params['fontsize']})
        axs[1].set_ylabel(**{'label': axis_params['ylabel'], 'fontsize': axis_params['fontsize']})
        axs[1].tick_params(**axis_params['tick_params'])
        axs[1].tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

        # --- Colorbar ---
        fig.subplots_adjust(bottom=0.2)
        cbar_ax = fig.add_axes([0.25, 0.08, 0.5, 0.03])
        cbar = fig.colorbar(im1, cax=cbar_ax, orientation='horizontal')
        cbar.set_label('Normalized Intensity', fontsize=12)
        cbar.ax.tick_params(labelsize=8)

        # --- Layout and save ---
        plt.subplots_adjust(wspace=0.3)

        if savePath is not None:
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            filename = 'recon_with_tumor.png' if withTumor else 'recon_without_tumor.png'
            plt.savefig(os.path.join(savePath, filename), dpi=300, bbox_inches='tight')

        plt.show()



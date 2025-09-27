from ._mainRecon import Recon
from .ReconEnums import ReconType, OptimizerType, ProcessType
from .AOT_Optimizers import MLEM, LS
from .ReconTools import check_gpu_memory, calculate_memory_requirement, mse
from AOT_biomaps.Config import config


import os
import sys
import subprocess
import warnings
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from datetime import datetime
from tempfile import gettempdir



class AlgebraicRecon(Recon):
    """
    This class implements the Algebraic reconstruction process.
    It currently does not perform any operations but serves as a template for future implementations.
    """
    def __init__(self, opti = OptimizerType.MLEM, numIterations = 10000, numSubsets = 1, isSavingEachIteration=True, lambda_reg=None, L_Factor=None, **kwargs):
        super().__init__(**kwargs)
        self.reconType = ReconType.Algebraic
        self.optimizer = opti
        self.reconPhantom = []
        self.reconLaser = []
        self.numIterations = numIterations
        self.numSubsets = numSubsets
        self.isSavingEachIteration = isSavingEachIteration
        self.lambda_reg = lambda_reg
        self.L_Factor = L_Factor

        if self.numIterations <= 0:
            raise ValueError("Number of iterations must be greater than 0.")
        if self.numSubsets <= 0:
            raise ValueError("Number of subsets must be greater than 0.")
        if type(self.numIterations) is not int:
            raise TypeError("Number of iterations must be an integer.")
        if type(self.numSubsets) is not int:
            raise TypeError("Number of subsets must be an integer.")
        
        print("Generating system matrix (processing acoustic fields)...")
        self.SMatrix = np.stack([ac_field.field for ac_field in self.experiment.AcousticFields], axis=-1)

    # PUBLIC METHODS

    def run(self, processType = ProcessType.PYTHON, withTumor= True):
        """
        This method is a placeholder for the Algebraic reconstruction process.
        It currently does not perform any operations but serves as a template for future implementations.
        """
            
        if(processType == ProcessType.CASToR):
            self._AlgebraicReconCASToR(withTumor)
        elif(processType == ProcessType.PYTHON):
            self._AlgebraicReconPython(withTumor)
        else:
            raise ValueError(f"Unknown Algebraic reconstruction type: {processType}")

    def load_reconCASToR(self,withTumor = True):
        if withTumor:
            folder = 'results_withTumor'
        else:
            folder = 'results_withoutTumor'
            
        for thetaFiles in os.path.join(self.saveDir, folder + '_{}'):
            if thetaFiles.endswith('.hdr'):
                theta = Recon.load_recon(thetaFiles)
                if withTumor:
                    self.reconPhantom.append(theta)
                else:
                    self.reconLaser.append(theta)

    def plot_MSE(self, isSaving=True, log_scale_x=False, log_scale_y=False):
        """
        Plot the Mean Squared Error (MSE) of the reconstruction.

        Parameters:
            isSaving: bool, whether to save the plot.
            log_scale_x: bool, if True, use logarithmic scale for the x-axis.
            log_scale_y: bool, if True, use logarithmic scale for the y-axis.
        Returns:
            None
        """
        if not self.MSE:
            raise ValueError("MSE is empty. Please calculate MSE first.")

        best_idx = self.indices[np.argmin(self.MSE)]

        print(f"Lowest MSE = {np.min(self.MSE):.4f} at iteration {best_idx+1}")
        # Plot MSE curve
        plt.figure(figsize=(7, 5))
        plt.plot(self.indices, self.MSE, 'r-', label="MSE curve")
        # Add blue dashed lines
        plt.axhline(np.min(self.MSE), color='blue', linestyle='--', label=f"Min MSE = {np.min(self.MSE):.4f}")
        plt.axvline(best_idx, color='blue', linestyle='--', label=f"Iteration = {best_idx+1}")
        plt.xlabel("Iteration")
        plt.ylabel("MSE")
        plt.title("MSE vs. Iteration")
        if log_scale_x:
            plt.xscale('log')
        if log_scale_y:
            plt.yscale('log')
        plt.legend()
        plt.grid(True, which="both", ls="-")
        plt.tight_layout()
        if isSaving and self.saveDir is not None:
            now = datetime.now()
            date_str = now.strftime("%Y_%d_%m_%y")
            scale_str = ""
            if log_scale_x and log_scale_y:
                scale_str = "_loglog"
            elif log_scale_x:
                scale_str = "_logx"
            elif log_scale_y:
                scale_str = "_logy"
            if self.optimizer == OptimizerType.MLEM:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_MSE_plot_MLEM{scale_str}{date_str}.png')
            elif self.optimizer == OptimizerType.LS:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_MSE_plot_LS{scale_str}{date_str}.png')
            elif self.optimizer == OptimizerType.LS_TV:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_MSE_plot_LS_TV_Lambda_{self.lambda_reg}_LFactor_{self.L_Factor}{scale_str}{date_str}.png')
            plt.savefig(SavingFolder, dpi=300)
            print(f"MSE plot saved to {SavingFolder}")

        plt.show()

    def show_MSE_bestRecon(self, isSaving=True):
        if not self.MSE:
            raise ValueError("MSE is empty. Please calculate MSE first.")


        best_idx = np.argmin(self.MSE)
        print(best_idx)
        best_recon = self.reconPhantom[best_idx]

        # Crée la figure et les axes
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        # Left: Best reconstructed image (normalized)
        im0 = axs[0].imshow(best_recon,
                            extent=(self.experiment.params.general['Xrange'][0]*1000, self.experiment.params.general['Xrange'][1]*1000,
                                    self.experiment.params.general['Zrange'][1]*1000, self.experiment.params.general['Zrange'][0]*1000),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[0].set_title(f"Min MSE Reconstruction\nIter {best_idx}, MSE={np.min(self.MSE):.4f}")
        axs[0].set_xlabel("x (mm)", fontsize=12)
        axs[0].set_ylabel("z (mm)", fontsize=12)
        axs[0].tick_params(axis='both', which='major', labelsize=8)

        # Middle: Ground truth (normalized)
        im1 = axs[1].imshow(self.experiment.OpticImage.phantom,
                            extent=(self.experiment.params.general['Xrange'][0]*1000, self.experiment.params.general['Xrange'][1]*1000,
                                    self.experiment.params.general['Zrange'][1]*1000, self.experiment.params.general['Zrange'][0]*1000),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[1].set_title(r"Ground Truth ($\lambda$)")
        axs[1].set_xlabel("x (mm)", fontsize=12)
        axs[1].set_ylabel("z (mm)", fontsize=12)
        axs[1].tick_params(axis='both', which='major', labelsize=8)
        axs[1].tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

        # Right: Reconstruction at last iteration
        lastRecon = self.reconPhantom[-1]
        print(lastRecon.shape)
        if self.experiment.OpticImage.phantom.shape != lastRecon.shape:
            lastRecon = lastRecon.T
        im2 = axs[2].imshow(lastRecon,
                            extent=(self.experiment.params.general['Xrange'][0]*1000, self.experiment.params.general['Xrange'][1]*1000,
                                    self.experiment.params.general['Zrange'][1]*1000, self.experiment.params.general['Zrange'][0]*1000),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[2].set_title(f"Last Reconstruction\nIter {self.numIterations * self.numSubsets}, MSE={np.mean((self.experiment.OpticImage.phantom - lastRecon) ** 2):.4f}")
        axs[2].set_xlabel("x (mm)", fontsize=12)
        axs[2].set_ylabel("z (mm)", fontsize=12)
        axs[2].tick_params(axis='both', which='major', labelsize=8)

        # Ajoute une colorbar horizontale centrée en dessous des trois plots
        fig.subplots_adjust(bottom=0.2)
        cbar_ax = fig.add_axes([0.25, 0.08, 0.5, 0.03])
        cbar = fig.colorbar(im2, cax=cbar_ax, orientation='horizontal')
        cbar.set_label('Normalized Intensity', fontsize=12)
        cbar.ax.tick_params(labelsize=8)

        plt.subplots_adjust(wspace=0.3)

        if isSaving and self.saveDir is not None:
            now = datetime.now()
            date_str = now.strftime("%Y_%d_%m_%y")
            savePath = os.path.join(self.saveDir, 'results')
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            if self.optimizer == OptimizerType.MLEM:
                namePath = f'{self.SMatrix.shape[3]}_SCANS_comparison_MSE_BestANDLastRecon_MLEM_Date_{date_str}.png'
            elif self.optimizer == OptimizerType.LS:
                namePath = f'{self.SMatrix.shape[3]}_SCANS_comparison_MSE_BestANDLastRecon_LS_Date_{date_str}.png'
            elif self.optimizer == OptimizerType.LS_TV:
                namePath = f'{self.SMatrix.shape[3]}_SCANS_comparison_MSE_BestANDLastRecon_LS_TV_Lambda_{self.lambda_reg}_LFactor_{self.L_Factor}_Date_{date_str}.png'
            SavingFolder = os.path.join(savePath, namePath)
            plt.savefig(SavingFolder, dpi=300, bbox_inches='tight')
            print(f"MSE plot saved to {SavingFolder}")

        plt.show()

    def show_theta_animation(self, vmin=None, vmax=None, duration=5000, save_path=None):
        """
        Show theta iteration animation (for Jupyter) and optionally save it as a GIF.
        
        Parameters:
            matrix_theta: list of (z, x) ndarray, Algebraic reconstructions
            x: 1D array, x-coordinates (in meters)
            z: 1D array, z-coordinates (in meters)
            vmin, vmax: color limits (optional)
            duration: duration of the animation in milliseconds
            save_path: path to save animation (e.g., 'theta.gif' or 'theta.mp4')
        """
        if len(self.reconPhantom) == 0 or len(self.reconPhantom) == 1:
            raise ValueError("No theta matrix available for animation.")

        frames = np.array(self.reconPhantom)
        num_frames = len(frames)

        interval = max(1, int(duration / num_frames))

        if vmin is None:
            vmin = np.min(frames)
        if vmax is None:
            vmax = np.max(frames)

        fig, ax = plt.subplots(figsize=(5, 5))
        im = ax.imshow(frames[0],
                    extent=(self.experiment.params.general['Xrange'][0],self.experiment.params.general['Xrange'][1], self.experiment.params.general['Zrange'][1], self.experiment.params.general['Zrange'][0]),
                    vmin=vmin, vmax=vmax,
                    aspect='equal', cmap='hot')

        title = ax.set_title("Iteration 0")
        ax.set_xlabel("x (mm)")
        ax.set_ylabel("z (mm)")
        plt.tight_layout()

        def update(frame_idx):
            im.set_array(frames[frame_idx])
            title.set_text(f"Iteration {self.indices[frame_idx]}")
            return [im, title]

        ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=interval, blit=False)

        if save_path:
            if save_path.endswith(".gif"):
                ani.save(save_path, writer="pillow", fps=1000 // interval)
            elif save_path.endswith(".mp4"):
                ani.save(save_path, writer="ffmpeg", fps=1000 // interval)
            else:
                raise ValueError("Unsupported file format. Use .gif or .mp4")
            print(f"Animation saved to {save_path}")

        plt.close(fig)
        plt.rcParams["animation.html"] = "jshtml"
        return HTML(ani.to_jshtml())  

    def plot_SSIM(self, isSaving=True, log_scale_x=False, log_scale_y=False):
        if not self.SSIM:
            raise ValueError("SSIM is empty. Please calculate SSIM first.")

        best_idx = self.indices[np.argmax(self.SSIM)]

        print(f"Highest SSIM = {np.max(self.SSIM):.4f} at iteration {best_idx+1}")
        # Plot SSIM curve
        plt.figure(figsize=(7, 5))
        plt.plot(self.indices, self.SSIM, 'r-', label="SSIM curve")
        # Add blue dashed lines
        plt.axhline(np.max(self.SSIM), color='blue', linestyle='--', label=f"Max SSIM = {np.max(self.SSIM):.4f}")
        plt.axvline(best_idx, color='blue', linestyle='--', label=f"Iteration = {best_idx}")
        plt.xlabel("Iteration")
        plt.ylabel("SSIM")
        plt.title("SSIM vs. Iteration")
        if log_scale_x:
            plt.xscale('log')
        if log_scale_y:
            plt.yscale('log')
        plt.legend()
        plt.grid(True, which="both", ls="-")
        plt.tight_layout()
        if isSaving and self.saveDir is not None:
            now = datetime.now()
            date_str = now.strftime("%Y_%d_%m_%y")
            scale_str = ""
            if log_scale_x and log_scale_y:
                scale_str = "_loglog"
            elif log_scale_x:
                scale_str = "_logx"
            elif log_scale_y:
                scale_str = "_logy"
            if self.optimizer == OptimizerType.MLEM:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_SSIM_plot_MLEM{scale_str}{date_str}.png')
            elif self.optimizer == OptimizerType.LS:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_SSIM_plot_LS{scale_str}{date_str}.png')
            elif self.optimizer == OptimizerType.LS_TV:
                SavingFolder = os.path.join(self.saveDir, f'{self.SMatrix.shape[3]}_SCANS_SSIM_plot_LS_TV_Lambda_{self.lambda_reg}_LFactor_{self.L_Factor}{scale_str}{date_str}.png')
            plt.savefig(SavingFolder, dpi=300)
            print(f"SSIM plot saved to {SavingFolder}")

        plt.show()

    def show_SSIM_bestRecon(self, isSaving=True):
        
        if not self.SSIM:
            raise ValueError("SSIM is empty. Please calculate SSIM first.")

        best_idx = self.indices[np.argmax(self.SSIM)]
        best_recon = self.reconPhantom[best_idx]

        # ----------------- Plotting -----------------
        _, axs = plt.subplots(1, 3, figsize=(15, 5))  # 1 row, 3 columns

        # Normalization based on LAMBDA max
        lambda_max = np.max(self.experiment.OpticImage.laser.intensity)

        # Left: Best reconstructed image (normalized)
        im0 = axs[0].imshow(best_recon, 
                            extent=(self.experiment.params.general['Xrange'][0], self.experiment.params.general['Xrange'][1], self.experiment.params.general['Zrange'][1], self.experiment.params.general['Zrange'][0]),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[0].set_title(f"Max SSIM Reconstruction\nIter {best_idx}, SSIM={np.min(self.MSE):.4f}")
        axs[0].set_xlabel("x (mm)")
        axs[0].set_ylabel("z (mm)")
        plt.colorbar(im0, ax=axs[0])

        # Middle: Ground truth (normalized)
        im1 = axs[1].imshow(self.experiment.OpticImage.laser.intensity, 
                            extent=(self.experiment.params.general['Xrange'][0], self.experiment.params.general['Xrange'][1], self.experiment.params.general['Zrange'][1], self.experiment.params.general['Zrange'][0]),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[1].set_title(r"Ground Truth ($\lambda$)")
        axs[1].set_xlabel("x (mm)")
        axs[1].set_ylabel("z (mm)")
        plt.colorbar(im1, ax=axs[1])

        # Right: Reconstruction at iter 350
        lastRecon = self.reconPhantom[-1] 
        im2 = axs[2].imshow(lastRecon,
                            extent=(self.experiment.params.general['Xrange'][0], self.experiment.params.general['Xrange'][1], self.experiment.params.general['Zrange'][1], self.experiment.params.general['Zrange'][0]),
                            cmap='hot', aspect='equal', vmin=0, vmax=1)
        axs[2].set_title(f"Last Reconstruction\nIter {self.numIterations * self.numSubsets}, SSIM={self.SSIM[-1]:.4f}")
        axs[2].set_xlabel("x (mm)")
        axs[2].set_ylabel("z (mm)")
        plt.colorbar(im2, ax=axs[2])

        plt.tight_layout()
        if isSaving:
            now = datetime.now()    
            date_str = now.strftime("%Y_%d_%m_%y")
            SavingFolder = os.path.join(self.saveDir, 'results', f'comparison_SSIM_BestANDLastRecon{date_str}.png')
            plt.savefig(SavingFolder, dpi=300)
            print(f"SSIM plot saved to {SavingFolder}")
        plt.show()

    def plot_CRC_vs_Noise(self, ROI_mask = None, start=0, fin=None, step=10, save_path=None):
        """
        Plot CRC (Contrast Recovery Coefficient) vs Noise for each iteration.
        """
        if self.reconLaser is None or self.reconLaser == []:
            raise ValueError("Reconstructed laser is empty. Run reconstruction first.")
        if isinstance(self.Laser,list) and len(self.Laser) == 1:
            raise ValueError("Reconstructed Image without tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        if self.reconPhantom is None or self.reconPhantom == []:
            raise ValueError("Reconstructed phantom is empty. Run reconstruction first.")
        if isinstance(self.reconPhantom, list) and len(self.reconPhantom) == 1:
            raise ValueError("Reconstructed Image with tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        
        if fin is None:
            fin = len(self.reconPhantom) - 1

        iter_range = self.indices

        crc_values = []
        noise_values = []

        for i in iter_range:
            recon_without_tumor = self.reconLaser[i].T

            # CRC
            crc = self.calculateCRC(iteration=i,ROI_mask=ROI_mask)
            crc_values.append(crc)

            # Noise
            noise = np.mean(np.abs(recon_without_tumor - self.experiment.OpticImage.laser.intensity))
            noise_values.append(noise)

        plt.figure(figsize=(6, 5))
        plt.plot(noise_values, crc_values, 'o-', label='ML-EM')
        for i, (x, y) in zip(iter_range, zip(noise_values, crc_values)):
            plt.text(x, y, str(i), fontsize=5.5, ha='left', va='bottom')

        plt.xlabel("Noise (mean absolute error)")
        plt.ylabel("CRC (Contrast Recovery Coefficient)")

        plt.xscale('log')
        plt.yscale('log')

        plt.title("CRC vs Noise over Iterations")
        plt.grid(True)
        plt.legend()

        if save_path:
            plt.savefig(save_path, dpi=300)
            print(f"Figure saved to: {save_path}")
        plt.show()
        
    def show_reconstruction_progress(self, start=0, fin=None, duration=5000, save_path=None):
        """
        Show the reconstruction progress for both with and without tumor.
        Parameters:
            start: int, starting iteration index
            fin: int, ending iteration index (inclusive)
            duration: int, duration of the animation in milliseconds
            save_path: str, path to save the figure (optional)
        """

        if self.reconLaser is None or self.reconLaser == []:
            raise ValueError("Reconstructed laser is empty. Run reconstruction first.")
        if isinstance(self.Laser,list) and len(self.Laser) == 1:
            raise ValueError("Reconstructed Image without tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        if self.reconPhantom is None or self.reconPhantom == []:
            raise ValueError("Reconstructed phantom is empty. Run reconstruction first.")
        if isinstance(self.reconPhantom, list) and len(self.reconPhantom) == 1:
            raise ValueError("Reconstructed Image with tumor is a single frame. Run reconstruction with isSavingEachIteration=True to get a sequence of frames.")
        
        step = 1 / self.experiment.params.general['f_saving']* duration / 1000  # convert duration to seconds and divide by frame rate

        if fin is None:
            fin = len(self.reconPhantom) - 1

        iter_list = self.indices
        nrows = len(iter_list)
        ncols = 3  # Recon, |Recon - GT|, Ground Truth

        vmin = 0
        vmax = 1

        recon_without_tumor_list = []
        diff_abs_without_tumor_list = []
        mse_without_tumor_list = []
        noise_list = []

        for i in iter_list:
            
            diff_abs_without_tumor = np.abs(recon_without_tumor - self.experiment.OpticImage.laser.intensity)
            mse_without_tumor = mse(self.experiment.OpticImage.laser.intensity.flatten(), recon_without_tumor.flatten())

            noise = np.mean(np.abs(self.reconLaser[i] - self.experiment.OpticImage.laser.intensity))

            recon_without_tumor_list.append(recon_without_tumor)
            diff_abs_without_tumor_list.append(diff_abs_without_tumor)
            mse_without_tumor_list.append(mse_without_tumor)
            noise_list.append(noise)

        global_min_diff_abs_without_tumor = np.min([d.min() for d in diff_abs_without_tumor_list[1:]])
        global_max_diff_abs_without_tumor = np.max([d.max() for d in diff_abs_without_tumor_list[1:]])

        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 3 * nrows))

        for i, iter_idx in enumerate(iter_list):
            recon_without_tumor = recon_without_tumor_list[i]
            diff_abs_without_tumor = diff_abs_without_tumor_list[i]
            mse_without_tumor = mse_without_tumor_list[i]
            noise = noise_list[i]

            im0 = axs[i, 0].imshow(recon_without_tumor, cmap='hot', vmin=vmin, vmax=vmax, aspect='equal')
            axs[i, 0].set_title(f"Reconstruction\nIter {iter_idx}, MSE={mse_without_tumor:.2e}", fontsize=10)
            axs[i, 0].axis('off')
            plt.colorbar(im0, ax=axs[i, 0])

            if i >= 0 :
                im1 = axs[i, 1].imshow(diff_abs_without_tumor, cmap='viridis', vmin=np.min(diff_abs_without_tumor), vmax=np.max(diff_abs_without_tumor), aspect='equal')
            else :
                im1 = axs[i, 1].imshow(diff_abs_without_tumor, cmap='viridis', vmin=global_min_diff_abs_without_tumor, vmax=global_max_diff_abs_without_tumor, aspect='equal')
            axs[i, 1].set_title(f"|Recon - Ground Truth|\nNoise={noise:.2e}", fontsize=10)
            axs[i, 1].axis('off')
            plt.colorbar(im1, ax=axs[i, 1])

            # 右图：ground truth
            im2 = axs[i, 2].imshow(self.experiment.OpticImage.laser.intensity, cmap='hot', vmin=vmin, vmax=vmax, aspect='equal')
            axs[i, 2].set_title(r"Ground Truth ($\lambda$)", fontsize=10)
            axs[i, 2].axis('off')
            plt.colorbar(im2, ax=axs[i, 2])

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
            print(f"Figure saved to: {save_path}")
        plt.show()

        # with tumor

        if fin is None:
            fin = len(self.reconPhantom) - 1

        iter_list = list(range(start, fin + 1, step))
        nrows = len(iter_list)
        ncols = 3  # Recon, |Recon - GT|, Ground Truth

        vmin = 0
        vmax = 1

        recon_with_tumor_list = []
        diff_abs_with_tumor_list = []
        mse_with_tumor_list = []
        noise_list = []

        for i in iter_list:
            recon_with_tumor = self.reconPhantom[i]
            diff_abs_with_tumor = np.abs(recon_with_tumor - self.experiment.OpticImage.phantom)
            mse_with_tumor = mse(self.experiment.OpticImage.phantom.flatten(), recon_with_tumor.flatten())

            noise = np.mean(np.abs(self.reconPhantom[i] - self.experiment.OpticImage.phantom))  # !! without tumor

            recon_with_tumor_list.append(recon_with_tumor)
            diff_abs_with_tumor_list.append(diff_abs_with_tumor)
            mse_with_tumor_list.append(mse_with_tumor)  
            noise_list.append(noise)


        global_min_diff_abs_with_tumor = np.min([d.min() for d in diff_abs_with_tumor_list[1:]])
        global_max_diff_abs_with_tumor = np.max([d.max() for d in diff_abs_with_tumor_list[1:]])

        _, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 3 * nrows))

        for i, iter_idx in enumerate(iter_list):
            recon_with_tumor = recon_with_tumor_list[i]
            diff_abs_with_tumor = diff_abs_with_tumor_list[i]
            mse_with_tumor = mse_with_tumor_list[i]
            noise = noise_list[i]

            im0 = axs[i, 0].imshow(recon_with_tumor, cmap='hot', vmin=vmin, vmax=vmax, aspect='equal')
            axs[i, 0].set_title(f"Reconstruction\nIter {iter_idx}, MSE={mse_with_tumor:.2e}", fontsize=10)
            axs[i, 0].axis('off')
            plt.colorbar(im0, ax=axs[i, 0])


            if i >= 0 :
                im1 = axs[i, 1].imshow(diff_abs_with_tumor, cmap='viridis', vmin=np.min(diff_abs_with_tumor), vmax=np.max(diff_abs_with_tumor), aspect='equal')
            else :
                im1 = axs[i, 1].imshow(diff_abs_with_tumor, cmap='viridis', vmin=global_min_diff_abs_with_tumor, vmax=global_max_diff_abs_with_tumor, aspect='equal')
            axs[i, 1].set_title(f"|Recon - Ground Truth|\nNoise={noise:.2e}", fontsize=10)
            axs[i, 1].axis('off')
            plt.colorbar(im1, ax=axs[i, 1])

            im2 = axs[i, 2].imshow(self.experiment.OpticImage.phantom, cmap='hot', vmin=vmin, vmax=vmax, aspect='equal')
            axs[i, 2].set_title(r"Ground Truth ($\lambda$)", fontsize=10)
            axs[i, 2].axis('off')
            plt.colorbar(im2, ax=axs[i, 2])

        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
            print(f"Figure saved to: {save_path}")
        plt.show()
   
    # PRIVATE METHODS

    def _AlgebraicReconPython(self,withTumor):
    
        if withTumor:
            if self.experiment.AOsignal_withTumor is None:
                raise ValueError("AO signal with tumor is not available. Please generate AO signal with tumor the experiment first in the experiment object.")
            if self.optimizer.value == OptimizerType.MLEM.value:
                self.reconPhantom, self.indices = self._MLEM(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withTumor, withTumor=withTumor)
            elif self.optimizer.value == OptimizerType.LS.value:
                self.reconPhantom, self.indices = self._LS(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withTumor, withTumor=withTumor)
            elif self.optimizer.value == OptimizerType.LS_TV.value:
                self.reconPhantom, self.indices = self._LS_Regularized(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withTumor, withTumor=withTumor)
            else:
                raise ValueError(f"Only MLEM and LS are supported for simple algebraic reconstruction. {self.optimizer.value} need Bayesian reconstruction")
        else:
            if self.experiment.AOsignal_withoutTumor is None:
                raise ValueError("AO signal without tumor is not available. Please generate AO signal without tumor the experiment first in the experiment object.")
            if self.optimizer.value == OptimizerType.MLEM.value:
                self.reconLaser, self.indices = self._MLEM(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withoutTumor, withTumor=withTumor)
            elif self.optimizer.value == OptimizerType.LS.value:
                self.reconLaser, self.indices = self._LS(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withoutTumor, withTumor=withTumor)
            elif self.optimizer.value == OptimizerType.LS_TV.value:
                self.reconLaser, self.indices = self._LS_Regularized(SMatrix=self.SMatrix, y=self.experiment.AOsignal_withoutTumor, withTumor=withTumor)
            else:
                raise ValueError(f"Only MLEM and LS are supported for simple algebraic reconstruction. {self.optimizer.value} need Bayesian reconstruction")

    def _AlgebraicReconCASToR(self, withTumor):
        
        # Define variables
        smatrix = os.path.join(self.saveDir,"system_matrix")

        if withTumor:
            fileName = 'AOSignals_withTumor.cdh'
        else:
            fileName = 'AOSignals_withoutTumor.cdh'

        # Check if input file exists
        if not os.path.isfile(f"{self.saveDir}/{fileName}"):
            self.experiment._saveAOsignals_Castor(self.saveDir)
        # Check if system matrix directory exists
        elif not os.path.isdir(smatrix):
            os.mkdir(smatrix)
        # check if system matrix is empty
        elif not os.listdir(smatrix):
            self.experiment.saveAcousticFields(self.saveDir)

        # Vérifier que le dossier de sortie existe
        os.makedirs(os.path.join(self.saveDir, 'results','recon'), exist_ok=True)

        # Vérifier que le fichier .cdh existe
        if not os.path.isfile(fileName):
            raise FileNotFoundError(f"Le fichier .cdh n'existe pas : {fileName}")

        # Créer une copie de l'environnement actuel et ajouter les variables CAStOR
        env = os.environ.copy()

        env.update({
            "CASTOR_DIR": f"{self.experiment.params.reconstruction['castor_executable']}",
            "CASTOR_CONFIG": f"{self.experiment.params.reconstruction['castor_executable']}/config",
            "CASTOR_64bits": "1",
            "CASTOR_OMP": "1",
            "CASTOR_SIMD": "1",
            "CASTOR_ROOT": "1",
        })

        # Construire la commande
        cmd = [
            f"{self.experiment.params.reconstruction['castor_executable']}/bin/castor-recon",
            "-df",  f"{self.saveDir}/{fileName}",
            "-opti", self.optimizer.value,
            "-it", f"{self.numIterations}:{self.numSubsets}",
            "-proj", "matrix",
            "-dout", os.path.join(self.saveDir, 'results','recon'),
            "-th", f"{ os.cpu_count()}",
            "-vb", "5",
            "-proj-comp", "1",
            "-ignore-scanner",
            "-data-type", "AOT",
            "-ignore-corr", "cali,fdur",
            "-system-matrix", smatrix,
        ]

        # Print the command
        print(" ".join(cmd))

        #save the command to a script file
        recon_script_path = os.path.join(gettempdir(), 'recon.sh')
        with open(recon_script_path, 'w') as f:
            f.write("#!/bin/bash\n")
            f.write(" ".join(cmd) + "\n")

        sys.exit(0)

        # --- Run Reconstruction Script ---
        print(f"Running reconstruction script: {recon_script_path}")
        subprocess.run(["chmod", "+x", recon_script_path], check=True)
        subprocess.run([recon_script_path], check=True)
        print("Reconstruction script executed.")

        self.load_reconCASToR(withTumor=withTumor)

    def _MLEM(self, SMatrix, y, withTumor):
        """
        This method implements the MLEM algorithm using either CPU or single-GPU PyTorch acceleration.
        Multi-GPU mode is disabled due to memory fragmentation issues or lack of availability.
        """
        result = None
        indices = None
        required_memory = calculate_memory_requirement(SMatrix, y)

        if self.isGPU:
            if check_gpu_memory(config.select_best_gpu(), required_memory):
                result, indices = MLEM._MLEM_GPU_basic(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)
            else:
                warnings.warn("Insufficient GPU memory for single GPU MLEM. Falling back to CPU.")

        if result is None and self.isMultiCPU:
            result, indices = MLEM._MLEM_CPU_multi(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)

        if result is None:
            result, indices = MLEM._MLEM_CPU_opti(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)
            if result is None:
                warnings.warn("Optimized MLEM failed. Falling back to basic CPU MLEM.")
                result, indices = MLEM._MLEM_CPU_basic(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)

        return result, indices
    
    def _LS(self, SMatrix, y, withTumor):
        """
        This method implements the LS algorithm using either CPU or single-GPU PyTorch acceleration.
        Multi-GPU mode is disabled due to memory fragmentation issues or lack of availability.
        """
        result = None
        indices = None
        required_memory = calculate_memory_requirement(SMatrix, y)

        if self.isGPU:
            if check_gpu_memory(config.select_best_gpu(), required_memory):
                result, indices = LS._LS_GPU_basic(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)
            else:
                warnings.warn("Insufficient GPU memory for single GPU LS. Falling back to CPU.")

        if result is None and self.isMultiCPU:
            result, indices = LS._LS_CPU_multi(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)

        if result is None:
            result, indices = LS._LS_CPU_opti(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)
            if result is None:
                warnings.warn("Optimized LS failed. Falling back to basic CPU LS.")
                result, indices = LS._LS_CPU_basic(SMatrix=SMatrix, y=y, numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor)

        return result, indices

    def _LS_Regularized(self,SMatrix, y, withTumor):
        result = None
        indices = None
        required_memory = calculate_memory_requirement(SMatrix, y)

        if check_gpu_memory(config.select_best_gpu(), required_memory):
            if self.lambda_reg is None or self.L_Factor is None:
                raise ValueError("For LS with TV regularization, both lambda_reg and L_Factor must be specified.")
            result, indices = LS._LS_TV_GPU(SMatrix= SMatrix, y=y,  numIterations=self.numIterations, isSavingEachIteration=self.isSavingEachIteration, withTumor=withTumor, lambda_tv=self.lambda_reg, L_Factor=self.L_Factor)
        else:
            warnings.warn("Insufficient GPU memory for single GPU LS with TV regularization. Falling back to CPU.")
            raise NotImplementedError("LS with TV regularization is not implemented for CPU.")
        return result, indices
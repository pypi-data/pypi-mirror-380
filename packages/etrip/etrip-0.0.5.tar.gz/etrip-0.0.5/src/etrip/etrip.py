import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import os
from scipy.signal import convolve2d, detrend
from scipy.optimize import minimize, curve_fit
import cv2
import glob

from tqdm.auto import tqdm

class eTRiP():

    # Estimate derivatives
    def _space_time_deriv(subset_f):
        N = len(subset_f)
        dims = subset_f[0]['im'].shape
        if N == 1:
            fx = np.zeros(dims)
            fy = np.zeros(dims)
            ft = np.zeros(dims)
            return None, None, None
        elif N == 2:
            pre = np.array([0.5, 0.5])
            deriv = np.array([-1, 1])
        elif N == 3:
            pre = np.array([0.223755, 0.552490, 0.223755])
            deriv = np.array([-0.453014, 0.0, 0.453014])
        elif N == 4:
            pre = np.array([0.092645, 0.407355, 0.407355, 0.092645])
            deriv = np.array([-0.236506, -0.267576, 0.267576, 0.236506])
        elif N == 5:
            pre = np.array([0.036420, 0.248972, 0.429217, 0.248972, 0.036420])
            deriv = np.array([-0.108415, -0.280353, 0.0, 0.280353, 0.108415])
        elif N == 6:
            pre = np.array([0.013846, 0.135816, 0.350337, 0.350337, 0.135816, 0.013846])
            deriv = np.array([-0.046266, -0.203121, -0.158152, 0.158152, 0.203121, 0.046266])
        elif N == 7:
            pre = np.array([0.005165, 0.068654, 0.244794, 0.362775, 0.244794, 0.068654, 0.005165])
            deriv = np.array([-0.018855, -0.123711, -0.195900, 0.0, 0.195900, 0.123711, 0.018855])
        else:
            raise Warning(f'No such filter size (N={N})')
             
        pre = [round(element,4) for element in pre]
        deriv = [round(element,4) for element in deriv]
        
        # SPACE/TIME DERIVATIVES
        fdt = np.zeros(dims)
        fpt = np.zeros(dims)
        for i in range(N):
            fpt = fpt + (pre[i] * subset_f[i]['im'])
            fdt = fdt + (deriv[i] * subset_f[i]['im'])
        
        # Reshape the filters to 2D arrays
        pre_2d = np.reshape(pre, (1, -1))
        deriv_2d = np.reshape(deriv, (-1, 1))
    
        # Perform the convolutions
        fx = convolve2d(fpt, pre_2d.T, mode='same')
        fx = convolve2d(fx, deriv_2d.T, mode='same')
        fy = convolve2d(fpt, pre_2d, mode='same')
        fy = convolve2d(fy, deriv_2d, mode='same')
        ft = convolve2d(fdt, pre_2d.T, mode='same')
        ft = convolve2d(ft, pre_2d, mode='same')
        
        return fx, fy, ft

    # Estimate motion
    def estimateMotion(inputDirectory,ext="jpg"):

        #absolute path
        inputDirectory = os.path.abspath(inputDirectory)
    
        GRADIENT_THRESHOLD = 8
        frames = []
        
        d = sorted([filename for filename in os.listdir(inputDirectory) if filename.lower().endswith(".%s"%ext)])
        N = len(d)
        c = 1
        f = []

        for k in range(1, N+1):
            im = cv2.imread(os.path.join(inputDirectory, d[k-1]))
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            if k == 1:
                scale = round(60 / max(im.shape), 4) # round to match Matlab output
            im = cv2.resize(im, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            f.append({})
            f[c-1]['orig'] = im
            f[c-1]['im'] = np.dot(im[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.float64)
            c += 1
        
        ydim, xdim = f[0]['im'].shape   # Double check if it isn't xdim, ydim instead.
        
        # compute motion
        taps = 7
        blur = [1, 6, 15, 20, 15, 6, 1]
        blur = np.array(blur) / np.sum(blur)
        blur = blur.reshape(1, -1)
        
        s = 1 # sub-sample spatially by this amount
        N = len(f) - (taps-1)
        Vx = np.zeros((ydim//s, xdim//s, N))
        Vy = np.zeros((ydim//s, xdim//s, N))
        
        for k in tqdm(range(N), leave=False, desc=os.path.basename(inputDirectory)):
            subset_f = f[k:k+taps]
            # print(f"Subset: {k} to {k+taps}")
            if len(subset_f) < 1:
                continue
            
            fx, fy, ft = eTRiP._space_time_deriv(subset_f)

            if any(var is not None for var in [fx,fx,ft]):
                fx2 = convolve2d(convolve2d(fx*fx, blur.T, mode='same'),
                                 blur, mode='same')
                fy2 = convolve2d(convolve2d(fy*fy, blur.T, mode='same'),
                                 blur, mode='same')
                fxy = convolve2d(convolve2d(fx*fy, blur.T, mode='same'),
                                 blur, mode='same')
                fxt = convolve2d(convolve2d(fx*ft, blur.T, mode='same'),
                                 blur, mode='same')
                fyt = convolve2d(convolve2d(fy*ft, blur.T, mode='same'),
                                 blur, mode='same')
    
                grad = np.sqrt(np.power(fx, 2) + np.power(fy, 2))
                # Set the specified regions to zero
                grad[:, :5] = 0
                grad[:5, :] = 0
                grad[:, -5:] = 0
                grad[-5:, :] = 0
    
                # Compute optical flow
                cx = 0
                bad = 0
                for x in range(0, xdim, s):
                    cy = 0
                    for y in range(0, ydim, s):
                        M = np.array([[fx2[y, x], fxy[y, x]], [fxy[y, x], fy2[y, x]]])
                        b = np.array([fxt[y, x], fyt[y, x]])
                        if np.linalg.cond(M) > 1e2 or grad[y, x] < GRADIENT_THRESHOLD:
                            Vx[cy, cx, k] = 0
                            Vy[cy, cx, k] = 0
                            bad += 1
                        else:
                            v = np.linalg.inv(M) @ b
                            Vx[cy, cx, k] = v[0]
                            Vy[cy, cx, k] = v[1]
                        cy += 1
                    cx += 1
    
                # check if bad / (xdim * ydim) == 1. If so, exit this function 
                if bad / (xdim * ydim) == 1:
                    return None, None
        
        # visualize motion field
        taps = 13
        blur = np.ones(taps)
        blur = blur / np.sum(blur)

        c = 0
        motion_x = []
        motion_y = []
    
        eps = 2.2204e-16
        for k in range(N - taps):
            vx = np.zeros(Vx.shape[:2])
            vy = np.zeros(Vy.shape[:2])
            Vx2 = Vx[:, :, k:k+taps]
            Vy2 = Vy[:, :, k:k+taps]
    
            for j in range(len(blur)):
                vx += blur[j] * Vx2[:, :, j]
                vy += blur[j] * Vy2[:, :, j]
    
            indx = np.where(np.abs(vx) > eps)
            indy = np.where(np.abs(vy) > eps)
    
            motion_x.append(1 / scale * np.mean(vx[indx]))
            motion_y.append(-1 / scale * np.mean(vy[indy]))
    
            c += 1
        
        return motion_x, motion_y

    # Estimate motion for all
    def estimateAll(inputDirectory, outputDirectory, ext="jpg"):
        #absolute path
        inputDirectory = os.path.abspath(inputDirectory)
        outputDirectory = os.path.abspath(outputDirectory)
        Path(outputDirectory).mkdir(parents=True, exist_ok=True)
    
        # Get a list of cropped image sub-directories
        d = sorted([f.path for f in os.scandir(inputDirectory) if f.is_dir()])
    
        for i in tqdm(range(len(d)), leave=False, desc="Estimate All"):
            subDirectory = d[i]
            plantID = os.path.basename(subDirectory)
            outputFilename = os.path.join(outputDirectory,"motion","%s.csv" % plantID)
            # Estimate motion
            if not os.path.isfile(outputFilename):
                motion_x,motion_y = eTRiP.estimateMotion(subDirectory, ext)
                # Check if motion was estimated
                if motion_x is None or motion_y is None:
                    print(f"ERROR: Could not estimate motion for {plantID}")
                    continue
                
                # Save vertical motion
                Path(os.path.dirname(outputFilename)).mkdir(parents=True, exist_ok=True)
                with open(outputFilename, "w") as f:
                    f.write("# PlantID: %s\n" % plantID)
                    df = pd.DataFrame({"motion x": motion_x, "motion y": motion_y})
                    df.to_csv(f, index=False, header=True, na_rep="inf")
    
    # Evaluate model
    def _evaluateModel(model, N):
        '''
        This function generates a sinusoid of length N 
        for a specified frequency, phase, and amplitude.
        '''
        freq=model[0]; phase=model[1]; amp=model[2]
        t = np.arange(N)
        f = amp * np.cos(freq * 2 * np.pi / len(t) * t + phase)
    
        return f
    
    
    # Error function
    def _errorFunc(model, dat):
        '''
        compute the RMS error between the current model and the data. 
        This is used by the non-linear optimization in modelFit.m
        '''
        N = len(dat)
        f = eTRiP._evaluateModel(model, N)
        err = np.sum((f - dat) ** 2)
        return err
    
    
    # Model fit
    def _modelFunc(t, freq, phase, amp):
        return eTRiP._evaluateModel([freq, phase, amp], N=len(t))
    
    
    # Jacobian
    def _jacFunc(t, freq, phase, amp):
        dfreq = -amp * np.sin(freq * 2 * np.pi / len(t) * t + phase) * 2 * np.pi / len(t) * t
        dphase = -amp * np.sin(freq * 2 * np.pi / len(t) * t + phase)
        damp = np.cos(freq * 2 * np.pi / len(t) * t + phase)
        return np.column_stack((dfreq, dphase, damp))
    
    # Fit model to motion data
    def modelFitAll(analysisDirectory):
        #absolute path
        motionDirectory = os.path.abspath(os.path.join(analysisDirectory,"motion"))
        modelDirectory = os.path.abspath(os.path.join(analysisDirectory,"model"))
    
        d = sorted([filename for filename in os.listdir(motionDirectory) if filename.lower().endswith(".csv")])
    
        # Create output directory if it don't exist
        Path(modelDirectory).mkdir(parents=True, exist_ok=True)
    
        Path_Array = []
        Period_Array = []
        CTP_Array = []
        rsq_Array = []
        rae_Array = []
    
        for fn in d:
            plantID = os.path.splitext(fn)[0]
            dat = pd.read_csv(os.path.join(motionDirectory,fn), comment="#")
            dat = dat.drop("motion x", axis=1)
            # Check if all values are the same, if so, skip this iteration, after printing an error message
            if len(dat["motion y"].unique()) == 1:
                print(f"ERROR: All values are the same for {plantID}")
                continue
            dat.replace([np.inf, -np.inf], np.nan, inplace=True) # replace inf
            dat = dat.fillna(0) # Fill NA with zeros
            dat = dat - dat.mean()
            dat = (dat - detrend(dat, type='linear'))
            dat = np.array(dat.squeeze())
            N = len(dat)
    
            # compute dominant frequency and phase for starting condition
            D = np.fft.fftshift(np.fft.fft(dat))
            
            if len(dat) % 2 == 0:
                mid = len(dat) // 2
            else:
                mid = len(dat) // 2
    
            D = D[mid:mid+11]  # Assumes that the dominant frequency is less than or equal to 10
            ind = np.argmax(np.abs(D))
            freq = ind 
            phase = np.angle(D[ind])  # Starting condition
            amp = np.mean(np.abs(dat))  # Starting condition
    
            initial_model = [freq, phase, amp]
    
            # Non-linear fitting of frequency, phase, and amplitude
            model = minimize(eTRiP._errorFunc, initial_model, args=(dat,), method='Nelder-Mead').x
    
            # Plot results
            f = eTRiP._evaluateModel(model, N)
            plt.plot(dat, 'b', linewidth=1)
            plt.plot(f, 'r', linewidth=1)
    
            if np.count_nonzero(np.logical_not(model)) > 2:
                plt.axis([0, N-1, -1, 1])
            else:
                plt.axis([0, N-1, np.min(dat), np.max(dat)])
    
            plt.legend(['Data', 'Model'])
            plt.title('Frequency = {}'.format(round(model[0],2)))
            # Save the figure
            plt.savefig(os.path.join(modelDirectory,"model_%s.png" % plantID), bbox_inches="tight", facecolor="w");
            # Close the figure
            plt.close()

            freq = model[0]
            Period = N / freq
            Period = Period / 3
            phase = model[1]
            Pjust = 24 / Period
            phi_ang = phase / Pjust
            phi = phi_ang / np.pi
            phi = phi * 12
    
            if phi < 0:
                CTP = (abs(phi) * 24) / Period
            else:
                CTP = 24 - (phi * 24) / Period
    
            # define t and model
            t = np.arange(N)   
            model = [freq, phase, amp]
    
            # Fit the model to the data using curve_fit
            beta, cov = curve_fit(eTRiP._modelFunc, t, dat, p0=model, jac=eTRiP._jacFunc)
    
            # Calculate the residuals and the coefficient of determination
            fittedData = eTRiP._evaluateModel(beta, N)
            residuals = dat - fittedData
            rsq = 1 - np.sum(residuals ** 2) / np.sum((dat - np.mean(dat)) ** 2)
    
    
            # Calculate the confidence interval for frequency (CI_freq)
            ci_freq = np.sqrt(cov[0, 0])
            CI_freq = ci_freq * Period / beta[0]
    
            # Calculate the confidence interval for the amplitude (CI)
            ci_amp = np.sqrt(cov[2, 2]) / 2
            AMP = beta[2]
            RAE = ci_amp / AMP
    
            output_values = [Period, CTP, rsq, RAE]
            output_values = [round(num,2) for num in output_values]
    
            Path_Array.append(plantID)
            Period_Array.append(Period)
            CTP_Array.append(CTP)
            rsq_Array.append(rsq)
            rae_Array.append(RAE)

        Models_data = pd.DataFrame(
            {"ID": Path_Array,
             "Period": Period_Array,
             "CTP": CTP_Array,
             "Rsquared": rsq_Array,
             "RAE": rae_Array,   
            })
    
        Models_data.to_csv(os.path.join(analysisDirectory,"models.csv"),index=False)
      
        
    
    
    

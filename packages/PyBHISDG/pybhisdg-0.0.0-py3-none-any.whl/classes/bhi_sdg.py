import numpy as np
import scipy
from joblib import Parallel, delayed
from warnings import warn
from scipy.signal.windows import kaiser

from numba import njit, prange  # For compiling at run-time

class BHISDG:
    def __init__(self, eeg: np.array = None,
                 eeg_fs: float = None,
                 r_peaks: np.array = None,
                 RR: np.array = None,
                 t_RR: np.array = None,
                 RR_int: np.array = None,
                 t_RR_int: np.array = None,
                 fs_RR_int: float = None,
                 tfr_t: np.array = None,
                 tfr_eeg: np.array = None,
                 tfr_hrv: np.array = None,
                 flims_eeg: dict = {"delta": [1,4], "theta": [4,8], "alpha": [8,12], "beta": [12,32]},
                 fs_bhi: float = 4,
                 window = 2,
                 parallelize: bool = True,
                 wvd_func = None,
                 arx_func = None,
                 arx_orders = [1, 1, 1],
                 cs = 0,
                 cp = 0):
        """ 
        eeg: numpy.array        - of shape [Nc, Nt], where Nc corresponds channels and Nt corresponds to timesamples
        eeg_fs: float           - The sample frequency at which the eeg has been acquired
        r_peaks: numpy.array    - Timepoints for detected R-peaks, provided in seconds.
                                  The timepoints are relative to the first sample of eeg
                                  Alternatively provide the r_peaks-derived values below.
            vvvvvvvvvvvvvvvvvvvvvvvvvvvv If r_peaks is not provided vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
            RR: numpy.array         - series of RR-intervals recorded for each R-peak
            t_RR: numpy.array       - Timeseries corresponding to each value of RR
            RR_int: numpy.array     - Uniformly, interpolated RR-values, sampled at a frequency of fs_RR_int
            t_RR_int: numpy.array   - Timeseries corresponding to each value of RR_int
            fs_RR_int: float        - Frequency for sampling the interpolated RR-values
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ If r_peaks is not provided ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        tfr_t, tfr_eeg and tfr_hrv, offers the user the option of manually providing time-frequency response for the SDG computation
        This would be an alternative to using the member methods compute_tfr_eeg and compute_tfr_hrv
        vvvvvvvvvvvvvvvvvvvvvvvvvvvv optional vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        tfr_t: numpy.array      - (optional) shape [Nt,] Timeseries corresponding to the tfr_eeg and tfr_hrv
        tfr_eeg: numpy.array    - (optional) shape [Nc, Nt, Neb] time-frequency response of the eeg signal
            First index is channel, second is the time index, third is frequency band index. The third index indicates the integration
            over the a frequency band of the PSD, at that particular timepoint for that particular channel
        tfr_hrv: numpy.array    - (optional) shape [Nhb, Nt], time-frequency response of the eeg signal
            First index corresponds to the frequency band index. Default would be integrated over LF and HF frequency bands
            Second index corresponds to the timepoint.
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ optional ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        flims_eeg: dictionary   - Keys corresponds to band names, and values should be a list with lower- and upper frequency boundary in Hz to be analyzed
        fsi_bhi: float          - BHI sampling frequency, typically chosen to be <10Hz
        parallelize: bool       - Flag whether internal SDG computation should be run in parallel on available cores

        Custom functions can optionally be passed as parameters to operate on internal computations.
        vvvvvvvvvvvvvvvvvvvvvvvvvvvv optional vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        wvd_func: function      - function to be called on the analytical interpolated RR signal. This function must take two inputs and provide three outputs as follows
            f, t, wvd = wvd_func(signal, fs) - wvd: np.array [Nf, Nt], is a powerspectral density estimated by the function 
                                                f: np.array [Nf,] is  the a series of frequencies in increasing order, corresponding to the rows of wvd
                                                t: np.array [Nt,] is  the a timeseries corresponding to the columns of wvd
                                                fs: float sampling frequency of the input signal
            wvd_func operates inside the compute_tfr_hrv()
        arx_func: function      - function called estimating the AMPA parameters. This function should output three parameters and take the parameters as follows
            a1, x1, sigma2 = arx_least_squares_fast(y, u, na, nb, nk)   - a1, x1 are the respective autoregressive and exogenous parameters approximated in the arx model, 
                                                                        - sigma2 is the residual noise variance when subtracting the model the signal
                                                                        - y is the tfr signal of a particular channel
                                                                        - u is the tfr signal of a particular hrv band (i.e. LF or HF)
                                                                        - na, nb and nk are polynomial orders of the model being estimated, provided through the arx_orders parameter
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ optional ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        cs, cp: float       - constant sympathetic and parasympathetic terms
        """
        # EEG parameters
        self.eeg            = dict()
        self.eeg["data"]    = eeg
        self.eeg["fs"]      = eeg_fs

        # HRV parameters
        self.hrv = dict()
        # User should either provide all the R_peak derived series or the R_peak series itself
        if ((RR is None) | (t_RR is None) | (t_RR_int is None) | (RR_int is None) | (fs_RR_int is None)):
            if (r_peaks is None):
                warn("BHISDG.__init__: to run the SDG pipeline, the class needs to be initialized with a vector of the r_peak location or all derived parameters")
            else:
                fs_RR_int = fs_bhi
                RR = np.diff(r_peaks)
                t_RR = r_peaks[1:]
                t_RR_int = np.arange(t_RR[0], t_RR[-1], 1/fs_RR_int)
                interpolator = scipy.interpolate.CubicSpline(t_RR, RR)
                RR_int = interpolator.__call__(t_RR_int, extrapolate = False)
        self.hrv["t"]           = t_RR         ### Not used
        self.hrv["data"]        = RR           # This is needed for CPr and CSr computation as well
        self.hrv["t_int"]       = t_RR_int
        self.hrv["data_int"]    = RR_int
        self.hrv["fs_hrv_int"]  = fs_RR_int
        
        # TFR parameters - These inputs can alternatively be provided if not computed using the class methods with the EEG- and HRV parameters
        self.tfr        = dict()
        self.tfr["t"]   = tfr_t
        self.tfr["eeg"] = tfr_eeg
        self.tfr["hrv"] = tfr_hrv
        
        # BHI specific parameters and SDG output
        self.bhi = dict()               # Placeholder for SDG output
        self.bhi["parameters"]  = dict()
        self.bhi["fs_bhi"]      = fs_bhi        # Samples per second of BHI to be computed
        self.bhi["flims_eeg"]   = flims_eeg     # a dict() of names holding lists with upper- and lower level of frequency bands to be analyzed
        self.bhi["bhi events"]  = None          # Will be constructed in the bhi_analysis method
        self.bhi["n events"]    = None          # Will be constructed in the bhi_analysis method

        ## Computational options
        self.opts = dict()
        # Related to HRV time-frequency-response computation
        self.opts["WVD function"] = SPWVD if wvd_func == None else wvd_func
        # Related to SDG related computation
        self.opts["parallelize"] = parallelize      # Option to enable parallelization of the inner bhi method
        self.opts["arx function"] = arx_least_squares_fast if arx_func == None else arx_func
        self.opts["arx orders"] = arx_orders
        
        # Window size for evaluating BHI model - window provided in second
        if window * fs_bhi < 15:            # Must be at least 15 samples
            window = np.ceil(15 / fs_bhi)
            print(f"The time window has been modified to {window:.2f} secs, as a minimum window allowing for robust results with the chosen sampling rate")
        self.opts["wind"] = int(window * fs_bhi)   # self.opts["wind"] is provided in samples, window is provided in seconds
        self.opts["Cs"] = cs
        self.opts["Cp"] = cp

    def compute_tfr_eeg(self, window = 2):
        """
        Input:
            - window: Window used at each time step for the short-time fourier transform
        Output:
            - self.tfr["eeg"]:      [Nch x Nl x Nb]-dimensional numpy.array, where
                                        Nch corresponds to the EEG channels
                                        Nl corresponds to the timepoints at which the stft is computed
                                        Nb corresponds to the frequency bands in self.bhi["flims_eeg"]
            - self.tfr["t"]:        timepoints corresponding to second dimension of self.tfr["eeg"]
                                    timepoints are centered at the window used to compute TFR
        """
        
        Nbands = len(self.bhi["flims_eeg"])
        Nch = int(self.eeg["data"].shape[0])

        w = int(self.eeg["fs"]*window)               # window length in #samples
        step = round(self.eeg["fs"]/self.bhi["fs_bhi"])          # Step size in #samples between consecutive windows

        # ------------------ TFR EEG -----------------
        n = self.eeg["data"].shape[1]       # Length of signal
        l = int(np.floor((n-w)/step))       # number of segments
        TFR_EEG = np.zeros([Nch, l, Nbands])    # Pre-allocation
        i_b_val = 0
        for i_b in self.bhi["flims_eeg"]:           # key values of dictionary
            for i_l in range(l):
                TFR_EEG[:,i_l,i_b_val] = self._bandpower(self.eeg["data"][:,(i_l*step):(i_l*step + w)], fs=self.eeg["fs"], fmin=self.bhi["flims_eeg"][i_b][0], fmax=self.bhi["flims_eeg"][i_b][1])
            i_b_val+=1
        
        t_tfr_eeg = np.arange(0, l)/self.bhi["fs_bhi"] +1       # timepoints for center of the window used to compute TFR
        self.tfr["t"] = t_tfr_eeg
        self.tfr["eeg"] = TFR_EEG
        self.bhi["parameters"]["EEG_TFR_step"] = step
    def compute_tfr_hrv(self):
        """
        Output:
            - self.tfr["hrv"]:      [Nhb x Nl]-dimensional numpy.array, where
                                        Nhb corresponds to the hrv band (i.e. LF and HF)
                                        Nl correpsonds to the time points of self.tfr["t"], the hrv band series is interpolated to these timepoints
            - self.tfr["eeg"]:      updated to only be represented at points where self.tfr["hrv"] is not nan
            - self.tfr["t"]:        updated to only be represented at points where self.tfr["hrv"] is not nan
        """
        
        f, t_tfr, wvd = self.opts["WVD function"](scipy.signal.hilbert(self.hrv["data_int"]-np.mean(self.hrv["data_int"])), fs=self.bhi["fs_bhi"])

        LF = integrate_frequency_band(wvd, 0.04, 0.15, f)
        HF = integrate_frequency_band(wvd, 0.15, 0.40, f)
        
        TFR_HRV = np.zeros([2, len(self.tfr["t"])])

        interpolator = scipy.interpolate.CubicSpline(t_tfr, LF)
        TFR_HRV[0,:] = interpolator.__call__(self.tfr["t"], extrapolate = False)
        interpolator = scipy.interpolate.CubicSpline(t_tfr, HF)
        TFR_HRV[1,:] = interpolator.__call__(self.tfr["t"], extrapolate = False)

        # Stripping away NaNs
        Ind_toKeep = ~np.any(np.isnan(TFR_HRV), axis=0)
        # Ind_toKeep = np.where(np.logical_and(np.logical_not(np.isnan(TFR_HRV[0,:])), np.logical_not(np.isnan(TFR_HRV[1,:]))))[0]
        self.tfr["t"] = self.tfr["t"][Ind_toKeep]
        self.tfr["eeg"] = self.tfr["eeg"][:,Ind_toKeep,:]
        self.tfr["hrv"] = TFR_HRV[:,Ind_toKeep]
    def compute_sdg(self, interpmethod=None):
        """
        Input:
            - interpmethod, string (optional) specifies what internal interpolation method should be used in the internal CPr CSr estimation, options are:
                "PChip" (default), "Akima", "CubicSpline"
        Output:
            - self.bhi["bth"]: numpy.array  [Nb, Nhb, Nc, Nt1] - The computed instantaneous brain-to-heart coupling
                Nb is the EEG frequency bands, NHb is the hrv frequency bands (i.e. LF and Hf)
                Nc is the eeg channel index, Nt1 is the time index corresponding to self.bhi["t"]["time_BToH"]
            - self.bhi["htb"]: numpy.array  [Nb, Nhb, Nc, Nt2] - The computed instantaneous heart-to-brain coupling
                Nb is the EEG frequency bands, NHb is the hrv frequency bands (i.e. LF and Hf)
                Nc is the eeg channel index, Nt2 is the time index corresponding to self.bhi["t"]["time_HToB"]
            - self.bhi["t"]  : dict with numpy.arrays 
                self.bhi["t"]["time_BToH"] is time-series corresponding to the timepoints of self.bhi["bth"]
                self.bhi["t"]["time_HToB"] is time-series corresponding to the timepoints of self.bhi["htb"]
        """
        Nbands = len(self.bhi["flims_eeg"])
        win_RR = 15                 # number RR samples
        first_iter = True
        Nrr_bands = 2
        for eeg_b in range(Nbands):
            for rr_b in range(Nrr_bands):
                tmpHtB, tmpBtH0, tmpBtH1, time_bhi, window = self._bhi_model_wT(eeg_b, rr_b, win_RR, TV = True, interpmethod=interpmethod)[0:5]
                if first_iter:      # Pre-allocation
                    HtB = np.zeros([Nbands, Nrr_bands, *tmpHtB.shape])
                    BtH = np.zeros([Nbands, 2, *tmpBtH0.shape])
                    first_iter = False
                HtB[eeg_b, rr_b,:,:] = tmpHtB
                BtH[eeg_b, 0, :, :] = tmpBtH0
                BtH[eeg_b, 1, :, :] = tmpBtH1
        
        BHI = dict()
        self.bhi["bth"] = BtH
        self.bhi["htb"] = HtB
        self.bhi["t"] = time_bhi

    def bhi_analysis(self, events, window=4):
        """
        events: dict()  - User prepared dict where key values are timepoints given in seconds and the values are the annotated type
        window: float   - the window length to be analysed in seconds
        """
        winlen = window*self.bhi["fs_bhi"]
        # Remove events that do not stay within the time range for which bhi is computed
        tmin = np.max([np.min(self.bhi["t"]["time_BToH"]), np.min(self.bhi["t"]["time_HToB"])])
        tmax = np.min([np.max(self.bhi["t"]["time_BToH"]), np.max(self.bhi["t"]["time_HToB"])])
        events = {k : v for k,v in events.items() if k>tmin and k+window<tmax}
        # Counting the number of occurrences of each event in the annotated member
        nEvs = dict()
        for k in events.values():
            if k not in nEvs: nEvs[k] = 0 
            nEvs[k] += 1
        
        BHI_evs = dict()
        for k in nEvs:
            BHI_evs[k] = np.zeros(np.array([2] + [nEvs[k]] + list(self.bhi["htb"].shape[0:3]) + [winlen]))  # pre-allocating[ [BtH x HtB] x [EEG bands] x [RR bands] x [nchans] x [nevents] ]
        
        # Store median timesegments located to the events object
        ev_counter = {k : 0 for k in nEvs.keys()}
        subscriptable_t = list(events.keys())
        for idx, t, ev in zip(range(len(events)), events.keys(), events.values()):

            # Find indexes along the time-axis corresponding to event
            t_idx_bth = np.where(self.bhi["t"]["time_BToH"] > t)[0][0]
            t_idx_htb = np.where(self.bhi["t"]["time_HToB"] > t)[0][0]
            # Checking for overlapping events
            
            if idx == 61:
                print(t_idx_bth)
                print(t_idx_htb)
                # print(self.bhi["bth"][:,:,:,t_idx_bth:(t_idx_bth+winlen)].shape)
                # print(BHI_evs[ev][0, ev_counter[ev],:,:,:,:].shape)

            if idx != len(events)-1:
                if (t+window) > subscriptable_t[idx+1]:
                    warn("Warning - SDGPy.bhi_analysis: for the chosen window length overlapping events are detected at position {idx:.1i}")
            
            
            # if t_idx_bth.shape[0]
            BHI_evs[ev][0, ev_counter[ev],:,:,:,:] = self.bhi["bth"][:,:,:,t_idx_bth:(t_idx_bth+winlen)]
            BHI_evs[ev][1, ev_counter[ev],:,:,:,:] = self.bhi["htb"][:,:,:,t_idx_htb:(t_idx_htb+winlen)]
            # print(idx)
            
            ev_counter[ev] = ev_counter[ev] + 1
        
        # # Median of medians reflecting
        # BHI_class = dict()
        # for ev in nEvs.keys():
        #     BHI_class[ev] = np.nanmedian(BHI_evs[ev], axis=4).reshape(BHI_evs[ev].shape[0:-1])  # 

        self.bhi["bhi events"] = BHI_evs        # [Direction, #event indices, Brain-freqband, Heart-freqband, Channel, Time]
        self.bhi["n events"] = nEvs

    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv supporting functions vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def _bandpower(self, data: np.array, fs=None, fmin=None, fmax=None, method="fft"):
        # Source inspiration: https://stackoverflow.com/questions/44547669/python-numpy-equivalent-of-bandpower-from-matlab
        f, Pxx = scipy.signal.periodogram(data, fs=fs, window="hamming",detrend=False)
        
        # If only one channel we have to ensure that the time index is aligned with the second dimension
        if data.shape[0] == 1:
            Pxx.reshape([1,-1])
            f.reshape([1,-1])
        ind_min = np.squeeze(np.where(f <= fmin))[-1]
        ind_max = np.squeeze(np.where(f >= fmax))[0] + 1    # open range indexing
        

        # This is implemented according to the matlab procedure for equivalence comparison
        # Small differences occur between the periodogram methods
        df = np.diff(f)
        missingWidth = (f[-1] - f[0]) / (len(f) - 1)
        df = np.append(df, missingWidth)
        return np.dot(Pxx[:,ind_min:ind_max], df[ind_min:ind_max])
        # TODO: Decide if the built-in integrations methods doesn't work better
        # return scipy.integrate.trapezoid(Pxx[:,ind_min:ind_max], axis=1)
        # return scipy.integrate.simpson(Pxx[:,ind_min:ind_max], f[ind_min:ind_max]) # https://stackoverflow.com/a/44915647
    def _bhi_model_wT(self, eeg_b, rr_b, win_RR, TV, interpmethod = None):
        """
        % This function quantifies directional Brain-Heart Interplay (BHI) 
        % through the model proposed by Catrambone et al.(2019) [1].

        % INPUT variables:
        % TFR_EEG = Time course of EEG power spectral density (TFR). This must be a matrix (Dimension: Channels X time)
        %           samples. Each series in each row should be filtered in the desired frequency band of
        %           interest (psi)
        % TFR_HRV = Time course of HRV TFR (Dimension: 1 X time). This should be filtered in the
        % desired frequency band of interest (phi: e.g., LF or HF band)
        % FS      = Sampling Frequency of the two TFRs
        % RR      = HRV series (expressed in seconds)
        % win_RR  = windows length (expressed in seconds) in which the heartbeat generation model (IPFM) is
        % reconstructed (default = 15s)
        % window  = windows length (in seconds) in which the parameters are calculated (default: window*FS >= 15 )
        % TV: time-varying flag. 0 for punctual estimate, 1 for time-resolved estimate.

        % OUTPUT variables:
        % - HeartToBrain = Functional coupling index (c_rrTOeeg(T)) from 
        % HRV Phi-band to EEG Psi-band
        % - BrainToHF, BrainToLF  = Functional coupling indices from  
        %  EEG Psi-band to  HRV-LF or  HRV-HF bands
        % - HeartToBrain_sigma, HeartToBrain_mc = model parameters to be used for fitting evaluation [1]
        % 
        % This software assumes that input series 
        % are all artifact free, e.g., heartbeat dynamics free of algotirhmic and/or physiological artifacts; e.g.
        % EEG series free of artifacts from eye blink, movement, etc.
        ---------------------------------------------------------------------------------------------
         This code implements the theoretical dissertation published in:
         [1] Catrambone Vincenzo, Alberto Greco, Nicola Vanello, Enzo Pasquale Scilingo,
         and Gaetano Valenza. "Time-Resolved Directional Brain–Heart Interplay Measurement 
         Through Synthetic Data Generation Models." 
         Annals of biomedical engineering 47, no. 6 (2019): 1479-1489.
        ---------------------------------------------------------------------------------------------
        Copyright (C) 2019 Vincenzo Catrambone, Gaetano Valenza
        
        This program is a free software; you can redistribute it and/or modify it under
        the terms of the GNU General Public License as published by the Free Software
        Foundation; either version 3 of the License, or (at your option) any later
        version.
        
        If you use this program in support of published research, please include a
        citation of the reference above. If you use this code in a software package,
        please explicitly inform the end users of this copyright notice and ask them
        to cite the reference above in their published research.
        ---------------------------------------------------------------------------------------------
        """
        #%% Testing of the input
        # TODO: Input checking.
        print(self.tfr["eeg"].shape)
        [Nch,Nt] = [self.tfr["eeg"].shape[0],self.tfr["eeg"].shape[1]]

        TFR_EEG = self.tfr["eeg"][:,:,eeg_b].reshape([Nch,Nt])
        TFR_HRV = np.squeeze(self.tfr["hrv"][rr_b,:])
        FS = self.bhi["fs_bhi"]
        time_tfr = self.tfr["t"]

        
        
        CPr, CSr = self._compute_cpr_and_csr(TFR_EEG, TFR_HRV, win_RR, interpmethod=interpmethod)

        TFR_EEG = np.divide( TFR_EEG-np.expand_dims(np.min(TFR_EEG,axis=-1),1), np.expand_dims((np.max(TFR_EEG,axis=-1) - np.min(TFR_EEG,axis=-1)),1) )
        TFR_HRV = np.divide( TFR_HRV-np.min(TFR_HRV,axis=-1), (np.max(TFR_HRV,axis=-1) - np.min(TFR_HRV,axis=-1)) )
        
        # Pre-allocation
        Niter = int(np.min([len(CPr), TFR_EEG.shape[1]-self.opts["wind"], len(TFR_HRV)-self.opts["wind"]]))
        nonan = np.where(np.logical_not(np.isnan(CPr)))[0].shape[0]     # For some parameters the inside model removes the nan positions equivalent to CPr and CSr
        HeartToBrain = np.zeros([Nch, Niter])
        BrainToLF = np.zeros([Nch, nonan])
        BrainToHF = np.zeros([Nch, nonan])
        HeartToBrain_sigma = np.zeros([Nch, Niter])
        HeartToBrain_mc = np.zeros([Nch, Niter])
        # time_bhi = [0]*Nch

        if Nch > 1 and self.opts["parallelize"]:
            out = Parallel(n_jobs=-1, backend="multiprocessing")(delayed(self._BHI_InsideModel)(TFR_EEG[ch,:], TFR_HRV, CPr, CSr, time_tfr, TV) for ch in range(Nch))
            HTB_vals, BLF_vals, BHF_vals, H_sig_vals, H_mc_vals, t_bhi_vals = zip(*out)
            HeartToBrain        = np.stack(HTB_vals,   axis=0)
            BrainToLF           = np.stack(BLF_vals,   axis=0)
            BrainToHF           = np.stack(BHF_vals,   axis=0)
            HeartToBrain_sigma  = np.stack(H_sig_vals, axis=0)
            HeartToBrain_mc     = np.stack(H_mc_vals,  axis=0)
            time_bhi            = t_bhi_vals[0]
        else:
            for ch in range(Nch):
                HeartToBrain[ch,:], BrainToLF[ch,:], BrainToHF[ch,:], HeartToBrain_sigma[ch,:], HeartToBrain_mc[ch,:], time_bhi = self._BHI_InsideModel(TFR_EEG[ch,:], TFR_HRV, CPr, CSr, time_tfr, TV)
        
        return HeartToBrain, BrainToLF, BrainToHF, time_bhi, HeartToBrain_sigma, HeartToBrain_mc
    def _compute_cpr_and_csr(self, TFR_EEG, TFR_HRV, win_RR, interpmethod):
        RR = self.hrv["data"]
        
        #%% RR model parameter estimation
        omega_lf = 2*np.pi *0.1             # LF mean frequency
        omega_hf = 2*np.pi *0.25            # HF mean frequency
        rr_cum = np.cumsum(RR)

        # Index_old is subtracted by 1 and index_new increased by one to accomodate for python 0 index and open-range slicing
        index_old = 0
        index_new = np.where(rr_cum > 1 + win_RR)[0][0]
        CS = np.zeros([int(rr_cum[-1]-win_RR),])
        CP = np.zeros([int(rr_cum[-1]-win_RR),])

        # For every second calculate a window to enable the calculation (overlapping segments)
        for i in range(0,int(rr_cum[-1]-win_RR)):
            HR = 1/ np.mean(RR[(index_old+1):index_new])                    # Time-varying heart rate
            gamma = np.sin(omega_hf/(2*HR))-np.sin(omega_lf/(2*HR))     # gamma parameter of the IPFM model
            MM = np.array([[np.sin(omega_hf/(2*HR))*omega_lf*HR/(4*np.sin(omega_lf/(2*HR))), -np.sqrt(2)*omega_lf*HR/(8*np.sin(omega_lf/(2*HR)))],
                            [-np.sin(omega_lf/(2*HR))*omega_hf*HR/(4*np.sin(omega_hf/(2*HR))), np.sqrt(2)*omega_hf*HR/(8*np.sin(omega_hf/(2*HR)))]])
            # TODO: Check to see if these two poincare parameters are correctly computed (blindly copied from the Matlab code)
            L = np.max(RR[index_old:index_new]) - np.min(RR[index_old:index_new])
            W = np.sqrt(2)*np.max(np.abs(RR[(index_old+1):index_new] - RR[index_old:(index_new-1)]))
            CC = 1/gamma * np.dot(MM, np.array([L,W]))
            CS[i] = CC[0]; CP[i] = CC[1]
            index_old = np.where(rr_cum > (i+1))[0][0]
            index_new = np.where(rr_cum > (i+1+win_RR))[0][0]

        # Interpolation and normalization to the [0, 1]-range of the parameters for computational reasons
        time_cs = np.median(np.arange(1, win_RR+1)) + np.arange(1,len(CS)+1)      # mid-points for the windows used in previous for-loop
        
        if interpmethod == "Akima":
            interpolator = scipy.interpolate.Akima1DInterpolator(time_cs, CS)
            CSr = interpolator.__call__(self.tfr["t"], extrapolate = False)       # CS Re-sampled        # A bunch of nan's at beginning and end like in Matlab
            interpolator = scipy.interpolate.Akima1DInterpolator(time_cs, CP)
            CPr = interpolator.__call__(self.tfr["t"], extrapolate = False)
        elif interpmethod == "CubicSpline":
            interpolator = scipy.interpolate.CubicSpline(time_cs, CS)
            CSr = interpolator.__call__(self.tfr["t"], extrapolate = False)       # CS Re-sampled        # A bunch of nan's at beginning and end like in Matlab
            interpolator = scipy.interpolate.CubicSpline(time_cs, CP)
            CPr = interpolator.__call__(self.tfr["t"], extrapolate = False)
        else:       # Pchip
            interpolator = scipy.interpolate.PchipInterpolator(time_cs, CS)
            CSr = interpolator.__call__(self.tfr["t"], extrapolate = False)       # CS Re-sampled        # A bunch of nan's at beginning and end like in Matlab
            interpolator = scipy.interpolate.PchipInterpolator(time_cs, CP)
            CPr = interpolator.__call__(self.tfr["t"], extrapolate = False)

        CSr = (CSr-np.nanmin(CSr))/(np.nanmax(CSr)-np.nanmin(CSr))
        CPr = (CPr-np.nanmin(CPr))/(np.nanmax(CPr)-np.nanmin(CPr))

        return CPr, CSr
    def _BHI_InsideModel(self, TFR_ch, TFR_rr, CPr, CSr, time_tfr, TV):
        
        Nt = len(TFR_ch)
        Cs1 = self.opts["Cs"]
        Cp1 = self.opts["Cp"]

        if TV:
            # The maximum number of iterations is calculated from the data lengths.
            Niterations = int(np.min([len(CPr), Nt-self.opts["wind"], len(TFR_rr)-self.opts["wind"]]))
            # Pre-allocation
            HToB_sigma =        np.zeros([Niterations,])
            HToB_mc =           np.zeros([Niterations,])
            HToB =              np.zeros([Niterations,])
            time_HToB =         np.zeros([Niterations,])
            medianTime_P_eeg =  np.zeros([Niterations,])
            BToHF =             np.zeros([Niterations,])
            BToLF =             np.zeros([Niterations,])
            for i in range(0, Niterations):
                a1, x1, sigma2 = self.opts["arx function"](TFR_ch[i:(i+self.opts["wind"]+1)], TFR_rr[i:(i+self.opts["wind"]+1)], na=self.opts["arx orders"][0], nb=self.opts["arx orders"][1], nk=self.opts["arx orders"][2])
                HToB_sigma[i] = np.sqrt(sigma2)
                HToB_mc[i] = -a1
                HToB[i] = x1
                time_HToB[i] = time_tfr[int(self.opts["wind"]/2+i)]
                medianTime_P_eeg[i] = np.nanmedian(TFR_ch[i:(i+self.opts["wind"]+1)])

                try:
                    BToHF[i] = (CPr[i].squeeze()-Cp1)/medianTime_P_eeg[i]
                    BToLF[i] = (CSr[i].squeeze()-Cs1)/medianTime_P_eeg[i]
                except:
                    # TODO: Make the exception like in the MATLAB code when you figure out the reason for the try-catch
                    print("Exception has occured in BHI_InsideModel")
            
            time_BToH = time_HToB[np.where(np.logical_not(np.isnan(BToLF)))[0]]
            BToLF = BToLF[np.where(np.logical_not(np.isnan(BToLF)))[0]]
            BToHF = BToHF[np.where(np.logical_not(np.isnan(BToHF)))[0]]

            ## The np.convolve is not identical to matlabs conv, when using the same. Check the custom made convolve_name function for details
            # HToB =  np.convolve(HToB,  2/window*np.ones(int(window/2)), "same")
            # BToHF = np.convolve(BToHF, 2/window*np.ones(int(window/2)), "same")
            # BToLF = np.convolve(BToLF, 2/window*np.ones(int(window/2)), "same")
            HToB =  convolve_same(HToB,  2/self.opts["wind"]*np.ones(int(self.opts["wind"]/2)))
            BToHF = convolve_same(BToHF, 2/self.opts["wind"]*np.ones(int(self.opts["wind"]/2)))
            BToLF = convolve_same(BToLF, 2/self.opts["wind"]*np.ones(int(self.opts["wind"]/2)))
        else:
            a1, x1, sigma2 = arx_least_squares(TFR_ch, TFR_rr, na=1, nb=1, nk=1)  # indices for the estimated parameters

            HToB_sigma = np.sqrt(sigma2)
            HToB_mc = a1
            HToB = x1
            time_HToB = 1
            medianTime_P_eeg = np.nanmedian(TFR_ch)

            # Brain to HF
            # The TFR_ch is normalized to [0,1], meaning that dividing by the individual values, like in the matlab code, will result in division by 0 somewhere along the array
            # Instead I chose to divide by the median of the array in line with what is done in the loop if TV==True
            BToHF = np.nanmedian((CPr-Cp1)/medianTime_P_eeg)
            BToLF = np.nanmedian((CSr-Cs1)/medianTime_P_eeg)
            time_BToH = 1
            
        time_bhi = dict()
        time_bhi["time_HToB"] = time_HToB
        time_bhi["time_BToH"] = time_BToH

        return [HToB, BToLF, BToHF, HToB_sigma, HToB_mc, time_bhi]

    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ supporting functions ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# vvvvvvvvvvvvvvvvvvvvvvvvvv Non-class specific support functions vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def convolve_same(A, B):
    """
    This function replicates the Matlab convolve function, with the "same" option enabled
    Python also has a np.convolve function with the optional "same" parameter. However this
    shifts the input relative to matlab output if the second input parameter is even.
    for example
    a = [5, 4, 3, 2, 1]
    b = [2, 2, 2, 2]
    full (a,b)-convolution = [2, 6, 12, 20, 28, 24, 24, 18, 10]
    np.convolve(a, b, "same") => [6, 12, 20, 28, 24]
    (matlab) conv(a, b, "same") => [12, 20, 28, 24, 18]
    
    To make the function comparable to matlab, the special case is considered
    """
    if len(B) % 2 == 0:
        conv_result = np.convolve(A,B)
        start_idx = int(np.ceil((len(conv_result)-len(A))/2))
        return conv_result[start_idx:start_idx+len(A)]
    else:
        return np.convolve(A,B,"same")
def arx_least_squares(y, u, na=1, nb=1, nk=1):
    """
    This model performed best in when replicating the MATLAB implementation

    Fit ARX model: y[t] + a1*y[t-1] = b1*u[t-nk]
    Returns: a1, b1
    """
    N = len(y)
    # Build regression matrix
    Y = y[max(na, nb+nk-1):]
    Phi = []
    for t in range(max(na, nb+nk-1), N):
        row = []
        # Output lags
        for i in range(1, na+1):
            row.append(-y[t-i])
        # Input lags (with delay nk)
        for j in range(nb):
            row.append(u[t-nk-j])
        Phi.append(row)
    Phi = np.array(Phi)
    # Least squares solution
    theta, *_ = np.linalg.lstsq(Phi, Y, rcond=None)
    # Computing error term
    Y_pred = Phi @ theta
    residuals = Y - Y_pred
    
    dof = len(residuals)-(na+nb)
    variance = np.sum(np.power(residuals,2))/dof
    return (*theta, variance)
@njit
def _arx_solve_compiled(y, u, na, nb, nk):
    N = y.shape[0]
    start = na if na > (nb + nk - 1) else (nb + nk - 1)
    rows = N - start
    cols = na + nb
    if rows <= 0:
        return np.empty(0, dtype=np.float64), 0.0, start

    Phi = np.empty((rows, cols), dtype=np.float64)
    Y = np.empty(rows, dtype=np.float64)

    for idx in range(rows):
        t = idx + start
        Y[idx] = y[t]
        # AR lags: -y[t-1], -y[t-2], ...
        for i in range(na):
            Phi[idx, i] = -y[t - (i + 1)]
        # Input lags with delay nk
        for j in range(nb):
            Phi[idx, na + j] = u[t - (nk + j)]

    # Normal equations: (Phi^T Phi) theta = Phi^T Y
    A = Phi.T.dot(Phi)
    b = Phi.T.dot(Y)
    # Solve linear system (assumes A is invertible / well-conditioned)
    theta = np.linalg.solve(A, b)

    # residuals and variance
    Y_pred = Phi.dot(theta)
    s = 0.0
    for i in range(rows):
        diff = Y[i] - Y_pred[i]
        s += diff * diff
    dof = rows - (na + nb)
    if dof > 0:
        variance = s / dof
    else:
        variance = 0.0
    return theta, variance, start
def arx_least_squares_fast(y, u, na=1, nb=1, nk=1):
    """
    Compiled ARX via numba (_arx_solve_compiled).
    Returns: (a1, b1, variance) for na=1,nb=1 (or theta elements and variance)
    """
    y = np.asarray(y, dtype=np.float64).ravel()
    u = np.asarray(u, dtype=np.float64).ravel()
    try:
        theta, variance, _ = _arx_solve_compiled(y, u, na, nb, nk)
    except:
        return [0, 0, 0]
    if theta.size == 0:
        # not enough data; return zeros and zero variance
        return tuple([0.0] * (na + nb)) + (0.0,)

    # Return parameters plus variance to match previous API
    # previous code returned (*theta, variance)
    out = tuple(theta.tolist()) + (variance,)
    return out

def SPWVD(signal, fs):
    # TODO: Inspired by MATLAB. Investigate possible copyright disparities
    # Make even
    if len(signal) % 2 == 1:
        signal = np.append(signal,0)
    # In matlab if the input is complex the data, an zeros are appended equivalently to the length
    signal = np.append(signal, np.zeros(len(signal)))

    # Change to offer an input value
    DataLen = len(signal)
    FreqBins = int(DataLen/2)

    # Smoothing windows
    nTimeWin = round(DataLen / 10)
    if nTimeWin % 2 == 0:
        nTimeWin += 1
    timeWindow = kaiser(nTimeWin, 20)

    nFreqWin = np.min([FreqBins, np.round(DataLen/4)])
    if nFreqWin % 2 == 0:
        nFreqWin += 1
    freqWindow = kaiser(nFreqWin, 20)

    # time vector
    totalDuration = 0.5*DataLen/fs
    timeVec = np.linspace(0, totalDuration, DataLen)


    ## In the wvdImpl file
    freqVec = np.linspace(0,1, FreqBins)
    N2 = DataLen
    N = int(np.ceil(DataLen/2))
    # Don't know yet what these will be used for
    nhTime = int(np.floor(DataLen/2))
    nhFreq = int(np.ceil(FreqBins/2))

    ## In the getSpwvdWindowParams file
    nhFreqWin = int(np.floor(nFreqWin/2))
    maxLag = int(np.floor(nTimeWin/2))

    G1 = np.roll(freqWindow, np.ceil(len(freqWindow)/2))
    g2 = np.roll(timeWindow, np.ceil(len(timeWindow)/2))
    ##

    nVec = np.linspace(0, N-1, N)
    mVec = np.linspace(0, maxLag, maxLag+1)
    M = maxLag+1

    nVecMN = np.matlib.repmat(nVec.reshape(1,-1), M ,1)
    mVecMN = np.matlib.repmat(np.reshape(np.floor(mVec/2), (-1,1)), 1,N)
    posLagMat = np.mod(nVecMN + np.matlib.repmat(np.ceil(np.reshape(mVec, (-1,1))/2),1,N), N2).astype(int)
    negLagMat = np.mod(nVecMN - mVecMN, N2).astype(int)

    autocorr = np.multiply(signal[posLagMat], np.conjugate(signal[negLagMat]))
    # --- applying time smoothing
    mnMat = np.multiply(np.matlib.repmat(np.reshape(g2[0:maxLag+1],(-1,1)),1,N), autocorr)
    
    #  --- Applying frequency smoothing
    afMat = scipy.fft.fft(mnMat,axis=1)

    # Indices
    noDoppStart = int(nhFreqWin+1)
    noDoppStop = int(nhTime-nhFreqWin-1-(np.remainder(nFreqWin,2)-1))
    noDoppSupportIxs = np.linspace(noDoppStart,noDoppStop, noDoppStop-noDoppStart+1).astype(int)
    posDoppIxs = np.linspace(0,nhFreqWin, nhFreqWin+1).astype(int)
    negDoppIx = nhFreqWin - (nFreqWin % 2 == 0).astype(int)

    # Matrix to contain the filtered frequency spectrum
    afWinMat = np.zeros((maxLag+1, nhTime),dtype=complex)
    afMatRow = afMat.shape[0]

    # filtering
    afWinMat[:,posDoppIxs] = np.multiply(np.matlib.repmat(np.reshape(G1[posDoppIxs],(1,-1)),afMatRow,1), afMat[:,posDoppIxs])
    afWinMat[:,-1-negDoppIx:] = np.multiply(np.matlib.repmat(np.reshape(G1[-1-negDoppIx:],(1,-1)),afMatRow,1), afMat[:,-1-negDoppIx:])
    afWinMat[:,noDoppSupportIxs] = 0

    # Return to time-lag domain
    mnMat = scipy.fft.ifft(afWinMat,axis=1)

    # Due to symmetry in autocorrelation we can retain only half without loss of information
    kmat = np.zeros((2*FreqBins, nhTime), dtype=complex)
    kmat[0:maxLag+1,:] = mnMat[0:maxLag+1, 0:nhTime]

    # Use time-lag function symmetry to obtain (-) lag vals from (+) vals.
    mEvenIxs = np.linspace(1, nhFreq-1, nhFreq-1).astype(int)
    mOddIxs = np.linspace(0, nhFreq-1, nhFreq).astype(int)
    # Use time-lag function symmetry to obtain (-) lag vals from (+) vals.
    kmat[[2*FreqBins- 2*mEvenIxs],:] = np.conjugate(kmat[2*mEvenIxs,:])
    kmat[[2*FreqBins- 2*mOddIxs-1],:] = np.conjugate(kmat[2*mOddIxs+1,:])

    # Convert to Time-frequency domain with FT m->k
    wvdMat = np.zeros((FreqBins, N2),dtype=complex)

    # "Even lag values are conjugate symmetric. Here we calculate WVD[k,2n] = FT{K[2m,n]}"
    wvdMat[:,0::2] = scipy.fft.fft(kmat[0::2,:],axis=0)

    kMatPrimeOdd = kmat[1::2,:]
    nFreqOdd = int(kMatPrimeOdd.shape[0])
    nhFreqOdd = int(np.ceil(nFreqOdd/2))
    kMatHat = np.zeros((nFreqOdd, nhTime),dtype=complex)
    kMatHat[0,:] = np.imag(kMatPrimeOdd[0,:])
    # frexIxs1 = np.linspace()
    # Calculate (1/2j) * [ K[2m+1,n] - K*[2*Nf-2m-1,n] ] for nonzero m.
    kMatHat[1:(nhFreqOdd+1), :] = 1/(2*1j) * (kMatPrimeOdd[1:(nhFreqOdd+1), :] - np.conjugate(kMatPrimeOdd[nFreqOdd::-1,:][:nFreqOdd-nhFreqOdd,:]))
    kMatHat[(nhFreqOdd+1):,:] = np.conjugate(kMatHat[1:nhFreqOdd,:][::-1,:])

    tfMat = scipy.fft.fft(kMatHat,axis=0)
    k = np.linspace(1,FreqBins-1, FreqBins-1).astype(int)
    A = np.cos(np.pi/FreqBins* k) 
    B = np.sin(np.pi/FreqBins* k) 

    wvdMat[k,1::2] = np.matlib.repmat( np.reshape((A*A+B*B)/B, (-1,1)), 1, tfMat.shape[1] ) *tfMat[k,:]
    wvdMat[0,1::2] = np.sum(kmat[1::2,:],axis=0)
    #
    freqVec = freqVec*fs/2
    return freqVec, timeVec, np.real(wvdMat)
def integrate_frequency_band(TFR, f1, f2, f):
    # Integrates over frequency band spanned by f1 and f2
    idx1 = np.where(f1<=f)[0][0]
    idx2 = np.where(f<=f2)[0][-1]+1
    return scipy.integrate.trapezoid(TFR[idx1:idx2,:], axis=0)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^ Non-class specific support functions ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



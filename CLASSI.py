import pywt
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, detrend
import os
from scipy.signal import find_peaks

path = 'C:\\Users\\GauravUgale\\Downloads\\Dharuben_new\\'
files = [x for x in os.listdir(path) if x.endswith('.csv')]

data = {'FileName':[], 'std_devi':[]}

for name in files:
    name = name.split('.')[0]

    header_list = ['MLII', 'Value', 'VALUE', 'ECG', '0', 'val','V1', 'II', 'noise1', 'noise2','ii']
    for header in header_list:
        try:
            y = pd.read_csv(f'{path}{name}.csv')[header].values
        except:
            pass
    # Generate an ECG signal with added high frequency noise
    fs = 700  # Sample rate
    # Perform Wavelet denoising

    peaks, properties = find_peaks(y, prominence=0.0005, width=0.05)
    # print("Peaks max:", x[peaks[0]],"\nPeaks Loc:",peaks[0])
    plt.plot(y) 
    plt.plot(peaks, y[peaks], "y")
    plt.vlines(x=peaks, ymin=y[peaks] - properties["prominences"],
    ymax = y[peaks], color = "C1")
    plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"],
            xmax=properties["right_ips"], color = "C1")

    # print(data)

    # xx= pd.DataFrame(data)
    # xx.to_csv('new_std.csv')

    # def signal_properties(signal, ):
    # fs=250;nperseg=1024
    # f, psd = welch(y, fs=fs, nperseg=nperseg)
    # spectral_centroid = np.sum(f * psd) / np.sum(psd)
    # spectral_bandwidth = np.sqrt(np.sum(psd * (f - spectral_centroid) ** 2) / np.sum(psd))

    plt.plot(y, 'r');plt.plot(peaks,'g');plt.plot(y,'orange')
    plt.figure(figsize=(10,4))
    if len(peaks)>= 30:
        plt.plot(y)
        plt.savefig(f'C:\\Users\\GauravUgale\\Desktop\\test_to\\new_high\\{name}.jpg')
        
    else:
        plt.plot(y)
        plt.savefig(f'C:\\Users\\GauravUgale\\Desktop\\test_to\\new_normal\\{name}.jpg')
    plt.close()
    # fig, axes = plt.subplots(2, 1, figsize=(9, 5), sharex=True)
    # fig.subplots_adjust(hspace=0)
    # axes[0].plot(y, c='k', label='original data')
    # axes[0].legend()
    # axes[1].plot(spectral_bandwidth,label='filter-1')
    # axes[1].legend()
    # # axes[2].plot(z,label='filter-1')
    # # axes[2].legend()
    # # plt.show()

    # plt.savefig(spectral_bandwidth)

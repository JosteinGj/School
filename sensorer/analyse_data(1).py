import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import math as m




def time_delay(signal_matrix, channels,plot=True):
    sig1 = signal_matrix[31250//10:, channels[0]]
    sig2 = signal_matrix[31250//10:, channels[1]]

    #xcorr=np.correlate(sig1,sig2,"full")
    winsize = 10000
    mid = len(sig1)//2
    winsig1 = sig1[(mid - winsize):(mid + winsize)]
    winsig2 = sig2[(mid - winsize):(mid + winsize)]

    winautocorr1 = np.correlate(winsig1, winsig1,"full")
    corrmid = np.argmax(np.abs(winautocorr1))
    corr = np.correlate(winsig1, winsig2,"full")
    delay = corrmid-np.argmax(np.abs(corr))

    if plot:
        plotwin = 500

        plt.plot(range(-plotwin, plotwin), corr[len(corr)//2-plotwin:len(corr)//2+plotwin]/max(corr))
        plt.show()
    return delay



def direction_detection(data):
    dt = np.ones((3, 3))
    for i in range(3):
        for j in range(3):
            dt[i, j] = time_delay(data, (i, j))
    print(dt)
    theta=m.atan2(np.sqrt(3)*(dt[1, 0]+dt[2,0]),(dt[1,0]-dt[2,0]-2*dt[2,1]))
    print(theta)
    print(np.rad2deg(theta))
    return theta

def raspi_import(path, channels=5):
    """
    Import data produced using adc_sampler.c.
    Returns sample period and ndarray with one column per channel.
    Sampled data for each channel, in dimensions NUM_SAMPLES x NUM_CHANNELS.
    """

    with open(path, 'r') as fid:
        sample_period = np.fromfile(fid, count=1, dtype=float)[0]
        data = np.fromfile(fid, dtype=np.uint16)
        data = data.reshape((-1, channels))
    return sample_period, data



# Import data from bin file
sample_period, data = raspi_import('sampling.bin')

data = signal.detrend(data, axis=0)  # removes DC component for each channel
sample_period *= 1e-6  # change unit to micro seconds

# Generate time axis
num_of_samples = data.shape[0]  # returns shape of matrix
t = np.linspace(start=0, stop=num_of_samples*sample_period, num=num_of_samples)

# Generate frequency axis and take FFT
freq = np.fft.fftfreq(n=num_of_samples, d=sample_period)
spectrum = np.fft.fft(data, axis=0)  # takes FFT of all channels

direction_detection(data)

# Plot the results in two subplots
# NOTICE: This lazily plots the entire matrixes. All the channels will be put into the same plots.
# If you want a single channel, use data[:,n] to get channel n
plt.subplot(2, 1, 1)
plt.title("Time domain signal")
plt.xlabel("Time [us]")
plt.ylabel("Voltage")
plt.plot(t[31250//10:], data[31250//10:,0])

plt.subplot(2, 1, 2)
plt.title("Power spectrum of signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Power [dB]")
plt.plot(freq, 20*np.log(np.abs(spectrum/np.max(spectrum)))) # get the power spectrum

plt.show()

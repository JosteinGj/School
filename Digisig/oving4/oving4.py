import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft as fft

L = 500
A = 1 / 4
fx = 0.04
fy = 0.10
n = np.arange(500)
r = 0.999

noise = np.random.normal(size=L)
signal_x= A * np.cos(2 * np.pi * fx * n)
signal_y= A * np.cos(2 * np.pi * fy * n)
signal = signal_x + signal_y
noisy_signal = signal + noise

Fast_and_Furious_Tansform = fft.fft(signal, n=2048)
NoisyFFT = fft.fft(noisy_signal, n=2048)
numerator_poly1 = [1, 1]
numerator_poly2 = [1,-1]

 
b0x = (1 - r) * np.sqrt(1 + r ** 2 - 2 * r * np.cos(4 * np.pi * fx))/np.sqrt(2*(1-np.cos(2*np.pi*fx)))
b0y = (1 - r) * np.sqrt(1 + r ** 2 - 2 * r * np.cos(4 * np.pi * fy))/np.sqrt(2*(1-np.cos(2*np.pi*fy)))

# polynomials for numerators
filter_num_x = b0x * sig.convolve(numerator_poly1, numerator_poly2)
filter_num_y = b0y * sig.convolve(numerator_poly1, numerator_poly2)

# polynomials for denominators in factorized form
x_filter_denom_poly1, x_filter_denom_poly2 = [1, -r * np.exp(1j * 2 * np.pi * fx)], [1, -r * np.exp(-1j * 2 * np.pi * fx)]
y_filter_denom_poly1, y_filter_denom_poly2 = [1, -r * np.exp(1j * 2 * np.pi * fy)], [1, -r * np.exp(-1j * 2 * np.pi * fy)]

# convolve to find polynomials proper polynomials
x_filter_denominator = sig.convolve(x_filter_denom_poly1, x_filter_denom_poly2)
y_filter_denominator = sig.convolve(y_filter_denom_poly1,y_filter_denom_poly2)

# filter that shit
distorted_signal_x_filtered = sig.lfilter(filter_num_x, x_filter_denominator,noisy_signal)
distorted_signal_y_filtered = sig.lfilter(filter_num_y, y_filter_denominator,noisy_signal)

# plot those zeros and poles
zeros=[1,-1]
poles_x=[r * np.exp(1j * 2 * np.pi * fx), r * np.exp(-1j * 2 * np.pi * fx)]
poles_y=[r * np.exp(1j * 2 * np.pi * fy), r * np.exp(-1j * 2 * np.pi * fy)]
theta=np.linspace(0, 2 * np.pi, 10000)


def task4a():

    # undistorted signal
    plt.plot(signal,label="undistorted signal")
    plt.xlabel("samples")
    plt.ylabel("amplitude")
    plt.title("Undistorted signal")
    plt.savefig("Digsig4_undistorted_signal.pdf")
    plt.show()

    # distorted signal
    plt.plot(noisy_signal,label="distorted signal")
    plt.title("Distorted signal")
    plt.xlabel("samples")
    plt.ylabel("amplitude")
    plt.savefig("Digsig4_distorted_signal.pdf")
    plt.show()

    # undistorted fft
    plt.plot(fft.fftfreq(2048),np.abs(Fast_and_Furious_Tansform)**2, label="undistorted signal")
    plt.xlabel("freq")
    plt.ylabel("Spectral density")
    plt.title("Spectral density plot(Undistorted)")
    plt.savefig("Digsig4_undistorted_spectral_desnity.pdf")
    plt.show()

    # distorted fft
    plt.plot(fft.fftfreq(2048),np.abs(NoisyFFT)** 2, label="undistorted signal")
    plt.xlabel("freq")
    plt.ylabel("Spectral density")
    plt.title("Spectral density plot(distorted)")
    plt.savefig("Digsig4_distorted_spectral_desnity.pdf")
    plt.show()


def task4b():
    # freqency response of x filter
    w, h = sig.freqz(filter_num_x, x_filter_denominator)
    plt.plot(w, 20 * np.log10(abs(h)), "b")
    plt.title("frequency response of x filter")
    plt.xlabel("Normalized freqency (radians/cycle)")
    plt.ylabel("Magnitude (dB)")
    plt.savefig("Digsig4_xfilter_freqresp.pdf")
    plt.show()
    # freqency response of y filter
    w, h = sig.freqz(filter_num_y, y_filter_denominator)
    plt.plot(w, 20 * np.log10(abs(h)),"b")
    plt.title("frequency response of x filter")
    plt.ylabel("Magnitude (dB)")
    plt.xlabel("Normalized freqency (radians/cycle)")
    plt.savefig("Digsig4_yfilter_freqresp.pdf")
    plt.show()

    # zero-pole plot of y filter
    plt.plot(np.sin(theta),np.cos(theta),"--k",)
    plt.plot(np.real(zeros),np.imag(zeros),"o",label="zeros")
    plt.plot(np.real(poles_y),np.imag(poles_y),"x",label="poles of y-filter")
    plt.xlabel("real part")
    plt.ylabel("imaginary part")
    plt.title("zero pole plot for resonator y-filter")
    plt.legend(loc="upper right")
    plt.savefig("Digsig4_ZP_y_plot.pdf")
    plt.show()


    # zero-pole plot of y filter
    plt.plot(np.sin(theta),np.cos(theta),"--k",)
    plt.plot(np.real(zeros),np.imag(zeros),"o",label="zeros")
    plt.plot(np.real(poles_x),np.imag(poles_x),"x",label="poles of x-filter")
    plt.xlabel("real part")
    plt.ylabel("imaginary part")
    plt.title("zero pole plot for resonator x-filter")
    plt.legend(loc="upper right")
    plt.savefig("Digsig4_ZP_x_plot.pdf")
    plt.show()


def task4c():
    
    # x filtered signal
    plt.plot(distorted_signal_x_filtered, label="distorted signal filtered for x signal")
    plt.title("Distorted signal filtered for x")
    plt.xlabel("samples")
    plt.ylabel("amplitude")
    plt.savefig("Digsig4_distorted_signal_x_filtered.pdf")
    plt.show()


    # x filtered spectral density
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(distorted_signal_x_filtered,n=2048))**2)
    plt.xlabel("normalized freqencies")
    plt.ylabel("amplitudes")
    plt.title("specral density of x-filterd system")
    plt.savefig("Digsig4_specdensity_x_filter.pdf")
    plt.show()


    # y filtered signal
    plt.plot(distorted_signal_y_filtered, label="distorted signal filtered for y signal")
    plt.title("Distorted signal filtered for y")
    plt.xlabel("samples")
    plt.ylabel("amplitude")
    plt.savefig("Digsig4_distorted_signal_y_filtered.pdf")
    plt.show()

    # y filtered spectral density
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(distorted_signal_y_filtered,n=2048))**2)
    plt.xlabel("normalized freqencies")
    plt.ylabel("amplitudes")
    plt.title("specral density of y-filterd system")
    plt.savefig("Digsig4_specdensity_y_filter.pdf")
    plt.show()


def task4d():

    totalfilter_numerator=sig.convolve(filter_num_x, filter_num_y)
    totalfilter_denominator=sig.convolve(x_filter_denominator,y_filter_denominator)
    total_filtered_signal=sig.lfilter(totalfilter_numerator, totalfilter_denominator,noisy_signal)


    # Freqency magnituede response of total filter
    w, h = sig.freqz(totalfilter_numerator, totalfilter_denominator)
    plt.plot(w, 20 * np.log10(abs(h)), "b")
    plt.ylabel("magnitude")
    plt.xlabel("normalized freqency (cycles/samples)")
    plt.title("frequency response of x filter")
    plt.savefig("Digsig4_fullfilter_mag_resp.pdf")
    plt.show()


    # pole zero plot of total filter
    plt.plot(np.sin(theta),np.cos(theta),"--k",)
    total_zeros = zeros + zeros
    total_poles = poles_x + poles_y


    plt.plot(np.real(total_zeros), np.imag(total_zeros), "o", label="zeros")
    plt.plot(np.real(total_poles), np.imag(total_poles), "x", label="poles")
    plt.xlabel("real part")
    plt.ylabel("imaginary part")
    plt.title("zero pole plot for resonator filter")
    plt.savefig("Digsig4_fullfilter_ZPplot.pdf")
    plt.show()


    # x and y filteded signal 
    plt.plot(total_filtered_signal,label="undistorted signal")
    plt.xlabel("samples")
    plt.ylabel("amplitude")
    plt.title("Doublefiltered signal")
    plt.savefig("Digsig4_doublefiltered_signal.pdf")
    plt.show()


     # total filtered spectral density
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(total_filtered_signal,n=2048))**2)
    plt.xlabel("normalized freqencies")
    plt.ylabel("amplitudes")
    plt.title("specral density of doubel-filtered system")
    plt.savefig("Digsig4_doublefilter_specdensity.pdf")
    plt.show()


    # comparative plot of signals. 
    plt.plot(signal,label="pure signal")
    plt.plot(noisy_signal,label="noisy signal")
    plt.plot(total_filtered_signal,label="filtered signal")
    plt.legend(loc="upper right")
    plt.xlabel("sample")
    plt.ylabel("signal strength")
    plt.savefig("digsig4_comparative_plots.pdf")
    plt.show()

    # comparative plot of spectrum
 
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(distorted_signal_x_filtered,n=2048))**2)
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(distorted_signal_y_filtered,n=2048))**2)
    plt.plot(np.fft.fftfreq(n=2048), np.abs(np.fft.fft(total_filtered_signal,n=2048))**2)
    plt.xlabel("normalized freqencies")
    plt.ylabel("amplitudes")
    plt.title("specral density of double-filtered system")
    plt.savefig("Digsig4_comparative_specdensity.pdf")
    plt.legend(loc="upper right")
    plt.show()


task4a()
task4b()
task4c()
task4d()

# zero-pole plot of x and y filters
plt.plot(np.sin(theta),np.cos(theta),"--k",)
plt.plot(0,0,"o",label="zeros")
plt.plot(-0.9,0,"x",label="poles of x-filter")
plt.xlabel("real part")
plt.ylabel("imaginary part")
plt.title("zero pole plot for system")
plt.legend(loc="upper right")
plt.savefig("Digsig4_task_1a_ZPa=-0.9.pdf")
plt.show()
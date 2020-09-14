import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import functools as ft


def u(t):
    return np.heaviside(t, 1 / 2)


def taskA24(t):
    return (u(-t - 1) - t * u(t + 1) * u(-t + 1) +
            (2 * t * u(t - 1) * u(-t + 2)) + u(t - 2))

def plota24():
    t = np.linspace(-2, 3, 1000)
    x1 = taskA24(t)
    x2 = taskA24(4 * t + 3)
    x3 = taskA24(-3 * t + 2)
    plt.plot(t, x1, label="original signal")
    plt.legend()
    plt.show()
    plt.plot(t, x2, label="transformation 1")
    plt.legend()
    plt.show()
    plt.plot(t, x3, label="transfomration 2")
    plt.legend()
    plt.show()


plota24()


def trunctTriPulse(t):
    return (-t/0.0075 + 1) * u(t) * u(-t + 0.0075)


def rectPulse(t, width):
    return u(t * width / 2) * u(-t + width / 2)


def gaussPulse(t, width):
    return np.exp(-1 * (t/width) ** 2)


def rectwave(pulsewidth, separation, numOfwaves):
    t = np.linspace(-(pulsewidth + separation) * (numOfwaves + 0.1) / 2,
                    (pulsewidth + separation) * (numOfwaves + 0.1) / 2,
                    1000000)
    dutycycle = pulsewidth/(pulsewidth+separation)
    signal = sig.square(2 * np.pi * 1 / (pulsewidth + separation) * t,
                        dutycycle) / 2 + 1 / 2
    return t, signal



interval = np.linspace(-0.03, 0.03, 1000000)
int2, wavetrain = rectwave(0.003, 0.007, 11)
trianglepulse = trunctTriPulse(interval)
sqarepulse = rectPulse(interval, 0.01)
gauss = gaussPulse(interval, 0.001)


def ploting():
    plt.plot(int2, wavetrain)
    plt.show()
    plt.plot(interval, trianglepulse)
    plt.show()
    plt.plot(interval, sqarepulse)
    plt.show()
    plt.plot(interval, gauss)
    plt.show()


ploting()

rect_rectconvolution = sig.convolve(sqarepulse, sqarepulse) / sum(sqarepulse)
plt.plot(np.linspace(-0.03, 0.03, len(rect_rectconvolution)),
         rect_rectconvolution)
plt.savefig("rectRectPlot.pdf")
plt.show()

rect_triconvolution = sig.convolve(sqarepulse, trianglepulse) / sum(sqarepulse)
plt.plot(np.linspace(-0.03, 0.03, len(rect_triconvolution)),
         rect_triconvolution)
plt.savefig("triRectPlot.pdf")
plt.show()

gauss_trainconvolution = sig.convolve(gauss, wavetrain) / sum(wavetrain)

train_triconvolution = sig.convolve( trianglepulse,wavetrain)  / sum(wavetrain)

plt.plot(np.linspace(-0.06, 0.06, len(gauss_trainconvolution)),
         gauss_trainconvolution)
plt.savefig("gausstraiuplot.pdf")
plt.show()

plt.plot(np.linspace(-0.06, 0.06, len(train_triconvolution)),
         train_triconvolution)
plt.savefig("triTrainplot.pdf")
plt.show()


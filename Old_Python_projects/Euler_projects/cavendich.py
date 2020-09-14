#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from numpy import loadtxt, pi, exp, sin, sum, ones, zeros, std, mean, corrcoef, linspace
from numpy.random import randint
from scipy.optimize import minimize
from matplotlib.pyplot import figure, plot, legend, xlabel, ylabel, show, hist, subplot, title


#   Modell for harmonisk svingning
#   S(t)=S_0 + A*exp(-alpha*t)*sin(omega*t + phi)
def svingeutslag(x, t):
    return x[0] + x[1] * exp(-x[2] * t) * sin(x[3] * t + x[4])


#   Tilpasse modell-parametere for harmonisk svingning til data
def tilpass(S, t, x0):
    kvadr_avvik = lambda x: sum((svingeutslag(x, t) - S) ** 2)
    x1 = minimize(kvadr_avvik, x0, method='Nelder-Mead')
    (S0, A, Alpha, w, phi) = x1.x
    if x1.success:
        return (S0, A, Alpha, w, phi)
    else:
        print('Tilpasning feilet')
        return x0


# Funksjon for Ã¥ estimere usikkerhet i tilpasningsparametre
def usikkerhet_bootstrap(S, t, x0, N):
    res = S - svingeutslag(x0, t)  # Avvik i data fra modell
    nParams = len(x0)  # Antall parametre
    S0 = zeros(N)
    A = zeros(N)
    Alpha = zeros(N)
    w = zeros(N)
    phi = zeros(N)
    for i in range(N):
        index = randint(0, len(S), len(
            S))  # Tabell med et tilfeldig(trukket med tilbakelegging) utvalg av tall mellom0 og antall datapunketer
        t_i = t[index]  # Tider som korresponderer med de tilfeldige datapunktene
        Sre = svingeutslag(x0, t_i) + res[index]  # Simulerte utsving
        (S0[i], A[i], Alpha[i], w[i], phi[i]) = tilpass(Sre, t_i, x0)
    T = 2 * pi / w
    figure('Histogram fra bootstrap simuleringer')
    subplot(231)
    xlabel('S0 ' + r'$(mm)$')
    hist(S0, normed=True)
    subplot(232)
    xlabel('A ' + r'$(mm)$')
    hist(A, normed=True)
    subplot(233)
    xlabel(r'$\alpha\ (1/s)$')
    hist(Alpha, normed=True)
    subplot(234)
    xlabel('T ' + r'$(s)$')
    hist(T)
    subplot(235)
    xlabel(r'$\phi\ (grader)$')
    hist(phi * 180 / pi, normed=True)
    print(
        'Middelverdier:\n<S0>=\t%e mm\n<A>=\t%e mm\n<Alpha>=%e 1/s\n<w>=\t%e (rad)/s\n<T>=\t%e s\n<phi>=\t%e (rad)' % (
        mean(S0), mean(A), mean(Alpha), mean(w), mean(T), mean(phi)))
    dx = (std(S0, ddof=1 + nParams), std(A, ddof=1 + nParams), std(Alpha, ddof=1 + nParams), std(w, ddof=1 + nParams),
          std(phi, ddof=1 + nParams))
    print('Usikkerheter:\n<dS0>=\t%e mm\n<dA>=\t%e mm\n<dAlpha>=%e 1/s\n<dw>=\t%e (rad)/s\n<dphi>=\t%e (rad)' % dx)
    print('Korellasjonskoeeisient mellom S0 og T: %e' % corrcoef(S, t)[0, 1])
    return dx


if __name__ == '__main__':
    data = loadtxt('S1dataEksempel.txt')  # Lese data fra fil
    t = data[:, 0] * 60 + data[:, 1]  # Tid: minutter i fÃ¸rste, og sekunder i andre kolonne
    S = data[:, 2]  # Utsving i tredje kolonne

    # Initielle verdier for tilpasningen
    S0_0 = 460  # Likevektslinje
    A0 = 20  # Amplitude, svingeutslag
    Alpha0 = 0  # Eksponensiell dempingskoeffisient for amplituden
    T0 = 650  # Periode
    phi0 = 0.6  # Fasevinkel
    x0 = [S0_0, A0, Alpha0, 2 * pi / T0, phi0]

    # Tilpasse modell-parametere til data
    x1 = tilpass(S, t, x0)
    (S0, A, Alpha, w, phi) = x1
    T = 2 * pi / w

    print(
        'Tilpassede verdier:\nS0=\t\t%e mm\nA=\t\t%e mm\nAlpha=\t%e 1/s\nw=\t\t%e (rad)/s\nT=\t\t%e s\nphi=\t%e (rad)' % (
        S0, A, Alpha, w, T, phi))

    # Plotte data, tilpasning, likevektslinje, og omhyldningskurver
    figure('Figur 1')
    plot(t, S, 'bx', label='MÃ¥lte data')
    t_plot = linspace(t[0], t[-1], 200)
    plot(t_plot, svingeutslag(x1, t_plot), '-r', label='$S(t)=%f%+f*e^{-%f*t}*\sin(%f*t%+f)$' % (S0, A, Alpha, w, phi))
    plot(t_plot, S0 * ones(len(t_plot)), 'k')  # Likevektslinje
    plot(t_plot, S0 + A * exp(-Alpha * t_plot), '--k')  # Ã˜vre omhyldningskurve
    plot(t_plot, S0 - A * exp(-Alpha * t_plot), '--k')  # Nedre omhyldningskurve
    xlabel('Tid ' + r'$(s)$')
    ylabel('Svingeutslag ' + r'$(mm)$')
    legend(loc='best')

    N_boot = 200  # Antall bootstrap simuleringer
    dx = usikkerhet_bootstrap(S, t, x1, N_boot)
    show()
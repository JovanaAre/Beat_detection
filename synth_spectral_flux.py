# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:52:35 2021

@author: vlado
"""

import numpy as np
import matplotlib.pyplot as plt

def synth_spectral_flux(bpm, dur=10, Fs=100):
    '''
        Generise sinteticku sekvencu impulsa spektralnog fluksa.
        Ulazni argumenti:
            bpm - tempo u BPM
            dur - trajanje u sekundama
            Fs  - frekvencija odmjeravanja u Hercima
    '''

    L = dur * Fs
    x = np.zeros(L)
    print(bpm, Fs)
    N = 60*Fs // bpm
    print(N)
    peaks = np.arange(N, L, N)
    x[peaks] = 1
    
    return x

Fs = 100
dur = 10

t = np.arange(0, dur, 1/Fs)

# Sekvenca impulsa sa konstantnim BPM
x = synth_spectral_flux(100)
plt.figure()
plt.plot(t, x)

# Sekvenca impulsa sa dva razlicita BPM
y = np.concatenate((synth_spectral_flux(100, dur=5), synth_spectral_flux(150, dur=5)))
plt.figure()
plt.plot(t, y)



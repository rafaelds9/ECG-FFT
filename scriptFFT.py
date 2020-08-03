import numpy as np
from matplotlib import pyplot as plt
from scipy.io import loadmat
from scipy.fft import fft, ifft, rfft
from biosppy.signals import ecg


def normalize(signal, amplification = 200): 
    signal = signal/amplification
    normalized = signal/max(signal)

    return normalized

# Constants related to the signal
amplification = 200
samplingRate = 360


# Loading signals

#Normal
normal0 = loadmat('Signals/NormalSinusRhythm/100m (0).mat')
normal1 = loadmat('Signals/NormalSinusRhythm/100m (1).mat')
normal2 = loadmat('Signals/NormalSinusRhythm/100m (2).mat')
normal3 = loadmat('Signals/NormalSinusRhythm/100m (3).mat')

#Atrial Fibrillation
atrialFib0 = loadmat('Signals/AtrialFibrillation/201m (0).mat')
atrialFib1 = loadmat('Signals/AtrialFibrillation/201m (1).mat')
atrialFib2 = loadmat('Signals/AtrialFibrillation/201m (2).mat')
atrialFib3 = loadmat('Signals/AtrialFibrillation/201m (3).mat')



# Normalizing the amplitudes
normal0 = normalize(normal0['val'][0])
normal1 = normalize(normal1['val'][0])
normal2 = normalize(normal2['val'][0])
normal3 = normalize(normal3['val'][0])
atrialFib0 = normalize(atrialFib0['val'][0])
atrialFib1 = normalize(atrialFib1['val'][0])
atrialFib2 = normalize(atrialFib2['val'][0])
atrialFib3 = normalize(atrialFib3['val'][0])

#Every class is stored in its own array
normal = np.stack((normal0,normal1,normal2, normal3))
atrialFib = np.stack((atrialFib0,atrialFib1,atrialFib2, atrialFib3))


# Shows a summary of the signal
#normalSummary = ecg.ecg(signal=normal0, sampling_rate=samplingRate, show=True)
#atrailFibSummary = ecg.ecg(signal=atrialFib0, sampling_rate=samplingRate, show=True)


#Frequency axis
xf = np.linspace(0.0, 1.0/(2.0*1/samplingRate), 10*samplingRate//2)

for itClass in range(2):
    
    if (itClass == 0):
        fig0 = plt.figure(figsize=(19.2,9.91)) #19.2,9.91
    else:
        fig1 = plt.figure(figsize=(19.2,9.91)) #19.2,9.91

    plt.rcParams.update({'font.size': 16})

    for itSignal in range(4):
        if (itClass == 0):
            fft = rfft(normal[0:][itSignal])
        else:
            fft = rfft(atrialFib[0:][itSignal])
    
        ax=plt.subplot(2, 2, itSignal+1)  
        plt.plot(xf, 2.0/10*samplingRate * np.abs(fft[0:10*samplingRate//2]))
        plt.grid()
        ax.set_ylim(-100, 1500)

#Ver o eixo das frequencias
plt.show()


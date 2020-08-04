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

#Hard coded for these signals (10s interval with 3600 samples)
xt = np.linspace(0.0, 10.0, 10*samplingRate)

for itClass in range(2):

    plt.rcParams.update({'font.size': 16})

    if (itClass == 0):
        fig0 = plt.figure(figsize=(19.2,9.91))
        fig0.suptitle("Time Domain - Normal")
    else:
        fig1 = plt.figure(figsize=(19.2,9.91))
        fig1.suptitle("Time Domain - Atrial Fibrillation")

    

    for itSignal in range(4):

        ax=plt.subplot(2, 2, itSignal+1)  

        if (itClass == 0):
            plt.title('Signal '+str(itSignal+1))
            plt.plot(xt, normal[0:][itSignal])
        else:

            plt.title('Signal '+str(itSignal+1))
            plt.plot(xt, atrialFib[0:][itSignal])
        
        plt.grid()
        #ax.set_ylim(-1, 22)
        ax.set_xlim(-0.03, 3)

plt.tight_layout
plt.show()


#Frequency axis
# Frequency values from 0 to the Sampling rate/2 
# (10*Fs//2 = 1800 values)
# The number of samples is halved because the input is a real signal
# i.e only positive frequencies values are used
xf = np.linspace(0.0, 1.0/(2.0*1/samplingRate), 10*samplingRate//2)


for itClass in range(2):

    plt.rcParams.update({'font.size': 16})

    if (itClass == 0):
        fig0 = plt.figure(figsize=(19.2,9.91))
        fig0.suptitle("Frequency Domain - Normal")
    else:
        fig1 = plt.figure(figsize=(19.2,9.91))
        fig1.suptitle("Frequency Domain - Atrial Fibrillation")

    

    for itSignal in range(4):

        ax=plt.subplot(2, 2, itSignal+1)  

        if (itClass == 0):

            # Negative frequencies are ignored
            # If x = signal before FFT and y = FFT(x) and k index of x and y
            # Then t = k*T/N = time value of x[k] nad f = k/N = frequency of y[k]
            fft = rfft(normal[0:][itSignal])
            plt.title('Signal '+str(itSignal+1))
            print("DC - Normal No.",itSignal+1, "=", np.round(np.abs(fft[0]),3))
        else:
             
            fft = rfft(atrialFib[0:][itSignal])
            plt.title('Signal '+str(itSignal+1))
            print("DC - Atrial Fib No.",itSignal+1, "=", np.round(np.abs(fft[0]),3))


        plt.plot(xf, np.abs(fft[0:10*samplingRate//2]))
        plt.grid()
        ax.set_ylim(-1, 22)
        ax.set_xlim(-10, 1.0/(2.0*1/samplingRate))

plt.tight_layout
plt.show()


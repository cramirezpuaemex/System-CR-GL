from scipy.signal import butter, lfilter 
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import math

def butter_bandpass(lowcut, highcut, fs, order=5): 
    nyq = 0.5 * fs 
    low = lowcut/nyq 
    high = highcut/nyq 
    b, a = butter(order, [low, high], btype='band') 
    return b, a 


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5): 
    b, a = butter_bandpass(lowcut, highcut, fs, order=order) 
    y = lfilter(b, a, data) 
    return y 

def extraeuncanal(sonido):
    canales=sonido.shape
    cuantos=len(canales)
    canal = 0
    if (cuantos==1): # Monofonico
        uncanal=sonido[:]
    if (cuantos>=2): # Estereo
        uncanal=sonido[:,canal]
    return(uncanal)



if __name__ == "__main__": 
    import numpy as np 
    import matplotlib.pyplot as plt 
    from scipy.signal import freqz 

    # Sample rate and desired cutoff frequencies (in Hz). 
    fs = 44100.0 
    lowcut = 350.0 
    highcut = 3500.0 

    print '**************lectura de archivos***************'
    archivo01 = 'tu_falta.wav'
    archivo02 = 'tu_falta_frase_5.wav'
    muestreo, sonido = waves.read(archivo01)
    x = extraeuncanal(sonido)
    f0 = 600.0 
    muestreo, sonido = waves.read(archivo02)
    y = extraeuncanal(sonido)


    plt.figure(2) 
    plt.clf() 
    plt.plot( x, label='Noisy signal') 

    senal01 = butter_bandpass_filter(x, lowcut, highcut, fs, order=4) 
    plt.plot( senal01, label='Filtered signal (%g Hz)' % f0) 
    plt.xlabel('time (seconds)') 
    #plt.hlines([-a, a], 0, T, linestyles='--') 
    plt.grid(True) 
    plt.axis('tight') 
    plt.legend(loc='upper left') 


    plt.figure(3) 
    plt.clf() 
    plt.plot( y, label='Noisy signal') 

    senal02 = butter_bandpass_filter(y, lowcut, highcut, fs, order=4) 
    plt.plot( senal02, label='Filtered signal (%g Hz)' % f0) 
    plt.xlabel('time (seconds)') 
    #plt.hlines([-a, a], 0, T, linestyles='--') 
    plt.grid(True) 
    plt.axis('tight') 
    plt.legend(loc='upper left') 


    print '*************procedimiento**********************'
    # PROCEDIMIENTO
    tamano01 = len(senal01)
    tamano02 = len(senal02)
    
    # Normaliza las senales
    amplitud = np.max(senal01)
    #senal01 = senal01/amplitud
    #senal02 = senal02/amplitud
    if len(senal01)>=len(senal02):
        ex=math.log(len(senal01),2)
        lon_mx=len(senal01)
    else:
        ex=math.log(len(senal02),2)
    lon_mx=len(senal02)
    
    
    ex=math.ceil(ex)
    print 'exponente', ex
    N=len(senal01)+len(senal02)
    f0 = np.fft.fft(senal01, 2**int(ex))
    f1 = np.fft.fft(senal02, 2**int(ex))
    #f0 = np.fft.fft(senal01, N)
    #f1 = np.fft.fft(senal02, N)
    c=[]
    
    for i in range(len(f0)):
        c.append(f1[i].conjugate()*f0[i])
    #c=np.asarray(c)


    print '**********************Graficas*********************'
    R_xy = (np.fft.ifft(c))
    
    #for i in range(len(senal01)):
        #n1=n1+(abs(senal02[i])*abs(senal02[i]))
    print '**********************inversa*********************'
        
    
    #[R_xy[i]=R_xy[i]/n for i in range(len(R_xy)) ]
    #n=len(senal02)+len(senal01)
    R_xy=np.asarray(R_xy)
    R_xy=abs(R_xy)
    
    L2 = [n**2 for n in senal02]
    
    n=sum(L2)
   
    for i in range(len(R_xy)):
        R_xy[i]=R_xy[i]/n
    
    
    plt.figure(4) 
    plt.clf() 
    plt.plot(R_xy)
    R_xy=R_xy.tolist()
    
    maximo=max(R_xy)
    indice=R_xy.index(maximo)
    print 'valos maximo de correlacion', maximo
    print 'indice donde encuentra la maxima correlacion', indice


    plt.show()
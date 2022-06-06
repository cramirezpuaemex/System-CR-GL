# analiza correlacion entre dos muestras
#formatos SAC

#====================Librerias===================================================
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import math
import obspy
from scipy.signal import butter, lfilter 
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
#==========================Lectura de archivos===================================
path1= "/home/carlos/Dropbox/Catalogo_2006_2007/2006/027.11.32/027.11.32.ALPI.HHZ.SAC"
#path1='/home/carlos/Escritorio/CODEX_2006/036/ZA.ZAPO..HHZ.M.2006.036.000000.SAC'
#path1= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/2006.036.10.57.ZA.COMA.HHZ.SAC"
st1=obspy.read(path1)
senal01=st1[0].data

path2= "/home/carlos/Dropbox/Catalogo_2006_2007/2006/028.13.45/028.13.45.ALPI.HHZ.SAC"

st1=obspy.read(path2)
senal02=st1[0].data
print '*************procedimiento**********************'
# PROCEDIMIENTO
tamano01 = len(senal01)
tamano02 = len(senal02)

#senal01 = butter_bandpass_filter(x, lowcut, highcut, fs, order=4) 
#senal02 = butter_bandpass_filter(y, lowcut, highcut, fs, order=3) 

print 'tamano01', tamano01, 'tamano02', tamano02
# Normaliza las senales





if len(senal01)>=len(senal02):
	ex=math.log(len(senal01),2)
	lon_mx=len(senal01)

	
else:
	ex=math.log(len(senal02),2)
	lon_mx=len(senal02)

print ' longitud maxima', lon_mx

ex=math.ceil(ex)
print 'exponente', ex



f0 = np.fft.fft(senal01, 2**int(ex))
f1 = np.fft.fft(senal02, 2**int(ex))

c=[]

print len(abs(f1))
print len(abs(f0))
for i in range(int(2**ex)):
	c.append(f1[i].conjugate()*f0[i])
#c=np.asarray(c)

print '**********************Inversa*********************'
R_xy = (np.fft.ifft(c))

#for i in range(len(senal01)):
	#n1=n1+(abs(senal02[i])*abs(senal02[i]))
print '**********************Graficas*********************'


#[R_xy[i]=R_xy[i]/n for i in range(len(R_xy)) ]
#n=len(senal02)+len(senal01)
R_xy=np.asarray(R_xy)
R_xy=abs(R_xy)
t0=maximo=max(R_xy)
L2 = [(p)**2 for p in senal01]
n=sum(L2)
#n=np.linalg.norm(senal02)
L1 = [(p1)**2 for p1 in senal02]
m=sum(L1)
#m=np.linalg.norm(senal01)
print 'm', m, 'n', n


for i in range(len(R_xy)):
	R_xy[i]=R_xy[i]/n
plt.figure(3)
plt.subplot(3,1,1)
plt.plot(senal01)
plt.subplot(3,1,2)
plt.plot(R_xy)
plt.subplot(3,1,3)
plt.plot(senal02)
R_xy=R_xy.tolist()

maximo=max(R_xy)
indice=R_xy.index(maximo)

print 'valos maximo de correlacion', maximo
print 'indice donde encuentra la maxima correlacion', indice	


plt.show()
	
	
print 'fin'
	

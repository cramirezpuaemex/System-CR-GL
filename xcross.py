import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves



archivo = 'tu_falta.wav'
muestreo, sonido = waves.read(archivo)

print 'fs', muestreo
tamano = np.shape(sonido)
muestras = tamano[0]
m = len(tamano)
canales = 1  # monofonico
if (m>1):  # estereo
    canales = tamano[1]
# experimento con un canal
if (canales>1):
    canal = 0
    uncanal = sonido[:,canal] 
else:
    uncanal = sonido


a = int(1*muestreo)
b = int(m*muestreo)



amplitud = np.max(uncanal)
senal01 = uncanal/amplitud
plt.plot(uncanal)
plt.xlabel('tiempo (s)')
plt.ylabel('Amplitud')
plt.show()
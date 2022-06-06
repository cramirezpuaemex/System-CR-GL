#====================Librerias===================================================
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import math
import obspy
from scipy.signal import butter, lfilter

from time import time 
#==========================Lectura de archivos===================================
#path1= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.038.00.34/2006.038.00.34.ZA.COMA.HHZ.SAC"
path1='/home/carlos/Escritorio/CODEX_2006/036/ZA.MAZE..HHZ.M.2006.036.000000.SAC'
#path1="/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/P_Windows/2006.036.10.57.ZA.MAZE.HHZ.SAC"
st1=obspy.read(path1)
senal01=st1[0].data

aux=[]
for ii in range(len(senal01)):
	if ii % 2 == 0:
		aux.append(senal01[ii])
senal01=aux


path2= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/P_Windows/2006.036.10.57.ZA.MAZE.HHZ.SAC"


st1=obspy.read(path2)
senal02=st1[0].data


aux=[]
for ii in range(len(senal02)):
	if ii % 2 == 0:
		aux.append(senal02[ii])
senal02=aux
aux=[]


path3= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/2006.036.10.57.ZA.MAZE.HHZ.SAC"
st1=obspy.read(path3)
senal03=st1[0].data
for ii in range(len(senal03)):
	if ii % 2 == 0:
		aux.append(senal03[ii])
senal03=aux
aux=[]
tiempo_inicial = time()
#print '*************procedimiento**********************'
# PROCEDIMIENTO
tamano01 = len(senal01)
tamano02 = len(senal02)


#print 'tamano01', tamano01, 'tamano02', tamano02
# Normaliza las senales

amplitud = np.max(senal01)

valor=20

l=tamano01/valor
l=int(math.floor(l))



if l>=len(senal02):
	ex=math.log(l,2)
	lon_mx=len(senal01)

	
else:
	ex=math.log(len(senal02),2)
	lon_mx=len(senal02)

#print ' longitud maxima', lon_mx

ex=math.floor(ex)
#print 'exponente', ex
#print 'l', l
v_max=[]
v_indice=[]
for p in range(valor):
	aux=[]
	#print '==== valor de P ===', p
	if p==0:
		parte=senal01[0:l]
	else:
		parte=senal01[l*p: l*(p+1)]

	f0 = np.fft.fft(parte, 2**int(ex))
	f1 = np.fft.fft(senal02, 2**int(ex))
	
	c=[]
	
	#print len(abs(f1))
	#print len(abs(f0))

	for i in range(len(f0)):
		c.append(f1[i].conjugate()*f0[i])
	#c=np.asarray(c)
	
	
	#print '**********************Graficas*********************'
	R_xy = (np.fft.ifft(c))
	
	#for i in range(len(senal01)):
		#n1=n1+(abs(senal02[i])*abs(senal02[i]))
	#print '**********************inversa*********************'
	
	
	#[R_xy[i]=R_xy[i]/n for i in range(len(R_xy)) ]
	#n=len(senal02)+len(senal01)
	R_xy=np.asarray(R_xy)
	R_xy=abs(R_xy)
	
	L2 = [n2**2 for n2 in senal02]
	n=sum(L2)

	L1 = [n1**2 for n1 in parte]
	m=sum(L1)


		


	#print 'm', m, 'n', n
	

	for i in range(len(R_xy)):

		R_xy[i]=R_xy[i]/n
	'''
	plt.figure(p+1)
	plt.plot(R_xy)
	'''

	R_xy=R_xy.tolist()
	
	maximo=max(R_xy)
	indice=R_xy.index(maximo)
	if maximo <1.003:
		v_max.append(maximo)
		v_indice.append(indice+(p*l))
	
	
	#print 'valos maximo de correlacion', maximo
	#print 'indice donde encuentra la maxima correlacion', indice+(p*l)	

tiempo_final = time() 
 
tiempo_ejecucion = tiempo_final - tiempo_inicial

print 'tiempo de ejecucion: ', tiempo_ejecucion
cont=1
for i in range(len(v_max)):

	#print 'valor maximo es: ', v_max[i], 'en la posicion: ', v_indice[i]

	if v_max[i] >=0.85 :
		#maximo=max(v_max)
		#indice=v_max.index(maximo)
		#indice=v_indice[indice]
		print 'valores maximo de correlacion', v_max[i]
		print 'indice donde encuentra la maxima correlacion', v_indice[i]
			
		


		plt.figure(cont)
		plt.subplot(2,1,1)
		plt.plot(senal03)
		plt.subplot(2,1,2)
		f=[senal01[i] for i in range(v_indice[i], v_indice[i]+len(senal03))]
		plt.plot(f)
		cont=cont+1
'''
plt.subplot(2,1,1)
plt.plot(senal02)
plt.subplot(2,1,2)
f=[senal01[i] for i in range(indice, indice+len(senal02))]	
plt.plot(f)
plt.show()
'''
plt.show()	
print 'fin'

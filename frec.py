from obspy import read
from scipy import fft, arange
from pylab import plot, show, title, xlabel, ylabel, subplot
import numpy as np
import subprocess
import glob
#path1='/home/carlos/Escritorio/Resultados/2006/100.11.10/2006.100.11.10.ZA.JANU.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/187.20.36/2006.187.20.36.ZA.JANU.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/36.10.57/2006.02.05.10.57.39.03.COMA.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/27.11.32/2006.01.27.11.31.49.27.COMA.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/31.09.19/2006.01.31.09.19.04.16.ALPI.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/92.18.48/2006.092.18.48.ZA.ALPI.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/73.23.33/2006.03.14.23.33.00.26.HIGA.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/148.07.23/2006.05.28.07.23.59.64.ESPN.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/102.17.20/2006.102.17.20.ZA.PERC.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/134.03.49/2006.05.14.03.49.29.48.OLOT.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/121.19.38/2006.05.01.19.38.38.00.SANM.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/113.10.39/2006.04.23.10.39.58.41.PAVE.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/110.03.28/2006.04.20.03.28.10.10.SNID.HHZ.SAC'
#path1='/home/carlos/Escritorio/Resultados/2006/93.17.04/2006.093.17.04.ZA.MAZE.HHZ.SAC'
path1='/home/carlos/Escritorio/Resultados/2006/64.02.54/2006.03.05.02.55.04.87.HIGA.HHZ.SAC'
path2='/home/carlos/Escritorio/Resultados/Prueba.SAC'
st = read(path1)

y=st[0].data
n = len(y) # longitud de la senal
Y = fft(y)
Y = Y[range(n/2)]

c=abs(Y)
np_array = c.tolist()
a=max(c)
b=(np_array.index(a))/100


print 'b= ', b
'''
subplot(2,1,1)

plot(y)

xlabel('Tiempo')

ylabel('Amplitud')

subplot(2,1,2)

#Se llama a la funcion con la senal y la rata de muestreo

plot(c)
show()
'''
if b>11:
	b1=b-10
	b2=b+10
else:
	b1=b
	b2=b+10




p = subprocess.Popen(['sac'],
                     		stdout = subprocess.PIPE,
                     		stdin  = subprocess.PIPE,
                     		stderr = subprocess.STDOUT )

s = "echo on\n"
line1='read '+path1+'\n'
line2='BANDPASS NPOLES 4 CORNER '+str(b1)+' '+str(b2)+'\n'
line3='write '+path2+'\n'
line4='read '+path2+'\n'
line5='apk\n'


s+=line1
s+=line2
s+=line3
s+=line4
s+=line5
 
s += "quit()\n"


out = p.communicate( s )
fase=out[0][339:363]

print out
print 'fase', fase



st1 = read(path2)
x=st1[0].data


n = len(x) # longitud de la senal
Y = fft(x)
Y = Y[range(n/2)]

c=abs(Y)
d=max(c)
e=max(x)






aux=[]
con =-1
a=0
b=0
bandera=0
if e <= 90:
	limite=10
if e >90 and e <=150:
	limite=20
if e >150 and e <=1000:
	limite =100
if e >1000 and e <10000:
	limite=1000
while con < len(x):
	
	con+=1
	for con in range(con, con+5):
		if con <len(x):
			if x[con] > limite or x[con] < -limite:
				print con, 'valor ', x[con]
				if a==0:
					print 'a ', a
					a=con
				bandera=0
			else:
				bandera+=1
				print con, 'checar', bandera

				if bandera>=2200 and a!=0 and con > a and b==0:
					b=con
				


	


if b==0:
	b=len(x)
print 'a', a
print 'b', b
m=b-a
#r=(aux/100)*2
print 'm', m
print len(aux)
print len(x)



print 'd', d
print 'e', e
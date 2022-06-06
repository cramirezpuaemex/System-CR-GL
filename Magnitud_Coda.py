from tkinter import filedialog
from Tkinter import *
import tkFileDialog
import subprocess
import glob
from Tkinter import Tk
import os
from os import remove
import os.path
import math
from obspy import read
from scipy import fft, arange
from pylab import plot, show, title, xlabel, ylabel, subplot
import numpy as np
from Phases import *
from formato_z import *
from formato_NE import *
from Rutas_Dir import *
from tkinter import messagebox
from Promedio_Magnitud import *
class Magnitud_Coda():

	def Take_input(self):

		self.INPUT = self.inputtxt.get("1.0", "end-1c")
		print(self.INPUT)
		a=0
		if self.INPUT!="":
			self.root.destroy()
			print "*****"
			self.Work(self.INPUT)
			#print "INPUT", self.INPUT
	



	def Input_data(self):

		self.root = Tk()
		self.root.geometry("300x100")
		self.root.title(" Input name to identifier")
		#INPUT=""     
		self.inputtxt = Text(self.root, height = 2,
		                width = 35,
		                bg = "light yellow")
		 
		self.Display = Button(self.root, height = 2,
		                 width = 20,
		                 text ="Start",
		                 command = lambda:self.Take_input())
		 

		self.inputtxt.pack()
		self.Display.pack()
		mainloop()




	def main(self):
		print "inicia"

		self.Input_data()
		
	
	def Work(self, year_new):
		print "Inicia proceso work, con id: ", year_new

		Tk().withdraw()
		#file=filedialog.askdirectory()
		#file=tkFileDialog.askdirectory()
		inicia_dir=Rutas_Dir()
		Tipo="Path del catalogo de eventos en formato SAC"
		
		file=inicia_dir.pathfile(Tipo)
		archivos=os.listdir(file)
		archivos=sorted(archivos)
		directorios=[]
		path=[]
		for i in range(len(archivos)):
			archivos[i]= file+'/'+archivos[i]
			if os.path.isdir(archivos[i])==True:
				temp=os.listdir(archivos[i])
				temp=sorted(temp)
				for j in range(len(temp)):
					if temp[j].find('HHZ')!=-1:
						path.append(archivos[i]+'/'+temp[j])

		
		Tipo="Path salve files"
		print"continua"
		guardar_archivos=inicia_dir.pathfile(Tipo)

		
		for i in path:
			print 'path', i
			guardar_archivosf=i[0:len(i)-23]


			print i
			fecha_archivos=guardar_archivosf[len(guardar_archivosf)-9:len(guardar_archivosf)]
			print "fecha archivos", fecha_archivos
			guardar_archivosf=guardar_archivos[0:len(guardar_archivosf)-9]
			#Tipo="Path salve files"
			#guardar_archivos=inicia_dir.pathfile(Tipo)
			#guardar_archivos='/home/carlos/Dropbox/2006a/'
			path1=i
			path2=guardar_archivos+'/Prueba.SAC'
			print "path2", path2
			st = read(path1)

			y=st[0].data
			n = len(y) # longitud de la senal
			Y = fft(y)
			Y = Y[range(n/2)]

			c=abs(Y)
			np_array = c.tolist()
			a=max(c)
			b=(np_array.index(a))/100


			#print 'b= ', b

			if b>11:
				b1=b-10
				b2=b+10
			else:
				b1=b
				b2=b+10

			if b1==0:
				b1=15
				b2=30
			p = subprocess.Popen(['sac'],
                     					stdout = subprocess.PIPE,
                     					stdin  = subprocess.PIPE,
                     					stderr = subprocess.STDOUT )

			s = "echo on\n"
			line1='read '+path1+'\n'
			line2='BANDPASS NPOLES 4 CORNER '+str(b1)+' '+str(b2)+'\n'
			line3='write '+path2+'\n'


			s+=line1
			s+=line2
			s+=line3

 
			s += "quit()\n"


			out = p.communicate( s )
			#print out[0]

			


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
							#print con, 'valor ', x[con]
							if a==0:
								#print 'a ', a
								a=con
							bandera=0
						else:
							bandera+=1
							#print con, 'checar', bandera

							if bandera>=2200 and a!=0 and con > a and b==0:
								b=con
				


	


			if b==0:
				b=len(x)
			print 'a', a
			print 'b', b
			m=(b-a)/100
			#r=(aux/100)*2
			print 'm', m
			if m < 1:
				m=len(x)/100

			Mc=(1.87*(math.log10(m)))-0.86
			#print Mc




			print 'Comienza a guardar archivos magnitud_'
			path_salve_magnitud=guardar_archivos+'/Magnitud_'+year_new+'/'+year_new+'/'
			path_salve_prom=guardar_archivos+'/Magnitud_'+year_new+'/'
			
			#path_salve=guardar_archivos+'/_'+year_new+'/'+year_new+'/'
			print "path_salve", path_salve_magnitud
			if not os.path.exists(path_salve_magnitud):
				os.makedirs(path_salve_magnitud)
			fo = open(path_salve_magnitud+'/'+'magnitud_'+fecha_archivos +'.txt', 'a')
			#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')

			fo.write('Tiempo (seg): '+ str(m)+ '\t Magnitud: '+str(Mc))
			fo.write('\n')


		

			fo.close()
			

			#***************************Fases**********************************


			inicio_path=Phases()
			phase=inicio_path.main(i)

			
			
			index_phase=phase.find('apk')
			inicio_z=formato_z()
			inicio_ne=formato_NE()
			fase_z=inicio_z.main(phase, index_phase)
			#print fase_z
			dia_phase=[]
			if fase_z != -1:
				nombre_n = i.replace("HHZ", "HHN")
				nombre_e = i.replace("HHZ", "HHE")
				phase_n=inicio_path.main(nombre_n)
				phase_e=inicio_path.main(nombre_e)
				fase_ne=inicio_ne.main(phase_n, phase_e)
				fase_n=fase_ne[0]
				fase_e=fase_ne[1]
				print'Datos finales\n', fase_z, ' ', fase_n, ' ', fase_e

				print 'Comienza a guardar archivos pahses'
				path_salve=guardar_archivos+'/fases_'+year_new+'/'+year_new+'/'
				print "path_salve", path_salve
				if not os.path.exists(path_salve):
					os.makedirs(path_salve)
				fo = open(path_salve+fecha_archivos +'.txt', 'a')
				#fo = open(path_salve)
				#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')

				#fo.write(fase_z+'\t '+fase_n+'\t '+fase_e)
				if fase_n != '0':
					#fo.write(fase_z)
					fo.write(fase_z+'       '+fase_n+'SI 0')
				else:
					fo.write(fase_z)
				dia_phase.append(fase_z)
				fo.write('\n')
				fo.close()


				#fo = open(guardar_archivos+'phases_full/'+year_new+'/'+fecha_archivos +'.txt', 'a')
					#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')

				#fo.write(fase_z+'\t '+fase_n+'\t '+fase_e)
				#fo.write(fase_z)
				#fo.write('\n')
				#fo.close()
		remove(path2)
		inicio_prom=Promedio_Magnitud()
		inicio_prom.main(path_salve_prom, year_new)







#inicia=Magnitud()
#inicia.main()									
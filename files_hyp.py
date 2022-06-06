from tkinter import filedialog
from Tkinter import *
import tkFileDialog
import subprocess
import glob
from Tkinter import Tk
import os
import os.path



class files_hyp():
	def main(self):
		Tk().withdraw()
		#file=filedialog.askdirectory()
		file=tkFileDialog.askdirectory()
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
					if temp[j].find('.txt')!=-1:
						path.append(archivos[i]+'/'+temp[j])


		for i in path:
			print i
			f = open(i,"r")
			self.arreglo= []
			contLin=0
			while True:
				linea = f.readline()
				if linea:
					datos = linea.split('\n')
					datos = datos[0].split(',')

					self.arreglo.append(datos[0])

				else:
					break	

			
			if len(self.arreglo)>3:


				fo = open('/home/carlos/Escritorio/hyp.txt', 'a')
					#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')
				for a in self.arreglo:

					fo.write(a)
					fo.write('\n')
				fo.write('\n')
				fo.close()




inicia= files_hyp()
inicia.main()
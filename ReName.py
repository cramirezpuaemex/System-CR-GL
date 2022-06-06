from Tkinter import Tk
import os
import os.path
from tkinter import filedialog
from Tkinter import *
import tkFileDialog
import subprocess
import glob

class ReName():
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
					if temp[j].find('SAC')!=-1:
						path.append(archivos[i]+'/'+temp[j])

		

		year_new='2007'

		for i in path:
			pos_year=i.find(year_new)
			pos_dot=i.find('.')
			print i
			
			dia=i[pos_year+5:pos_dot]
			print 'dia', dia
			if len(dia)<=2:
				dia='0'+dia
			#print 'dia: ', dia
			ruta= i[0:pos_year+5]+dia+i[pos_dot:pos_dot+7]
			estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']
			#ext=i.find('.ZA.')
			nombre=ruta[len(ruta)-10:len(ruta)-1]
			print 'nombre ', nombre
			carpeta='/home/carlos/Escritorio/'+year_new+'/'+nombre

			for ext in estaciones:

				if i.find(ext) != -1:
				
					path2=carpeta+'/'+nombre+'.'+ext+'.'+i[len(i)-7:len(i)]
					break

				#else:
				
					#path2=carpeta+'/'+nombre+'.ZA.'+i[len(i)-12:len(i)]
			
			#print 'path2', path2

			

			
			#print path2
			if len(path2)!=61:
				print 'error', len(path2)

			
			if not os.path.exists(carpeta):
					print 'crea carpeta en', carpeta
					os.makedirs(carpeta)
			else:
				print 'ya existe la carpeta', carpeta

			p = subprocess.Popen(['sac'],
                     					stdout = subprocess.PIPE,
                     					stdin  = subprocess.PIPE,
                     					stderr = subprocess.STDOUT )

			s = "echo on\n"
			line1='read '+i+'\n'
			line2='write '+path2+'\n'



			s+=line1
			s+=line2

 
			s += "quit()\n"


			out = p.communicate( s )
			

inicia=ReName()
inicia.main()
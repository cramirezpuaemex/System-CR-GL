from tkinter import filedialog
from Tkinter import *
import tkFileDialog

from Tkinter import Tk
import os
import os.path
class OpenFile_multiple():
	def main(self, tipo):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		file=tkFileDialog.askdirectory(initialdir = "/home",title = tipo)
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

		return path
		#for i in path:
			#print i

		#print 'numero de archivos', len(path)

#inicia=OpenFile_multiple()
#inicia.main()
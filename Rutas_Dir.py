from Tkinter import Tk
import tkFileDialog
from tkFileDialog import askdirectory
from tkinter import filedialog
import os
import os.path
class Rutas_Dir():
	filename = ""
	def pathfile(self, Tipo):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		#file=tkFileDialog.askdirectory(initialdir = "/home",title = Tipo)
		#print file

		root4 = Tk()
		file =  askdirectory(initialdir = "/home",title = Tipo)
		root4.destroy()
		print "file met Rutas_Dirs ", file
		return file

	

#inicio=Rutas_Dir()
#Tipo="Selecciona Directorio para guardar archivo "
#archivos=inicio.pathfile(Tipo)
#print archivos
#archivos=sorted(archivos)



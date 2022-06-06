from Tkinter import *
import tkFileDialog 

from ScrolledText import *

class Guardar_datos():
	def guardar_directorio(self, Tipo):

		rutadeldirectorio=tkFileDialog.askdirectory(title=Tipo)
		return rutadeldirectorio



#inicia=Guardar_datos()
#ruta=inicia.guardar_directorio()

#print ruta
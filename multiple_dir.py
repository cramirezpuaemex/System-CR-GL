from tkinter import *
from Rutas_Dir import *
import tkFileDialog
import tkinter as tk

class multiple_dir():

	def main(self, b):
		if b==0:
			self.a=[]
			self.pregunta()
		else:
			print self.a
			return self.a

	def Pregunta_yes(self):
	    inicio=Rutas_Dir()
	    Tipo="ji"
	    #Tk().withdraw()
	    file=inicio.pathfile(Tipo)
	    #borrar()
	    self.a.append(file)


	def Pregunta_not(self):
	    self.root3.destroy()
	    b=1
	    self.main(b)


	def pregunta(self):

		a=[]
		self.root3 = Tk()
		self.root3.config(bd=25)
		T = Text(self.root3,  height = 1, width = 30)

		Fact = """Select directory with files"""

		T.pack()
		Button(self.root3, text="yes", command=self.Pregunta_yes).pack(side="left")
		#Button(root, text="Resta", command=resta).pack(side="left")
		Button(self.root3, text="Not", command=self.Pregunta_not).pack(side="right")

		T.insert(tk.END, Fact)
		self.root3.mainloop()

inicio=multiple_dir()
b=0
inicio.main(b)
print a

#Desarrollado por Carlos Ramirez Pina
from Tkinter import *
import tkMessageBox

from Datos_correlacion import *
from file_hypodd import *
#from hyp_path import *
from Magnitud_Coda import *
#from Promedio_Magnitud import *
import sys
from option_multiple import *



		


class Principal:
	def FuncionClass(self):
		print  ":)"

	def Salir(self):
		sys.exit(0)
		##print  texto



	def Correlacion_multiple(self):
		print ':)'
		self.root0.destroy()	
		Inicia_D_C=Datos_correlacion()
		Inicia_D_C.main()
		self.MenuPrincipal()
	def Localizacion(self):
		print ':) **'
		#inicio_opc_mult=option_multiple()
		#inicio_opc_mult.MenuPrincipal_Localizacion()
		inicio_opc=option_multiple()
		inicio_opc.MenuPrincipal_localizacion()
		#messagebox.showinfo(message="process completed successfully", title="Message")
		self.MenuPrincipal()
	def Re_localizacion(self):
		print ':) ****'
		self.root0.destroy()	
		inicio=file_hypodd()
		inicio.main()

	def Magnitud_Coda(self):
		print ':)  *******'
		self.root0.destroy()	
		inicia=Magnitud_Coda()
		inicia.main()
		self.MenuPrincipal()
		#Realiza el promedio por magnitud
		#inicia= Promedio_Magnitud()
		#inicia.main()

	def Aproximar(self):
		print ':) **********'	
	def Clasificar(self):
		print ':) *************'



	def MenuPrincipal(self):
		self.root0 = Tk()
		self.root0.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root0.title(" Seismology system CR_GL")
		#INPUT=""     

		 
		self.Display = Button(self.root0, height = 2,
		                 width = 40,
		                 text ="Create Catalogs events seismic",
		                 command = lambda:self.Correlacion_multiple())

		self.Display2 = Button(self.root0, height = 2,
		                 width = 40,
		                 text ="Using localization",
		                 command = lambda:self.Localizacion())
		self.Display3 = Button(self.root0, height = 2,
		                 width = 40,
		                 text ="Using Re localization",
		                 command = lambda:self.Re_localizacion())	
		self.Display4 = Button(self.root0, height = 2,
		                 width = 40,
		                 text ="Coda Magnitude",
		                 command = lambda:self.Magnitud_Coda())			                 	

		self.Display8 = Button(self.root0, height = 2,
		                 width = 20,
		                 text ="Quit",
		                 command = lambda:self.Salir())

		#self.inputtxt.pack()
		self.Display.pack()
		self.Display4.pack()
		self.Display2.pack()
		self.Display3.pack()
		
		self.Display8.pack()
		mainloop()

	# def MenuPrincipal(self):
	# 	v0=Tk()
	# 	v0.minsize(512,265)
	# 	v0.title('Seismology system CR_GL')
	# 	menu1 = Menu(v0)
	# 	v0.config(menu=menu1)

	
	# 	menu1_1 = Menu(menu1, tearoff=0)
	# 	menu1.add_cascade(label="->Opciones<-", menu=menu1_1)
	# 	menu1_1_1 = Menu(menu1_1, tearoff=0)
	# 	menu1_1_2 = Menu(menu1_1, tearoff=0)
	# 	menu1_1_3 = Menu(menu1_1, tearoff=0)
	# 	menu1_1_4 = Menu(menu1_1, tearoff=0)
	# 	menu1_1.add_command(label="Crear catalogo de eventos", command=self.Correlacion_multiple)
	# 	menu1_1.add_command(label="Localizacion", command=self.Localizacion)	
	# 	#menu1_1_4.add_command(label="Clasificar", command=self.ValidacionClasificar)
	# 	#menu1_1_4.add_command(label="Aproximar", command=self.ValidacionAproximar)
	# 	menu1_1.add_command(label="Re_localizacion", command=self.Re_localizacion)
	# 	#menu1_1_1.add_command(label="Autocorrelacion_multiple",command=self.Autocorrelacion_multiple)
	# 	#menu1_1_1.add_command(label="Test",command=self.TestClasifica)
	# 	menu1_1.add_command(label="Magnitud Coda", command=self.Magnitud_Coda)
	# 	#menu1_1.add_command(label="Aproximar", command=self.Aproximar)
	# 	#menu1_1.add_command(label="Clasificar", command=self.Clasificar)
	# 	#menu1_1_2.add_command(label="Entrenamiento",command=self.EntrenarAproximar)
	# 	#menu1_1_2.add_command(label="Test",command=self.TestAproximar)
	# 	menu1_1.add_command(label="Salir", command=self.Salir)
		
		
	# 	#CREDITOS
	# 	etiqueta = Label(v0,text="Elaborado por: CARLOS RAMIREZ PINA")
	# 	etiqueta.grid(column=0, row=20) 
	# 	#tkMessageBox.showinfo("Bienvenido", "En este sistema en el menu OPCIONES podra realizar las siguientes actividades:\n\n -> Normalizar un conjunto de datos\n\n -> Realizar validacion Cruzada\n\n -> Entrenamiento (con el uso del algoritmo Back Propagation)\n\n -> Test(con el uso del algoritmo Back Propagation)\n\n ->Aproximar (conjunto de datos que no se conoce el valor esperado)\n\n ->Clasificar (conjunto de datos que no se conoce la clase asignada)\n\n -> Salir(termino del programa)\n")

	# 	v0.mainloop()
		
	def main(self):
		#self.MensajeBienvenida()
		self.MenuPrincipal()

		

iniciar=Principal()
iniciar.main()
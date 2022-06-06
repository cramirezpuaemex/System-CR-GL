# Programa de redes neuronales basado en el codigo escrito en C++ de Roberto Alejo Eleuterio
#Desarrollado por Carlos Ramirez Pina
import sys
from Tkinter import *
import tkFileDialog 
import tkMessageBox
from ScrolledText import *
import ttk
from OpenFile_multiple import *
from scross import *
import decimal
import random
import math
from Guardar_datos import *
from tkFileDialog import askopenfilename


class Datos_correlacion():
	print "welcome to system for egenerate calog of the events seismic"
	filename = ""
	pathArchivoDE=None
	pathArchivoDF=None
	def pathfileDE(self):

		inicia_guardando=Guardar_datos()


		inicia=OpenFile_multiple()

		self.filename = inicia.main()
		return(self.filename)
	def pathfileDF(self):
		Tipo=" Select files in format SAC"
		inicia=OpenFile_multiple(Tipo)

		self.filename = inicia.main()
		return(self.filename)
	def abrirArchivo(self):
		print ':)****'
		
		archivo =self.pathfileDE()
		self.etiquetaPath.config(text="Archivos selecionados:"+str(len(archivo)))
		self.pathArchivoDE=archivo
		#print  self.pathArchivoDE
		
	def abrirArchivoFile(self):

		archivo =self.pathfileDF()
		self.etiquetaPath1.config(text="Archivos selecionados:"+str(len(archivo)))
		self.pathArchivoDF=archivo
		#print  self.pathArchivoDF



	def trabajar(self):
		#print  ":)"
		respuesta=self.validar()
		if respuesta == True:
			#============================ Se indica path para guardar resultados ===============================
			inicia=Guardar_datos()
			Tipo="Select file for salve results"
			ruta_guardar_datos=inicia.guardar_directorio(Tipo)
			print '=============================================='
			print  " path para guardar datos", ruta_guardar_datos
			print '=============================================='
			inicia_xcross=scross()
			estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']

			for i in range(len(self.pathArchivoDE)):
			#for i in range(9, 15):
				#fo = open(ruta_guardar_datos+'/Archivos_Analisados.txt', 'a')
				#fo.write('==================================\n')
				#fo.write('Inicia analizar archivo: \n')
				#fo.write(self.pathArchivoDE[i]+'\n')
				#fo.write('==================================\n')
				#fo.close()
				for ii in estaciones:
					if self.pathArchivoDE[i].find(ii) !=-1:
						self.estacion_1=ii

				#=========================================
				for j in range(len(self.pathArchivoDF)):				
				#for j in range(len(self.pathArchivoDE)):
				#or j in range(50):
					for jj in estaciones:
						if self.pathArchivoDF[j].find(jj) != -1:
							self.estacion_2=jj
					if self.estacion_1==self.estacion_2:
						inicia_xcross.main( self.pathArchivoDE[i], self.pathArchivoDF[j], ruta_guardar_datos)
						#inicia_xcross.main( self.pathArchivoDE[j], self.pathArchivoDF[i], ruta_guardar_datos)
						#print 'termina una carpeta del catalogo'
				#fo = open(ruta_guardar_datos+'/Archivos_Analisados.txt', 'a')
				#fo.write('==================================\n')
				#fo.write('Termina de analizar archivo: \n')
				#fo.write(self.pathArchivoDE[i]+'\n')
				#fo.write('==================================\n')
				#fo.close()
				#self.app.destroy()
			#tkMessageBox.showinfo("En Proceso", "Preciona OK para continuar\n        Favor de esperar")
			self.app.destroy()
			#inicia=ClasificaPrueba()
			#inicia.main(self.pathArchivoDE, self.pathArchivoDF)


	

	def validar(self):
		valido = False
		##print  'entra'

		#VALIDAR QUE EXITAN PATH SI NO SE SELECCIONO MANUAL
		#if self.pathArchivoDE == None and manualDE == False:
		if self.pathArchivoDE == None:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar el primer conjunto  de datos de entrada")
		elif self.pathArchivoDF == None and manualDES == False:
			valido = False
			tkMessageBox.showinfo("Error", "Debe seleccionar el segundo conjunto de datos de entrada")
		else:
			valido = True

		return valido


	def habilitarManual(self):
		if len(self.b)!=0:
			self.botonGuardar.config(state=NORMAL)



	def habilitarDataSet(self, long):
		if long !=0:
			self.entrada_texto.config(state=NORMAL)
			self.entradaIter.config(state=NORMAL)
			self.entradaMSE.config(state=NORMAL)
			self.botonEntrenar.config(state=NORMAL)


		# cadena = "Factor de correccion: " + str(alfa) + "\n" + "Error minimo esperado: " + str(errorminimo) + "\n" + "Error Promedio: " + str(errorpromedio) + "\n"+ "Iteracion: " + str(iteracion) + "\n" + "Error minimo: " + str(minimo) + "\n" + "r1: " + str(ww11) + "\n" + "r2: " + str(uu) + "\n" + "bias: " + str(bb1) + "\n"	+ "bias2:"  + str(bb3) + "\n"
		# result.config(state=NORMAL)
		# result.insert(INSERT, cadena)
		# result.config(state=DISABLED)
	def cambiar_stringvar(nuevotexto,stringvar):
		stringvar.set(nuevotexto)



	def main(self):
		valor = "" #para el inicio los entry tenga b

		self.app = Tk()
		self.app.title('Input of data for correlation')
		self.app.geometry("736x200")
		self.app.maxsize(736, 200)

		#VP -> VENTANA PRINCIPAL
		vp = Frame(self.app)
		
		vp.grid(column=0, row=0, padx=(50,50), pady=(10,10)) #posicionar los elementos en tipo matriz, padx es para margen
		vp.columnconfigure(0,weight=1)  #tamanio relativo a las columnas
		vp.rowconfigure(0,weight=1)


		#DATOS ENTRADA POR PATH
		etiquetaDE = Label(vp,text="Set data: ")
		etiquetaDE.grid(column=0, row=0) #especificar en la final y columna 
		
		boton = Button(vp, width=21, text="Select for day (repository)", command=self.abrirArchivo)
		boton.grid(column=2,row=0)

		etiquetaDF = Label(vp,text="Select set data ")
		etiquetaDF.grid(column=0, row=2) #especificar en la final y columna 
	
		boton = Button(vp, width=21, text="Select catalog (masters)", command=self.abrirArchivoFile)
		boton.grid(column=2,row=2)
 
		self.etiquetaPath = Label(vp,text=" ")
		self.etiquetaPath.grid(column=1, row=0) 

		self.etiquetaPath1 = Label(vp,text=" ")
		self.etiquetaPath1.grid(column=1, row=2) 
		
		
		
		# #EJECUCION
		boton = Button(vp, width=20, text="Run", command=self.trabajar)
		boton.grid(column=1,row=8)


	


		botonSalir = Button(vp, width=20, text="Quit", command=self.app.destroy)
		botonSalir.grid(column=2,row=22)
		


		#CREDITOS
		etiqueta = Label(vp,text="Elaborado por: CARLOS RAMIREZ PINA")
		etiqueta.grid(column=1, row=40) 
		self.app.mainloop()


#Inicia_D_C=Datos_correlacion()
#Inicia_D_C.main()


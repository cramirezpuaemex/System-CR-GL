import os.path
from tkinter import messagebox
import subprocess
import glob
import math
from os import remove
import tkinter as tk
from tkinter import ttk
from Tkinter import *
from Rutas import *
from Rutas_Dir import *
from File_Data_hypDD import *
from station import *
from In_Out_HypDD import *
from data_times_hyp import *
from files_ct_cc_hypdd import *
from Principal import *
class file_hypodd():

	def menu(self, name):
		self.model=name
		print self.model
		#self.root2 = tk.Tk()
		#self.root2.config(width=300, height=200)
		#self.root2.title("Module using HypoDD program")
		#boton = ttk.Button(text="1.- Crear archivo de configuracion (inp)", command=self.settings)
		#boton1 = ttk.Button(text="2.- Localizar usando HypoDD", command=self.HypoDD)
		#boton2 = ttk.Button(text="3.- Crear archivo  station", command=self.station)
		#boton3 = ttk.Button(text="Salir", command=self.salir)
		#boton.place(x=10, y=20)
		#boton1.place(x=10, y=50)
		#boton2.place(x=10, y=80)
		#boton3.place(x=100, y=120)
		#self.root2.mainloop()
		self.root2 = Tk()
		self.root2.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root2.title(" Input name to identifier")
		#INPUT=""     

		 
		self.Display = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="6.- Create file of settings(inp)",
		                 command = lambda:self.settings())

		self.Display2 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="1.- Create file to dat (.dat)",
		                 command = lambda:self.file_data())
		self.Display3 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="2.- Create file to station(.sta)",
		                 command = lambda:self.station())		
		#self.Display4 = Button(self.root2, height = 2,
		                 #width = 40,
		                 #text ="3.- Crear archivo  station",
		                 #command = lambda:self.station())
		self.Display5 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="3.- Create file of data times",
		                 command = lambda:self.data_times())
		self.Display6 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="4.- Create file dt.ct",
		                 command = lambda:self.files_ct())
		self.Display7 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="5.- Create file dt.cc",
		                 command = lambda:self.files_cc())

		self.Display1 = Button(self.root2, height = 2,
		                 width = 40,
		                 text ="7.- System locations using HypoDD",
		                 command = lambda:self.HypoDD())
		self.Display8 = Button(self.root2, height = 2,
		                 width = 20,
		                 text ="Quit",
		                 command = lambda:self.salir())

		#self.inputtxt.pack()
		
		
		self.Display2.pack()
		self.Display3.pack()
		#self.Display4.pack()		
		self.Display5.pack()
		self.Display6.pack()
		self.Display7.pack()
		self.Display.pack()	
		self.Display1.pack()
			
		self.Display8.pack()
		mainloop()

	def settings(self):
		print ':)  ******* settings'
		print "inp"

		self.root2.destroy()
		self.create_file()
		
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)


	def HypoDD(self):
		print ':)  ******* HypoDD'
		print "loc"
		self.root2.destroy()
		self.Software_hypoDD()
		
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)



	def file_data(self):
		print ':)  ******* file_data'
		self.root2.destroy()
		inicio_data_dat=File_Data_hypDD()
		inicio_ruta=Rutas()
		Tipo="File with localization"
		path_loca=inicio_ruta.main(Tipo)
		inicio_data_dat.main(path_loca,self.model)
		
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)


	def data_times(self):
		print ':)  ******* data_times'
		inicio_data_times =data_times_hyp()
		self.root2.destroy()
		opc=1
		self.main_data_times_hyp(self.model, opc)


	def end_data_times(self):

		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)
		

		
		#messagebox.showinfo(message="process completed successfully", title="Message")
		#self.menu(self.INPUT)

	def files_ct(self):
		print ':)  ******* dt.ct'
		self.root2.destroy()
		inicio_files_ct=files_ct_cc_hypdd()
		#model="codex_17"
		inicio_files_ct.main_files_ct(self.model)

		self.root2.destroy()
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)
	def files_cc(self):
		print ':)  ******* dt.cc'
		self.root2.destroy()
		inicio_in_out=In_Out_HypDD()

		
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)
	def station(self):
		print ':)  ******* station'
		self.root2.destroy()
		inicio_data_sta=station()
		inicio_ruta=Rutas()
		Tipo="File with station"
		path_loca=inicio_ruta.main(Tipo)
		inicio_data_sta.main(path_loca,self.model)
		
		messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu(self.INPUT)


	def salir(self):
		#self.root = tk.Tk()
		self.root2.destroy()
		#iniciar=Principal()
		#iniciar.main()

	def Take_input(self):

		self.INPUT = self.inputtxt.get("1.0", "end-1c")
		print(self.INPUT)
		a=0
		if self.INPUT!="":
			self.root1.destroy()
			print "*****"
			self.menu(self.INPUT)
			#print "INPUT", self.INPUT
	



	def Input_data(self):

		self.root1 = Tk()
		self.root1.geometry("300x100")
		#self.root.config(width=300, height=100)
		self.root1.title(" Input name to identifier")
		#INPUT=""     
		self.inputtxt = Text(self.root1, height = 2,
		                width = 35,
		                bg = "light yellow")
		 
		self.Display = Button(self.root1, height = 2,
		                 width = 20,
		                 text ="Start",
		                 command = lambda:self.Take_input())
		 

		self.inputtxt.pack()
		self.Display.pack()
		mainloop()

	def main(self):
		print "Bienvenidos al Software hypoDD con python"
		
		#print "Ingresa el nombre del modelo a ser analizado:"
		#self.model=""
		#self.model=raw_input()
		#print type(self.model)

		#print "el nombre del modelo es:"+ self.model

		self.Input_data()


		'''
		resp="y"
		while resp == "Y" or resp == "y" or resp == "yes" or resp== "YES":
			print "Selecciona la opcion que deseas realizar"

			print "1.- crear archivo de configuracion (inp)"
			print "2.- Localizar usando HypoDD"
			print "3.crear archivo  station"
			opc=input("Selecciona opcion: " )

			if opc ==1:
				print "inp"
				self.create_file()
				resp=raw_input("Deseas realizar otra proceso (Yes), cualquier valor para terminar")

			elif opc ==2:
					print "loc"
					self.Software_hypoDD()
					resp=raw_input("Deseas realizar otra proceso (Yes), cualquier valor para terminar")
			elif opc ==3:
				print "station"
				resp=raw_input("Deseas realizar otra proceso (Yes), cualquier valor para terminar")
			else: 
				print "Opcion incorrecta, ingresa la opcion correcta"





		#self.model='codex_17'
			
		#self.create_file()
		#elf.Software_hypoDD()
		'''
		print "Termina Programa"

	def Lectura_file(self):
		inicio_ruta=Rutas()
		Tipo="Input file .crh"
		path=inicio_ruta.main(Tipo)
		#path="/home/carlos/Dropbox/hyp/codex/"+self.model+".crh"
		f = open(path,"r")
		arreglo= []
		contLin=0
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(' ')
				arreglo.append(datos)
			else:
				break

		return arreglo

	def Software_hypoDD(self):

		print "Entra a la funcion de Software"
		self.name_soft=(os.path.abspath(os.getcwd()))

		#p=""
		p = subprocess.Popen(['./hypoDD'],
                     			stdout = subprocess.PIPE,
                     			stdin  = subprocess.PIPE,
                     			stderr = subprocess.STDOUT )

			
		s=''
		line1=self.name_soft+'/Files_HypDD/'+self.model+'.inp\n'
		s+=line1
		print s	

		out = p.communicate( s )
		print out	


	def Menu_cc(self):
		self.root13 = Tk()
		self.root13.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root13.title("using settings with con file dt.cc")
		#INPUT=""     

		 
		self.Display = Button(self.root13, height = 2,
		                 width = 40,
		                 text ="Yes",
		                 command = lambda:self.file_cc_yes())

		self.Display2 = Button(self.root13, height = 2,
		                 width = 40,
		                 text ="Not",
		                 command = lambda:self.file_cc_not())

		#self.inputtxt.pack()
		self.Display.pack()
		self.Display2.pack()

		mainloop()
	def file_cc_yes(self):
		self.root13.destroy()
		Tipo="Select file with dt.cc"
		self.file_cc=inicio_rutas.main(Tipo)
		self.opc_cc=1
		self.Menu_IDAT()
	def file_cc_not(self):
		self.root13.destroy()
		self.opc_cc=0
		self.Menu_IDAT()


	def Menu_IDAT(self):
		self.root14 = Tk()
		self.root14.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root14.title("Select option for IDAT")
		#INPUT=""     

		 
		self.Display = Button(self.root14, height = 2,
		                 width = 40,
		                 text ="0 = synthetics;",
		                 command = lambda:self.settings_idat(opc=0))

		self.Display1 = Button(self.root14, height = 2,
		                 width = 40,
		                 text ="1= cross corr",
		                 command = lambda:self.settings_idat(opc=1))
		self.Display2 = Button(self.root14, height = 2,
		                 width = 40,
		                 text ="2= catalog",
		                 command = lambda:self.settings_idat(opc=2))
		self.Display3 = Button(self.root14, height = 2,
		                 width = 40,
		                 text ="3= cross & cat",
		                 command = lambda:self.settings_idat(opc=3))

		#self.inputtxt.pack()
		self.Display.pack()
		self.Display1.pack()
		self.Display2.pack()
		self.Display3.pack()

		mainloop()

	def settings_idat(self, opc):
		self.opc_idat=str(opc)
		self.root14.destroy()
		self.Menu_IPHA()

	def Menu_IPHA(self):
		self.root15 = Tk()
		self.root15.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root15.title("Select option for IDAT")
		#INPUT=""     

		 
		self.Display = Button(self.root15, height = 2,
		                 width = 40,
		                 text ="1 = p",
		                 command = lambda:self.settings_ipha(opc=1))

		self.Display1 = Button(self.root15, height = 2,
		                 width = 40,
		                 text ="2= s",
		                 command = lambda:self.settings_ipha(opc=2))
		self.Display2 = Button(self.root15, height = 2,
		                 width = 40,
		                 text ="3= p & s",
		                 command = lambda:self.settings_ipha(opc=3))


		#self.inputtxt.pack()
		self.Display.pack()
		self.Display1.pack()
		self.Display2.pack()


		mainloop()

	def settings_ipha(self, opc):
		self.opc_ipha=str(opc)
		self.root15.destroy()
		self.create_file_continue()


	def create_file(self):
		inicio_ruta_dir=Rutas_Dir()
		Tipo="path salve archivo .inp"
		self.path_create_file=inicio_ruta_dir.pathfile(Tipo)
		Tipo="Select file with dt.ct"
		inicio_rutas=Rutas()
		self.files_ct=inicio_rutas.main(Tipo)
		print "---+++++++++++",self.files_ct
		self.Menu_cc()
	def create_file_continue(self):
		#self.Menu_IDAT()

		#self.Menu_IPHA()



		self.name_salve_file=(os.path.abspath(os.getcwd()))
		self.sta_dat=self.name_salve_file+'/Files_HypDD/'+self.model+'_sta.dat'
		self.data_dat=self.name_salve_file+'/Files_HypDD/'+self.model+'.dat'
		datos_model=self.Lectura_file()
		for m in range(2):

			if m==0:

				fo = open(self.path_create_file+'/'+self.model+'.inp', 'w')
			else:
				fo = open(self.name_salve_file+'/Files_HypDD/'+self.model+'.inp', 'w')
			fo.write("* RELOC.INP:\n")
			fo.write("*--- input file selection\n")
			fo.write("* cross correlation diff times: (not used in this test)\n")
			if self.opc_cc==1:
				fo.write(self.files_cc+"\n")
			else:
				fo.write("#dt.cc\n")


			
			fo.write("*\n")
			fo.write("*catalog P & S diff times:\n")
			fo.write(self.files_ct+"\n")
			fo.write("*\n")
			fo.write("* event file:\n")
			fo.write(self.data_dat+"\n")
			fo.write("*\n")
			fo.write("* station file:\n")
			fo.write(self.sta_dat+"\n")
			fo.write("*\n")
			fo.write("*--- output file selection\n")
			fo.write("* original locations:\n")
			fo.write(self.path_create_file+"/"+self.model+".loc\n")
			fo.write("* relocations:\n")
			fo.write(self.path_create_file+"/"+self.model+".reloc\n")
			fo.write("* station information:\n")
			fo.write(self.path_create_file+"/"+self.model+".sta\n")
			fo.write("* residual information:\n")
			fo.write("*"+self.model+".res\n")
			fo.write("\n")
			fo.write("* source paramater information:\n")
			fo.write("*"+self.model+".src\n")
			fo.write("\n")
			fo.write("*\n")
			fo.write("*--- data type selection: \n")
			fo.write("* IDAT:  0 = synthetics; 1= cross corr; 2= catalog; 3= cross & cat \n")
			fo.write("* IPHA: 1= P; 2= S; 3= P&S\n")
			fo.write("* DIST:max dist [km] between cluster centroid and station \n")
			fo.write("* IDAT   IPHA   DIST\n")
			fo.write("    "+self.opc_idat+"     "+self.opc_ipha+"     400\n")
			fo.write("*\n")
			fo.write("*--- event clustering:\n")
			fo.write("* OBSCC:    min # of obs/pair for crosstime data (0= no clustering)\n")
			fo.write("* OBSCT:    min # of obs/pair for network data (0= no clustering\n")
			fo.write("* OBSCC  OBSCT    \n")
			fo.write("     2     2      \n")
			fo.write("*\n")
			fo.write("*--- solution control:\n")
			fo.write("* ISTART:  	1 = from single source; 2 = from network sources\n")
			fo.write("* ISOLV:	1 = SVD, 2=lsqr\n")
			fo.write("* NSET:      	number of sets of iteration with specifications following\n")
			fo.write("*  ISTART  ISOLV  NSET\n")
			fo.write("    1        2      2\n")
			fo.write("*\n")
			fo.write("*--- data weighting and re-weighting: \n")
			fo.write("* NITER: 		last iteration to use the following weights\n")
			fo.write("* WTCCP, WTCCS:		weight cross P, S \n")
			fo.write("* WTCTP, WTCTS:		weight catalog P, S \n")
			fo.write("* WRCC, WRCT:		residual threshold in sec for cross, catalog data \n")
			fo.write("* WDCC, WDCT:  		max dist [km] between cross, catalog linked pairs\n")
			fo.write("* DAMP:    		damping (for lsqr only) \n")
			fo.write("*       ---  CROSS DATA ----- ----CATALOG DATA ----\n")
			fo.write("* NITER WTCCP WTCCS WRCC WDCC WTCTP WTCTS WRCT WDCT DAMP\n")
			fo.write("  5      -9     -9   -9   -9   1.0    -9  -9    -9   20\n")
			fo.write("  5      -9     -9   -9   -9   1.0    -9   5     8   20\n")
			fo.write("*\n")
			fo.write("*--- 1D model:\n")
			fo.write("* NLAY:		number of model layers  \n")
			fo.write("* RATIO:	vp/vs ratio \n")
			fo.write("* TOP:		depths of top of layer (km) \n")
			fo.write("* VEL: 		layer velocities (km/s)\n")
			fo.write("* NLAY  RATIO \n")

			#datos_model=self.Lectura_file()

			fo.write("   "+str(len(datos_model)-1)+"     1.73\n")
			#fo.write("*Colima model(jimenez, 2012). Depth to top, velocity\n")
			print datos_model[0]
			fo.write("*"+str(datos_model[0])+". Depth to top, velocity\n")
			fo.write("* TOP \n")

			#print datos_model
			#fo.write("*********Datos nuevos****\n")
			for i in range(1,len(datos_model)):
				#i=i+1
				aux=[]
				for j in datos_model[i]:
					if j!="":
						aux.append(j)
				datos_model[i]=aux
	
				#print datos_model[i]
				print datos_model[i][1]," ",
			
				fo.write(str(datos_model[i][1]+" "))
			fo.write("\n")
			#fo.write("********* Fin Datos nuevos****\n")
			print "\n"



			#fo.write("0.0 2.0 4.0 6.0 12.0 18.0 35.0\n")
			fo.write("* VEL\n")
			for i in range(1,len(datos_model)):
				#i=i+1
				aux=[]
				for j in datos_model[i]:
					if j!="":
						aux.append(j)
				datos_model[i]=aux
	
				#print datos_model[i]
				print datos_model[i][0]," ",
				
				fo.write(str(datos_model[i][0]+" "))
			fo.write("\n")
			print "\n"
			#fo.write("		
			#fo.write("1.90 3.40 3.80 5.90 6.00 7.40 8.10\n")
			fo.write("*\n")
			fo.write("*--- event selection:\n")
			fo.write("* CID: 	cluster to be relocated (0 = all)\n")
			fo.write("* ID:	ids of event to be relocated (8 per line)\n")
			fo.write("* CID    \n")
			fo.write("    0      \n")
			fo.write("* ID")

	def main_data_times_hyp(self, mode, opc):
		#model='codex_16'
		self.opc=opc
		self.model=mode
		print "Bienvenidos al Software file input and out file HypoDD con python"

		print "Ingresa el nombre del modelo a ser analizado:"
		#model=""
		#model=raw_input()
		print type(self.model)
		self.archivos_origen=self.origen(self.model)
		print "****orig"
		self.archivos_origen.pop(0)
		for i in self.archivos_origen:
			print i
		pregunta_b=0
		self.main_pregunta(pregunta_b)

	def datos_proceso(self, archivos_pick):
		#archivos_pick=self.Lec_files()

		#archivos_origen=self.origen(model)
		#print "****origen"
		#archivos_pick=self.Read_files()

		print "****read"
		
		
		#print len(archivos_pick)
		#print len(archivos_cross)
		print "Nombre del modelo:  ", self.model
		inicio_rutas_dir=Rutas_Dir()
		Tipo="Input path to salve files times"
		path_salve=inicio_rutas_dir.pathfile(Tipo)
		path_salve=path_salve+'/datos_time/'+self.model+'/'
		for i in range(len(self.archivos_origen)):
			idece_analizar=int(self.archivos_origen[i][0])
			self.Proceso(archivos_pick[idece_analizar], self.archivos_origen[i], self.model, path_salve )

		print "************************"
		print "Fin de proceso uno"
		print "************************"


		self.end_data_times()
		#messagebox.showinfo(message="process completed successfully", title="Message")
		#inicio_hypDD=file_hypodd()
		#inicio_hypDD.data_times(opc=2)
	
						
		#resp=raw_input("Deseas realizar otra proceso (Yes), ingresa cualquier valor y enter para terminar:  ")

	def origen(self, model):	
		#model='codex_13'
		inicio_rutas=Rutas()
		Tipo="Input path "+model+" localization"
		ruta_loca=inicio_rutas.main(Tipo)

		#ruta_loca='/home/carlos/Dropbox/Catalogo_2006_2007/'+model+'.txt'
		f = open(ruta_loca,"r")
		elementos= []
		while True:
			linea = f.readline()
			if linea:
				elementos.append(linea)
			else:
						break

		elementos1 = []
		for i in elementos:
			lista=i.split("\t")
			lista.remove("\n")
			elementos1.append([(e) for e in lista])
		
		archivos=[]


		#for i in elementos1:
			#aux=[]
			#print i[0], i[2], i[3]
		
		return elementos1	
	def main_pregunta(self, b):
		if b==0:
			self.a=[]
			self.pregunta()
		elif b==1:
			self.pregunta()
		else:
			print self.a
			self.Lec_files(self.a)

	def Pregunta_yes(self):
	    inicio_rutas_dir=Rutas_Dir()
	    self.root3.destroy()
	    Tipo="Path Directory whit files phases"
	    #Tk().withdraw()
	    file=inicio_rutas_dir.pathfile(Tipo)
	    #borrar()
	    self.a.append(file+'/')
	    b=1
	    self.main_pregunta(b)


	def Pregunta_not(self):
	    self.root3.destroy()
	    b=2
	    self.main_pregunta(b)


	def pregunta(self):

		a=[]
		self.root3 = Tk()
		#self.root3.config(bd=25)
		self.root3.title(" Input name to identifier")
		T = Text(self.root3,  height = 1, width = 30)

		Fact = """Select directory with files"""

		T.pack()
		Button(self.root3, text="yes", command=self.Pregunta_yes).pack(side="left")
		#Button(root, text="Resta", command=resta).pack(side="left")
		Button(self.root3, text="Not", command=self.Pregunta_not).pack(side="right")

		T.insert(tk.END, Fact)
		self.root3.mainloop()

	def Lec_files(self,a):
		

		files_all=a
		print "recibe los valores: ", files_all

		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/','/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2007/']
		seq=0		
		path_archivos=[]
		for fi in files_all:
			file=fi
			archivos=os.listdir(file)

			archivos=sorted(archivos)
			#path_archivos+=archivos
			#print 'Archivos: \n', archivos
			aux=[]
			for arh in range(len(archivos)):
				i=archivos[arh]
				aux.append(file+i)
			path_archivos+=aux	

		print path_archivos
		print "proceso datos proceso"
		self.datos_proceso(path_archivos)	
			
		#return path_archivos

	def Proceso(self, i, origen, model, path_salve):
		#funcion para las nuevas modificaciones
		#def Proceso(self, path, origen, model):
		print "Ingresa al proceso Data times"
		#print path
		print origen
		print model
		#inicio_rutas_dir=Rutas_Dir()
		#Tipo="Input path to salve files times"
		#path_salve=inicio_rutas_dir.pathfile(Tipo)
		'''
		#nueva modificacion para cear los archivos data.times
		inicio_read_file=Lectura_file()
		arreglo=[]
		arreglo=inicio_read_file.main(path)
		for i in arreglo:
			print i
		time_origen=origen[3]
		if time_origen[5]==' ':
			aux_o1=time_origen[0:4]
			aux_o2=time_origen[6:len(time_origen)]
			time_origen=aux_o1+'0'+aux_o2
			#print 'aqui', time_origen
		time_origen=time_origen.replace(' ', '')
		print 'cambiado', time_origen
		origen_hora=int(time_origen[0:2])
		origen_min=int(time_origen[2:4])
		origen_seg=int(time_origen[len(time_origen)-5:len(time_origen)-3])
		origen_cen=float(time_origen[len(time_origen)-3:len(time_origen)])
		print origen_hora
		print origen_min
		print origen_seg
		print origen_cen
		for a in arreglo:
			if len(a[0])==24:
				time_pick=(a[0][len(a[0])-9:len(a[0])])
				pick_hora=int(time_pick[0:2])
				pick_min=int(time_pick[2:4])
				pick_seg=int(time_pick[len(time_pick)-5:len(time_pick)-3])
				pick_cen=float(time_pick[len(time_pick)-3:len(time_pick)])
			else:
				time_pick=(a[0][15:24])
				#time_pick=float(a[0][len(a[0])-9:len(a[0])])
				pick_hora=int(time_pick[0:2])
				pick_min=int(time_pick[2:4])
				pick_seg=int(time_pick[len(time_pick)-5:len(time_pick)-3])
				pick_cen=float(time_pick[len(time_pick)-3:len(time_pick)])
			
			print pick_hora
			print pick_min
			print pick_seg
			print pick_cen


			result_hora= pick_hora-origen_hora
			print "resultado hora", result_hora
			
			result_min=pick_min-origen_min
			if result_min <0:
				aux_min=59-origen_min
				result_min=aux_min+pick_min
			result_seg=pick_seg-origen_seg
			if result_seg <0:
				aux_seg= 59-origen_seg
				result_seg=aux_seg+pick_seg
			result_cen= pick_cen-origen_cen
			if result_cen <0:
				aux_cen= 0.99- origen_cen
				result_cen= pick_cen+aux_cen
			print "*****************"
			print "resul_min",result_min
			print "resul_seg",result_seg
			print "resul_min",result_cen
			print "*****************"

			print "Pick"
			print pick_hora, " ", pick_min," ",float(pick_seg)+float(pick_cen)
			print "origen"
			print origen_hora, " ", origen_min," ", float(origen_seg)+float(origen_cen)
			print "resultado"
			print float(result_seg)/10
			time=float(result_min)+(float(result_seg)/10)

			print "time", time

			print result_hora," ",result_min,".",result_seg
			# Verifica si la carpeta existe para guardar resultados, en otro caso genera l carpeta
			path_salve='/home/carlos/Escritorio/datos_time/'+model+'/'
			if not os.path.exists(path_salve):
				os.makedirs(path_salve)
			
			fo = open('/home/carlos/Escritorio/datos_time/'+model+'/id_'+origen[0]+'.txt', 'a')
			fo = open(path_salve+'id_'+origen[0]+'.txt', 'a')

			#if result_seg < 30 and float(origen[7]) < 2:
				#time=result_seg+result_cen
			time =str(time)
			if len(time)<5:
				for i in range(5-len(time)):
					time=time+'0'
			print a[0][0:4], time, 'P'
			fo.write(str(a[0][0:4])+'   '+str(time)+'\n')

		#fin de la seccion modificada en data.times
		'''

		inicio_read_file=Lectura_file()
		arreglo=[]
		arreglo=inicio_read_file.main(i)
		print origen
		time_origen=origen[3]
		if time_origen[5]==' ':
			aux_o1=time_origen[0:4]
			aux_o2=time_origen[6:len(time_origen)]
			time_origen=aux_o1+'0'+aux_o2
			#print 'aqui', time_origen
		time_origen=time_origen.replace(' ', '')
		#print 'cambiado', time_origen
		origen_hora=int(time_origen[0:2])
		origen_min=int(time_origen[2:4])
		origen_seg=int(time_origen[len(time_origen)-5:len(time_origen)-3])
		origen_cen=float(time_origen[len(time_origen)-3:len(time_origen)])
		for a in arreglo:
			if len(a[0])==24:
				time_pick=(a[0][len(a[0])-9:len(a[0])])
				pick_hora=int(time_pick[0:2])
				pick_min=int(time_pick[2:4])
				pick_seg=int(time_pick[len(time_pick)-5:len(time_pick)-3])
				pick_cen=float(time_pick[len(time_pick)-3:len(time_pick)])
			else:
				time_pick=(a[0][15:24])
				#time_pick=float(a[0][len(a[0])-9:len(a[0])])
				pick_hora=int(time_pick[0:2])
				pick_min=int(time_pick[2:4])
				pick_seg=int(time_pick[len(time_pick)-5:len(time_pick)-3])
				pick_cen=float(time_pick[len(time_pick)-3:len(time_pick)])
			

			if pick_cen-origen_cen<0:
				#print 'menor en cen'
				result_cen=pick_cen+(0.99-origen_cen)
				pick_seg=pick_seg-1
			else:
				result_cen=pick_cen-origen_cen
			#print pick_seg
			if pick_seg-origen_seg<0:
				#print 'menor seg'
				result_seg=pick_seg+(59-origen_seg)
				pick_min=pick_min-1
			else:
				result_seg=pick_seg-origen_seg
			if pick_min- origen_min<0:
				#print 'menor min'
				result_min=pick_min+(59-origen_min)
				pick_hora-1
			else:
				result_min=pick_min- origen_min
			if pick_hora-origen_hora<0:
				#print 'menor hora'
				result_hora=pick_hora+(23-origen_hora)
			else:
				result_hora=pick_hora-origen_hora

			#print time_origen, time_pick
			#print a[0][0:4] , '---', pick_hora,pick_min,pick_seg, pick_cen, '---', origen_hora,origen_min,origen_seg, origen_cen,'---', result_hora, result_min, result_seg, result_cen
			#model='codex_13'
			# Verifica si la carpeta existe para guardar resultados, en otro caso genera l carpeta
			
			
			if not os.path.exists(path_salve):
				os.makedirs(path_salve)
			
			#fo = open('/home/carlos/Escritorio/datos_time/'+model+'/id_'+origen[0]+'.txt', 'a')
			fo = open(path_salve+'id_'+origen[0]+'.txt', 'a')
			if result_seg < 30 and float(origen[7]) < 2:
				time=result_seg+result_cen
				print a[0][0:4], time, origen[7], 'P'
				fo.write(str(a[0][0:4])+'   '+str(time)+'\t'+str(origen[7])+'\n')


#inicio=file_hypodd()
#inicio.main()
import os.path
import subprocess
import glob
import math
from tkinter import filedialog
from Tkinter import *
import tkFileDialog
from os import remove
from File_hyp import *
from Tiempo_hyp import *
from Hyp_Lectura_file import *
from Hyp_Analisis_Resultados import *
from Software_hyp import *
from Software_hyp_ptr import *
from Rutas_Dir import *
from Rutas import *

class hyp_path():

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
		print '**************************'
		print 'Hyp1.40'
		print '**************************'
		print "Welcome the Software file input and out file HypoInverse con python"

		self.Input_data()
		




	def Work(self, name):
		

		#Create instance  of settings file .hyp
		inicio_file_hyp=File_hyp()
		self.model=name
		#Model's input to be analyzed.
		modelos=[]
		modelos.append(name)
		#modelos=['codex_17']
		for i in modelos:
			print 'modelo', i
			#Get path of the files of the system CR_GL
			self.name_salve_file=(os.path.abspath(os.getcwd()))
			print "------", self.name_salve_file, "-------------"

			self.inicio_ruta=Rutas()
			self.inicio_ruta_dir=Rutas_Dir()
			Tipo="Path of file stations"
			self.path_estaciones=self.inicio_ruta.main(Tipo)
			print "sta", self.path_estaciones
			Tipo="Path of file DEL"
			self.path_del=self.inicio_ruta.main(Tipo)
			print "del", self.path_del
			Tipo="Path of the model in format crh"
			self.path_crh=self.inicio_ruta.main(Tipo)
			print "crh", self.path_crh
			Tipo="Path for salve results of the system"
			
			self.path_finish=self.inicio_ruta_dir.pathfile(Tipo)

			inicio_file_hyp.file_main(i, self.name_salve_file, self.path_estaciones, self.path_del, self.path_crh)
			self.Read_files(i)
			#self.proceso(i)


	def Pregunta_yes_hyp(self):
	    inicio_rutas_dir=Rutas_Dir()
	    self.root8.destroy()
	    Tipo="Path Directory whit files phases"
	    #Tk().withdraw()
	    file=inicio_rutas_dir.pathfile(Tipo)
	    print "file", file
	    #borrar()
	    self.a_hyp.append(file+'/')
	    print self.a_hyp
	    
	    self.menu_hyp_file()

	def salir_hyp(self):
		#self.root = tk.Tk()
		print "salir"
		self.root8.destroy()
		self.Read_files_part_two()

	def menu_hyp_file(self):
		self.root8 = Tk()
		self.root8.geometry("400x200")
		#self.root.config(width=300, height=100)
		self.root8.title(" Select path catalogs of event seismic .SAC")
		#INPUT=""     

		 
		self.Display = Button(self.root8, height = 2,
		                 width = 40,
		                 text ="yes",
		                 command = lambda:self.Pregunta_yes_hyp())

	

		self.Display8 = Button(self.root8, height = 2,
		                 width = 20,
		                 text ="not",
		                 command = lambda:self.salir_hyp())

		#self.inputtxt.pack()
		self.Display.pack()
		
		self.Display8.pack()
		mainloop()




	def Read_files(self, model):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		#self.inicio_ruta_dir=Rutas_Dir()
		#inicio_ruta=Rutas()
		self.a_hyp=[]
		self.menu_hyp_file()

	def Read_files_part_two(self):	
		files_all=self.a_hyp
		print "files_all", files_all, "y continua"

		model=self.model
		




		#Tipo="Path of files of the phases be analyzed "
		#files_all.append(self.inicio_ruta_dir.pathfile(Tipo))
		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/','/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2007/']
		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/']
		#file='/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/'
		seq=0
		for fi in files_all:
			file=fi+'/'
			archivos=os.listdir(file)
			archivos=sorted(archivos)
			#print 'Archivos: \n', archivos
		
			
			for arh in range(len(archivos)):
				i=archivos[arh]
				aux=file+i
				#if arh == 13:
				self.proceso(aux, model, seq)
				seq+=1

		######################################################

	def proceso(self, i, model, seq):
		#print i
		file_name=i[len(i)-13:len(i)-4]
		print file_name
		#i='/home/carlos/Dropbox/2006a/phases/2006/Phases_038.02.38.txt'
		#i='/home/carlos/Dropbox/2006a/phases/2006/Phases_036.10.57.txt'
		inicio_read_file=Hyp_Lectura_file()
		arreglo=[]
		arreglo=inicio_read_file.main(i)

		cont=0
		hora=0
		minut=0
		seg=0
		estaciones_llegada=[]
		tiempo_llegada=[]
		minuto_llegada=[]
		hora_llegada=[]
		for j in arreglo:
			#print j
			hora+=int(j[0][15:17])
			minut+=int(j[0][17:19])
			seg+=float(j[0][19:24])
			cont+=1
			hora_llegada.append(j[0][15:17])
			minuto_llegada.append(j[0][17:19])
			tiempo_llegada.append(j[0][19:24])
			estaciones_llegada.append(j[0][0:4])

		#print hora_llegada, len(hora_llegada)
		#print minuto_llegada, len(minuto_llegada)
		resultados=[]
		inicio_tiempo=Tiempo_hyp()
		resultados=inicio_tiempo.proceso_tiempo(hora_llegada, minuto_llegada, tiempo_llegada, estaciones_llegada)
		#print 'resultados', resultados
		hora_llegada=[]
		minuto_llegada=[]
		tiempo_llegada=[]
		estaciones_llegada=[]
		hora_llegada=resultados[0]
		minuto_llegada=resultados[1]
		tiempo_llegada=resultados[2]
		estaciones_llegada=resultados[3]


		#print estaciones_llegada, 'len', len(estaciones_llegada)
		#print hora_llegada, 'len', len(hora_llegada)
		#print minuto_llegada, 'len', len(minuto_llegada)
		#print tiempo_llegada, 'len', len(tiempo_llegada)

		if len(tiempo_llegada)>=3:

			
			#path_estaciones='/home/carlos/Dropbox/hyp/codex/codex.sta'
	
		
			arreglo_estaciones= []
			contLin=0
			arreglo_estaciones=inicio_read_file.main(self.path_estaciones)
			#print '++++++++++++++', arreglo_estaciones
			longitud_min=[]
			longitud_g=[]
			latitud_min=[]
			latitud_g=[]
			for e in estaciones_llegada:
				for j in arreglo_estaciones:
					if j[0].find(e) != -1:
						latitud_g.append(j[0][15:17])
						latitud_min.append(j[0][18:24])
						longitud_g.append(j[0][26:29])
						longitud_min.append(j[0][30:36])
						break
	

			aux_lag=0
			aux_lam=0
			aux_log=0
			aux_lom=0
			#for j in range(len(estaciones_llegada)):
			for j in range(3):
				aux_lag+=int(latitud_g[j])
				aux_lam+=float(latitud_min[j])
				aux_log+=int(longitud_g[j])
				aux_lom+=float(longitud_min[j])
				#print estaciones_llegada[j],  latitud_g[j], latitud_min[j],longitud_g[j], longitud_min[j]
			
			num=len(latitud_min)
			#a1= int(aux_lag/num)
			#a2= round(float(aux_lam/num),1)
			#a3= int(aux_log/num)
			#a4= round(float(aux_lom/num),1)
			a1= int(aux_lag/3)
			a2= round(float(aux_lam/3),1)
			a3= int(aux_log/3)
			a4= round(float(aux_lom/3),1)
	
	
			#******************************************************************************************************
			#******************************************************************************************************	
			#******************************************************************************************************	
			hora=hora/cont
			minuto=minut/cont
			segundo=round((seg/cont), 1)
			
			# if len(str(segundo))<5:
			# 	fecha =str(hora)+str(minuto)+'0'+str(segundo-5)
			# else:
			# 	fecha =str(hora)+str(minuto)+str(segundo-5)
	
	
			segundo_aux=float(tiempo_llegada[0])
			segundo_aux=round(segundo_aux,1)
			#print 'segundo', segundo_aux
			if len(str(segundo_aux))<4:
				fecha =str(hora_llegada[0])+str(minuto_llegada[0])+'0'+str(segundo_aux-1)
			else:
				fecha =str(hora_llegada[0])+str(minuto_llegada[0])+str(segundo_aux-1)
	
	
	
			#print 'fecha', fecha
	
			
	
			#******************************************************************************************************
			#******************************************************************************************************	
			#******************************************************************************************************	
			
			
			inicio_software_hyp=Software_hyp()
			resultados_software=inicio_software_hyp.main(fecha, a1, a2, a3, a4, arreglo, file_name, seq, self.name_salve_file)
	
	
	
			errores_ERZ=resultados_software[0]
			errores_ERH=resultados_software[1]
			ubicacion=resultados_software[2]
			depth=resultados_software[3]

			inicio_analisis_resultados= Hyp_Analisis_Resultados()
		
			if len(errores_ERZ)!=0:
	
				resltados_analisis=inicio_analisis_resultados.main(errores_ERZ)
				aux_uz=resltados_analisis[0]
				#aux_dep=resltados_analisis[1]
				#aux_uh=resltados_analisis[1]
				#aux_uz=errores_ERZ.index(min(errores_ERZ))
				#aux_uh=errores_ERH.index(min(errores_ERH))
	
				#print  ubicacion[aux_uz]
				#print 'minimo ERZ\n', ubicacion[aux_uz]
				#print 'minimo ERH\n', ubicacion[aux_uh]
				#print  ubicacion[aux_uz]

				profunidad=depth[aux_uz]

				#print 'len vectores', len(ubicacion), len(depth)
				#print 'profunidad', profunidad
				inicio_software_hyp_ptr=Software_hyp_ptr()
				inicio_software_hyp_ptr.main(fecha, a1, a2, a3, a4, arreglo, profunidad, self.name_salve_file)
				path_ptr= self.name_salve_file+'/File_hyp/rcodex.prt'
				arreglo_ptr=[]				
				arreglo_ptr=inicio_read_file.main(path_ptr)

				#print '****************************************'
				
				for pt in range(len(arreglo_ptr)):
					#print pt, arreglo_ptr[pt][0][0:5]
					if arreglo_ptr[pt][0][0:5]== ' YEAR':
						pt_index=pt+1

						#print arreglo_ptr[pt_index-1][0][0:6]
						#print arreglo_ptr[pt_index]
						#print arreglo_ptr[pt_index][0][13:23]
						#print arreglo_ptr[pt_index][0][24:34]
						#print arreglo_ptr[pt_index][0][35:45]
						break
				
				#print '****************************************'
				primera_fila=[]
				segunda_fila=[]
				#print len(ubicacion[aux_uz])

				primera_fila.append(ubicacion[aux_uz][0:3])
				primera_fila.append('YEAR')
				primera_fila.append(ubicacion[aux_uz][7:11])
				primera_fila.append(ubicacion[aux_uz][15:26])
				primera_fila.append(ubicacion[aux_uz][28:31])
				primera_fila.append(ubicacion[aux_uz][36:39])
				primera_fila.append(ubicacion[aux_uz][42:48])
				primera_fila.append(ubicacion[aux_uz][49:52])
				primera_fila.append(ubicacion[aux_uz][53:57])
				primera_fila.append(ubicacion[aux_uz][59:63])
				primera_fila.append(ubicacion[aux_uz][64:68])
				primera_fila.append(ubicacion[aux_uz][69:72])
				primera_fila.append(ubicacion[aux_uz][74:76])
				segunda_fila.append(seq)
				year_salve=int(ubicacion[aux_uz][83:87])
				year_salve=year_salve+100
				#print year_salve, '---', seq
				segunda_fila.append(str(year_salve))
				#segunda_fila.append(ubicacion[aux_uz][83:87])
				#segunda_fila.append(ubicacion[aux_uz][88:100])
				segunda_fila.append(ubicacion[aux_uz][88:93])
				#segunda_fila.append(ubicacion[aux_uz][104:111])
				segunda_fila.append(arreglo_ptr[pt_index][0][13:23])
				#segunda_fila.append(ubicacion[aux_uz][113:120])
				segunda_fila.append(arreglo_ptr[pt_index][0][24:34])
				segunda_fila.append(arreglo_ptr[pt_index][0][35:45])
				segunda_fila.append(ubicacion[aux_uz][121:126])
				
				segunda_fila.append(ubicacion[aux_uz][126:133])

				segunda_fila.append(ubicacion[aux_uz][133:139])
				segunda_fila.append(ubicacion[aux_uz][139:142])
				segunda_fila.append(round(float(ubicacion[aux_uz][142:147])))
				segunda_fila.append(round(float(ubicacion[aux_uz][147:151])))
				print segunda_fila
				#guarda_model='/home/carlos/Dropbox/Catalogo_2006_2007/'+model+'.txt'
				#Tipo="Path for salve results of the system"
				#inicio_ruta_dir=Rutas_Dir()
				#path_finish=inicio_ruta_dir.pathfile(Tipo)
				guarda_model=self.path_finish+'/'+model+'.txt'
				print guarda_model
				fo = open(guarda_model, 'a')
				if seq==0:
					for i in primera_fila:
						fo.write(str(i)+ '\t')
					fo.write( '\n')
					for i in segunda_fila:
						fo.write(str(i)+'\t')
					fo.write( '\n')

				else:
					for i in segunda_fila:
						fo.write(str(i) +'\t')
					fo.write( '\n')
			
			
	

#inicio=hyp_path()
#inicio.main()

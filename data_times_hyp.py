import os.path
import os.path
import subprocess
import glob
from Lectura_file import *
from Correlacion import *
from Rutas import *
from Rutas_Dir import *
from tkinter import *
import tkFileDialog
import tkinter as tk
from file_hypodd import *

class data_times_hyp():


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
		messagebox.showinfo(message="process completed successfully", title="Message")
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

		

#inicio =data_times_hyp()
#opc=1
#model="codex_17"
#inicio.main(model, opc)
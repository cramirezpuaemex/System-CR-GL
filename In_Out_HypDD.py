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

class In_Out_HypDD():
	def main(self, model, opc):
		#model='codex_16'


		print "Bienvenidos al Software file input and out file HypoDD con python"

		print "Ingresa el nombre del modelo a ser analizado:"
		#model=""
		#model=raw_input()
		print type(model)
		archivos_origen=self.origen(model)
		print "****orig"
		archivos_origen.pop(0)
		#for i in archivos_origen:
			#print i
		archivos_pick=self.Lec_files()

		#archivos_origen=self.origen(model)
		#print "****origen"
		#archivos_pick=self.Read_files()

		print "****read"
		
		
		#print len(archivos_pick)
		#print len(archivos_cross)
		print "Nombre del modelo:  ", model


		#resp="y"
		#while resp == "Y" or resp == "y" or resp == "yes" or resp== "YES":
			#print "Selecciona la opcion que deseas realizar"

			#print "1.- proceso para generar datos_times"
			#print "2.- Proceso para generar dt.ct"
			#print "3.- Proceso para generar dt.cc"
			
			#opc=input("Selecciona opcion: " )

		if opc ==1:
			for i in range(len(archivos_origen)):
				idece_analizar=int(archivos_origen[i][0])
				self.Proceso(archivos_pick[idece_analizar], archivos_origen[i], model )
			print "************************"
			print "Fin de proceso uno"
			print "************************"				
			#resp=raw_input("Deseas realizar otra proceso (Yes), ingresa cualquier valor y enter para terminar:  ")

		elif opc ==2:
				
			archivos_cross=self.Read_files_cross()
			print "****cross"
			archivos_times=self.Read_files_times(model)
			print "****times"

					
			print "7.-Utilizando RMS average"
			print "8.-Utilizando Cross correlation"
			print "9.-Utilizando Quality signal"


			process =0
			while process == 0:
				process=input("Proceso a realizar:  ")
				print type(process)
				if process == 7 or process == 8 or process == 9:
					break
				else:
					process=input("Opcion incorrecta, ingresa la opcion correcta:  ")





			print "************************"
			print "Inicio de proceso dos"
			print "**********************"
			for i in range(len(archivos_times)):
				print "id", i
				print "file", archivos_times[i]
				self.Proceso_dos(archivos_times[i],i, archivos_times, model, process)

			resp=raw_input("Deseas realizar otra proceso (Yes), ingresa cualquier valor y enter para terminar:  ")

			
		elif opc ==3: 
			print "Nota: para esta seccion se tienbe que crear primero el dt_cross.ct, opcion 2 del menu principal"
			res=input("cuentas con archivo? 1: para contunuar. 2: Para regresar al menu principal")

			if res ==1:
				file="/home/carlos/Escritorio/"+model+"/dt_cross.ct"
				datos=self.lectura_cross(file)
				fo = open('/home/carlos/Escritorio/'+model+'/dt.cc', 'a')
				for i in range(len(datos)):
					#print datos[i]
					#print datos[i][0]
					if datos[i][0]=="#":
						aux=[]
						for j in range(len(datos[i])):
							if datos[i][j]!="":
								aux.append(datos[i][j])
						#print "aux", aux		
						fo.write(aux[0]+"\t\t"+aux[1] +"\t\t"+aux[2]+"\t\t0\n")
					else:
						aux=[]
						for j in range(len(datos[i])):
							if datos[i][j]!="":
								aux.append(datos[i][j])
						#print "aux", aux

						a = float(aux[1])
						b = float(aux[2])
						resultado= a-b
						fo.write(aux[0] +"\t\t"+str(resultado)+"\t\t"+aux[3]+"\t"+aux[4]+"\n")
			else:
				print "Selecciona la opcion 2 del menu principal"				

		else:
			print "Opcion incorrecta, ingresa la opcion correcta"





		#self.model='codex_17'
			
		#self.create_file()
		#elf.Software_hypoDD()
		print "Termina Programa"
		

		
		#self.cont=0
		'''
		print 	archivos_origen[0]
		for i in range(len(archivos_origen)):
			if i!=0:
				indicador=int(archivos_origen[i][0])
				print "id", indicador
				print archivos_pick[indicador]
				print archivos_cross[indicador]
				#self.Compara( indicador, archivos_pick, archivos_cross)
		'''		
		

		'''

		print archivos_pick[475]
		'''


	def main_pregunta(self, b):
		if b==0:
			self.a=[]
			self.pregunta()
		else:
			print self.a
			return self.a

	def Pregunta_yes(self):
	    inicio=Rutas_Dir()
	    self.root3.destroy()
	    Tipo="Path Directory whit files phases"
	    #Tk().withdraw()
	    file=inicio.pathfile(Tipo)
	    #borrar()
	    self.a.append(file)


	def Pregunta_not(self):
	    self.root3.destroy()
	    b=1
	    self.main_pregunta(b)


	def pregunta(self):

		a=[]
		self.root3 = Tk()
		self.root3.config(bd=25)
		T = Text(self.root3,  height = 1, width = 30)
		n1 = StringVar()
		n2 = StringVar()
		r = StringVar()
		Fact = """Select directory with files"""

		T.pack()
		Button(self.root3, text="yes", command=self.Pregunta_yes).pack(side="left")
		#Button(root, text="Resta", command=resta).pack(side="left")
		Button(self.root3, text="Not", command=self.Pregunta_not).pack(side="right")

		T.insert(tk.END, Fact)
		self.root3.mainloop()

	def Lec_files(self):
		pregunta_b=0
		self.main_pregunta(pregunta_b)

		files_all=self.a
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
			
		return path_archivos


	def lectura_cross(self, path):	
		f = open(path,"r")
		arreglo= []
		contLin=0
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(',')
				datos =datos[0].split(' ')
				arreglo.append(datos)
			else:
				break

		return arreglo	
		
	def Read_files_cross(self):
		files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/2006/','/home/carlos/Dropbox/Catalogo_2006_2007/2007/']
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
			
		return path_archivos

	def Read_files_times(self, model):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		files_all='/home/carlos/Escritorio/datos_time/'+model+'/'
		#print len(files_all)
		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/']
		#file='/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/'
		
		#archivos=[]

		archivos=os.listdir(files_all)
		f=[]
		for i in archivos:
			idei=i.find('id_')
			idef=i.find('.txt')
			print i[idei+3:idef]#
			f.append(int(i[idei+3:idef]))
		f.sort()
		print f
		path_archivos=[]
		for i in f:
			path_archivos.append("/home/carlos/Escritorio/datos_time/"+model+"/id_"+str(i)+".txt")
		#archivos=sorted(archivos)
		#archivos.sort()
		
			

		print "len archivos", len(archivos)
		return path_archivos
	def Compara(self, i, files, cross):
		print "id",i
		compa1=files[i][len(files[i])-13:len(files[i])-4]
		print compa1
		compa2=cross[i][len(cross[i])-9:len(cross[i])]
		print compa2
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

	def Read_files(self):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/','/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2007/']
		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/']
		#file='/home/carlos/Dropbox/Catalogo_2006_2007/Phases_2006/'
		seq=0
		path_archivos=[]
		for fi in files_all:
			file=fi
			archivos=os.listdir(file)
			archivos=sorted(archivos)
			#print 'Archivos: \n', archivos
		
			
			for arh in range(len(archivos)):
				i=archivos[arh]
				aux=file+i
				#if arh == 13:
				path_archivos.append(aux)
				#print aux
				#self.Proceso(aux)


		return path_archivos

		######################################################
	def Proceso(self, i, origen, model):
		#funcion para las nuevas modificaciones
		#def Proceso(self, path, origen, model):
		print "Ingresa al proceso Data times"
		#print path
		print origen
		print model
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
			inicio_rutas_dir=Rutas_Dir()
			Tipo="Input path to salve files times"
			path_salve=inicio_rutas_dir.pathfile()
			path_salve=path_salve+'/datos_time/'+model+'/'
			if not os.path.exists(path_salve):
				os.makedirs(path_salve)
			
			#fo = open('/home/carlos/Escritorio/datos_time/'+model+'/id_'+origen[0]+'.txt', 'a')
			fo = open(path_salve+'id_'+origen[0]+'.txt', 'a')
			if result_seg < 30 and float(origen[7]) < 2:
				time=result_seg+result_cen
				print a[0][0:4], time, origen[7], 'P'
				fo.write(str(a[0][0:4])+'   '+str(time)+'\t'+str(origen[7])+'\n')

		


				
	def Read_cross(self, path):		
		path_archivos=[]
		path=path+"/"
		archivos=os.listdir(path)
		archivos=sorted(archivos)
		for i in archivos:
			if i.find("HHZ")!= -1:
				path_archivos.append(i)

		return path_archivos
		######################################################

	def Software_SAC(self, ruta_cross1, ruta_cross2):

		print "Entra a la funcion de Software"
		#print "RT1", ruta_cross1
		#print "RT2", ruta_cross2

		p = subprocess.Popen(['sac'],
                     			stdout = subprocess.PIPE,
                     			stdin  = subprocess.PIPE,
                     			stderr = subprocess.STDOUT )

			
		s=''
		line1="r "+ruta_cross1+"\n"
		s+=line1
		line1='apk\n'
		s+=line1
		line1="r "+ruta_cross2+"\n"
		s+=line1
		line1='apk\n'
		s+=line1
		line1="q"
		s+=line1
		#print s	

		out = p.communicate( s )
		#print out[0]
		b= out[0].split('\n')

		#for i in range(len(b)):
			#print i, b[i]
		#a=out[0]

		cali1=b[3]
		cali2=b[4]

		#for i in range(len(cali1)):
			#print i, cali1[i]

		if cali1.find("WARNING:")==-1:
			cali1=cali1[8]
		else:
			cali1 = 4
		if cali2.find("WARNING:")==-1:
			cali2=cali2[8]
		else:
			cali2 = 4


		
		'''
		ind1=a.find("California")
		ind2=a.find("SAC Error: EOF/Quit")
		

		#print out[0][ind1+7: ind2]
		calidad1=out[0][ind1+20:ind2-41]
		calidad2=out[0][ind1+46:ind2-15]
		'''
		print "************"
		print "resultados de Software_SAC"
		print cali1
		print cali2
		print "***********"
		aux=[]
		aux.append(cali1)
		aux.append(cali2)
		#aux.append(wr)
		
		return aux
	def Proceso_dos(self, i, j, archivos, model, process):
		print "inicia cross"
		print "i", j
		print "/////////////////////////////////////////"
		print i
		inicio_read_file=Lectura_file()
		arreglo=[]
		arreglo=inicio_read_file.main(i)
		
		files_xcross=[]
		files_xcross=self.Read_files_cross()
		#for x in arreglo:
			#print x

		j=j+1
		for a in range(j,len(archivos)):

			print archivos[a]
			print "*****************+++++++++++++++++++"
			arreglo1=inicio_read_file.main(archivos[a])
			vector=[]
			identifica=[]
			for x in arreglo:
				estacion=x[0][0:4]
				#print "estacion", estacion
				for y in arreglo1:
					aux=[]
					aux_id=[]
					if y[0].find(estacion)==0:
						aux.append(x[0])
						aux.append(y[0])
						vector.append(aux)
						aux_id.append(i)
						aux_id.append(archivos[a])
						identifica.append(aux_id)

			#print "vector", vector
			#print "identifica", identifica
			if len(vector) > 0:
				path_salve_ct='/home/carlos/Escritorio/'+model+'/'
				if not os.path.exists(path_salve_ct):
					os.makedirs(path_salve_ct)
				if process == 7:
					fo = open('/home/carlos/Escritorio/'+model+'/dt.ct_prom', 'a')
				elif process == 8:
					fo = open('/home/carlos/Escritorio/'+model+'/dt.ct_cross', 'a')
				else:
					fo = open('/home/carlos/Escritorio/'+model+'/dt.ct_new', 'a')
				ide=i.find('id_')
				identificador1=i[ide+3:len(i)-4]
				ide=archivos[a].find('id_')
				identificador2=archivos[a][ide+3:len(archivos[a])-4]
				print '#     ',identificador1, '     ', identificador2
				#print "path01", files_xcross[int(identificador1)]
				#print "path02", files_xcross[int(identificador2)]
				fo.write('#     '+identificador1+'     '+identificador2+'\n')
				cross01=[]
				cross02=[]
				cross01=self.Read_cross(files_xcross[int(identificador1)])
				cross02=self.Read_cross(files_xcross[int(identificador2)])
				for x in vector:
					datos1=x[0].split(' ')
					datos2=x[1].split(' ')
					#print "datos1", datos1, "datos2", datos2
					for xc in cross01:
						if xc.find(datos1[0])!= -1:
							ruta_cross1=files_xcross[int(identificador1)]+"/"+xc
							break
					for xc in cross02:
						if xc.find(datos1[0])!= -1:
							ruta_cross2=files_xcross[int(identificador2)]+"/"+xc
							break
					time1=datos1[3].replace('\t', '')
					if len(time1) <5:
						restantes=5-len(time1)
						for r in range(restantes):
							time1=time1+'0'
						time1=' '+time1
					else:
						time1=time1+'0'
					
#
					time2=datos2[3].replace('\t', '')
					if len(time2) <5:
						restantes=5-len(time2)
						for r in range(restantes):
							time2=time2+'0'
						time2=' '+time2
					else:
						time2=time2+'0'

					if process == 7:

						# Seccion que realiza el archivo dt.ct utilizando el Error de localizacion
						prom=abs(((float(datos1[4])+float(datos2[4]))/2)-1)
						prom=str(prom)
						if len(prom) <6:
							restantes=6-len(prom)
							for r in range(restantes):
								prom=prom+'0'
					elif process == 8:
						# Seccion que utiliza Archivos ccon correlacion cruzada
						iniciar_xcross=Correlacion()
						correlacion=iniciar_xcross.main(ruta_cross1, ruta_cross2)
						correlacion=round(correlacion, 4)
						prom=str(correlacion)
					else:

						#Seccion que utiliza la calidad de la signal
						datos_new= self.Software_SAC(ruta_cross1, ruta_cross2)
					
						calidad1=float(datos_new[0])
						calidad2=float(datos_new[1])

						prom = (calidad1+ calidad2)/2

	
						if prom >=0 and prom <1:
							valor = "1.00"
						elif prom >=1 and prom <2:
							valor ="0.75"
						elif prom >=2 and prom <3:
							valor = "0.50"
						elif prom >=3 and prom <4:
							valor ="0.25"
						else:
							valor="0.00"
						print "VALOR: ", valor
						prom=str(valor)

					
					#print "correlacion es: ", correlacion
					print "correlacion entre", ruta_cross1, "y", ruta_cross2
					print datos1[0], '\t', time1, '\t', time2, '\t', prom,'p'
					fo.write(datos1[0]+'     '+time1+'   '+time2+' '+(prom)+' P\n')







#inicio_grupos=ct()
#inicio_grupos.main()

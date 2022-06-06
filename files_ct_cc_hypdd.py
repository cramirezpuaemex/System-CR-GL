from Rutas_Dir import *
import tkinter as tk
from tkinter import ttk
from Tkinter import *
from Lectura_file import *
from tkinter import messagebox
class files_ct_cc_hypdd():

	def main_files_ct(self, model):
		#archivos_cross=self.Read_files_cross()
		#print "****cross"
		print "bienvenido a crear archivos dt.ct"
		archivos_times=self.Read_files_times(model)
		print "****times"

					
		print "7.-Utilizando RMS average"
		print "8.-Utilizando Cross correlation"
		print "9.-Utilizando Quality signal"
		self.menu_ct()

		




		print "************************"
		print "Inicio de proceso dos"
		print "**********************"

		process=self.opcion
		inicio_rutas_dir=Rutas_Dir()
		Tipo="Path salve files dt.ct"
		path_salve_ct=inicio_rutas_dir.pathfile(Tipo)
		files_xcross=[]
		self.a=[]
		self.menu_cross_file()
		
		files_xcross=self.Read_files_cross(self.a)
		for i in range(len(archivos_times)):
			print "id", i
			print "file", archivos_times[i]
			self.Proceso_dos(archivos_times[i],i, archivos_times, model, process, path_salve_ct,files_xcross)
		#messagebox.showinfo(message="process completed successfully", title="Message")
		self.menu_ct()
		print "************************"
		print "Fin de proceso dos"
		print "**********************"

	def Read_files_times(self, model):
		#Tk().withdraw()
		#file=filedialog.askdirectory()
		inicio_rutas_dir=Rutas_Dir()
		Tipo="Select path with files data times"
		files_all_aux=inicio_rutas_dir.pathfile(Tipo)
		files_all=files_all_aux+'/'
		#files_all='/home/carlos/Escritorio/datos_time/'+model+'/'
		#print (files_all)
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
			#path_archivos.append("/home/carlos/Escritorio/datos_time/"+model+"/id_"+str(i)+".txt")
			path_archivos.append(files_all+"id_"+str(i)+".txt")

		for i in path_archivos:
			print i
		#archivos=sorted(archivos)
		#archivos.sort()
		return path_archivos
		
	def settings_ct(self, opc):
		self.opcion=opc
		print self.opcion
		self.root6.destroy()
	def salir(self):
		#self.root = tk.Tk()
		print "salir"
		self.root6.destroy()
	def salir_cross(self):
		#self.root = tk.Tk()
		print "salir"
		self.root5.destroy()
	def menu_ct(self):
		self.root6 = Tk()
		self.root6.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root6.title(" Input name to identifier")
		#INPUT=""     

		 
		self.Display = Button(self.root6, height = 2,
		                 width = 40,
		                 text ="Using RMS average",
		                 command = lambda:self.settings_ct(opc=7))

		self.Display2 = Button(self.root6, height = 2,
		                 width = 40,
		                 text ="Using Cross correlation",
		                 command = lambda:self.settings_ct(opc=8))
		self.Display3 = Button(self.root6, height = 2,
		                 width = 40,
		                 text ="Using Quality signal",
		                 command = lambda:self.settings_ct(opc=9))		

		self.Display8 = Button(self.root6, height = 2,
		                 width = 20,
		                 text ="Quit",
		                 command = lambda:self.salir())

		#self.inputtxt.pack()
		self.Display.pack()
		
		self.Display2.pack()
		self.Display3.pack()
		
		self.Display8.pack()
		mainloop()

	def Pregunta_yes(self):
	    inicio_rutas_dir=Rutas_Dir()
	    self.root5.destroy()
	    Tipo="Path Directory whit files phases"
	    #Tk().withdraw()
	    file=inicio_rutas_dir.pathfile(Tipo)
	    print "file", file
	    #borrar()
	    self.a.append(file+'/')
	    print self.a
	    
	    self.menu_cross_file()

	def menu_cross_file(self):
		self.root5 = Tk()
		self.root5.geometry("400x200")
		#self.root.config(width=300, height=100)
		self.root5.title(" Select path catalogs of event seismic .SAC")
		#INPUT=""     

		 
		self.Display = Button(self.root5, height = 2,
		                 width = 40,
		                 text ="yes",
		                 command = lambda:self.Pregunta_yes())

	

		self.Display8 = Button(self.root5, height = 2,
		                 width = 20,
		                 text ="not",
		                 command = lambda:self.salir_cross())

		#self.inputtxt.pack()
		self.Display.pack()
		
		self.Display8.pack()
		mainloop()

	def Read_files_cross(self, files_all):
		
		print "files_all", files_all
		#files_all=['/home/carlos/Dropbox/Catalogo_2006_2007/2006/','/home/carlos/Dropbox/Catalogo_2006_2007/2007/']
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

	def Proceso_dos(self, i, j, archivos, model, process, path_salve_ct, files_xcross):
		print "inicia cross"
		print "i", j
		print "/////////////////////////////////////////"
		print i
		inicio_read_file=Lectura_file()
		arreglo=[]
		arreglo=inicio_read_file.main(i)
		
		
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
				#path_salve_ct='/home/carlos/Escritorio/'+model+'/'
				#path_salve_ct='/home/carlos/Escritorio/'+model+'/'
				if not os.path.exists(path_salve_ct):
					os.makedirs(path_salve_ct)
				if process == 7:
					fo = open(path_salve_ct+'/'+model+'_dt.ct_prom', 'a')
				elif process == 8:
					fo = open(path_salve_ct+'/'+model+'_dt.ct_cross', 'a')
				else:
					fo = open(path_salve_ct+'/'+model+'_dt.ct_new', 'a')
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
		


#inicio_files_ct=files_ct_cc_hypdd()
#model="codex_17"
#inicio_files_ct.main_files_ct(model)
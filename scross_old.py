


#====================Librerias===================================================
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import math
import obspy
from scipy.signal import butter, lfilter
from Generar_Nombre import *
from time import time 
import time
import os
from obspy.core import UTCDateTime
#importa las clases
from Diezmado import *
from Procedimiento import*
from Genera_archivos import *
from Comprobar_Resultados import *
from PickerSAC import *
class scross:




	def main(self, path1, path2, ruta_guardar_resultados):
		#==========================Lectura de archivos===================================
		#tiempo_inicial = time()
		print time.strftime("%H:%M:%S")
		valor=20
		print 'dia', path1
		print 'catalogo', path2
		#path1= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.038.00.34/2006.038.00.34.ZA.COMA.HHZ.SAC"
		#path1='/home/carlos/Escritorio/CODEX_2006/036/ZA.ZAPO..HHZ.M.2006.036.000000.SAC'
		#path1="/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/P_Windows/2006.036.10.57.ZA.MAZE.HHZ.SAC"
		st1=obspy.read(path1)
		#print(st1[0].stats)
		self.senal01=st1[0].data
		
		#print ' tamano original', len(self.senal01)
		inicia_diezmado=Diezmado()
		#s1=inicia_diezmado.proceso(self.senal01, valor)
		#print ' tamano final', len(s1)


	
		
		#path2= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/P_Windows/2006.036.10.57.ZA.MAZE.HHZ.SAC"
		#path2= "/home/carlos/Escritorio/Catalogo_CODEX_2006/2006.036.10.57/2006.036.10.57.ZA.ZAPO.HHZ.SAC"	
		
		st2=obspy.read(path2)
		#print(st1[0].stats)
		self.senal02=st2[0].data
		
		
		
		#print ' tamano original', len(self.senal02)
		#s2=inicia_diezmado.proceso(self.senal02, valor)
		#print ' tamano final', len(s2)
		
		

		

		#==================nueva seccion=======================
		inicia_proceso = Procedimiento()
		# regresa dos arreglos, el primero que contiene los valores maximos de correlacion y el segundo los indices donde se encontro la maxima correlacion
		valores= inicia_proceso.proceso(inicia_diezmado.proceso(self.senal01, valor), inicia_diezmado.proceso(self.senal02, valor), valor)

		print time.strftime("%H:%M:%S")
		#print '*******************************************************'
		#print 'tiempo de ejecucion: ', tiempo_ejecucion



		#*************************************************************************************************
		#*************************************************************************************************
		v_max=valores[0]
		v_indice= valores[1]

		for i in range(len(v_max)):
			#print 'valores maximo de correlacion', v_max[i]
			#print 'indice donde encuentra la maxima correlacion', v_indice[i]*4

			# Indice Inicio de la ventana donde se encontro un posible candidato (indice_inicio_resp)
			indice_inicio_resp= v_indice[i]*4
			#Calcula la hora de la ventana del posible evento
			time_h=int(int(int((indice_inicio_resp)/100)/60)/60)
			#Calcula la minutos de la ventana del posible evento
			time_m=int(int(int((indice_inicio_resp)/100)/60)%60)
			#Calcula la minutos de la ventana del posible evento
			time_s=int(int((indice_inicio_resp)/100)%60)
			
			#*************************************************************************************************
			#*************************************************************************************************

			#se verifica que tenga datos suficientes al inicio del dia (10 segundos antes o 1000 ntps antes)
			if indice_inicio_resp-1000>=0:
				indice_fin_resp=(indice_inicio_resp)+len(self.senal02)
				st_datos_resp=self.senal01[indice_inicio_resp-1000: (indice_inicio_resp)+len(self.senal02)]

				st1[0].data=st_datos_resp
				st1[0].stats.sac.nzhour=time_h
				st1[0].stats.sac.nzmin=time_m
				st1[0].stats.sac.nzsec=time_s
				st1[0].stats.sac.npts=len(st1[0].data)
				date= st1[0].stats.starttime
				year_time=date.year
				month_time=date.month
				day_time=date.day
				time_inicio=UTCDateTime(year_time, month_time, day_time, time_h, time_m, time_s, 10000)
				# Indice termino de la ventana donde se encontro un posible candidato (indice_fin_resp)
				indice_fin_resp=(indice_inicio_resp)+len(self.senal02)
				#Calcula la hora de la ventana del posible evento
				time_h_fin=int(int(int((indice_fin_resp)/100)/60)/60)
				#Calcula la minutos de la ventana del posible evento
				time_m_fin=int(int(int((indice_fin_resp)/100)/60)%60)
				#Calcula la minutos de la ventana del posible evento
				time_s_fin=int(int((indice_fin_resp)/100)%60)
				time_final=UTCDateTime(year_time, month_time, day_time, time_h_fin, time_m_fin, time_s_fin, 10000)

				
				# Asigna tiempos a la ventana candidata formato  SAC
				st1[0].stats.starttime=time_inicio
				#st1[0].stats.endtime=time_final
				#*************************************************************************************************
				#*************************************************************************************************

				inicio_genera=Generar_Nombre()
				
				#ruta=inicio_genera.main(path1, str(time_h), str(time_m), str(time_s))
				nombre_guardar=inicio_genera.main(path1, str(time_h), str(time_m), str(time_s))
				Inicia_guardar_archivos=Genera_archivos()

				#++++++++++++++++++++++++++++++++++++++++++++++++++





				#++++++++++++++++++++++++++++++++++++++++++++++++++
				#print nombre_guardar
				#================== Genera un sismograma en formato SAC para su posterior analisis ============================================
				st1.write(ruta_guardar_resultados+'/'+nombre_guardar, format='SAC')				
				nombre_final=ruta_guardar_resultados+'/'+nombre_guardar
				#print nombre_final
				#=========================== Inicia la creacion de la clase para la busqueda de la onda P =====================================
				iniciaPicker=PickerSAC()
				#=========================== Termina la creacion de la clase para la busqueda de la onda P =====================================
				#=========================== Comienza el analisis de la onda P =================================================================
				opc=-2
				respuesta_picker=iniciaPicker.main(nombre_final, opc)
				#print respuesta_picker
				if respuesta_picker != -1:
					print '********************************************************************'
					print '********************************************************************'
					print nombre_guardar
						


					##opcion=0 para guardar los datos en archivo txt y  regresa el dia en el que se encontro
					#opcion=0
					#Inicia_guardar_archivos.crea_nombre(path1, path2, ruta_guardar_resultados, nombre_guardar,indice_inicio_resp-1000, (indice_inicio_resp)+len(self.senal02), v_max[i], opcion, respuesta_picker)
					
					#========================= Verifica formato de hora ======================================
					if len(str(time_h))==1:
						c_hora='0'+str(time_h)
					else:
						c_hora=str(time_h)


					#======================== Verifica  year de analisis ========================================

					if path1.find('2006')!=-1:
						
						year='2006'
						path1_dia=path1.find('2006')
						#======================== Verifica formato de dia ========================================
						c_dia=path1[path1_dia+5:path1_dia+8]
						if len(str(c_dia))==1:
							c_dia='0'+str(c_dia)
						else:
							c_dia=str(c_dia)
					elif path1.find('2007')!=-1:
						year='2007'
						path1_dia=path1.find('2007')
						#======================== Verifica formato de dia ========================================
						c_dia=path1[path1_dia+5:path1_dia+8]
						if len(str(c_dia))==1:
							c_dia='0'+str(c_dia)
						else:
							c_dia=str(c_dia)												
					else:
						year='2008'
						#======================== Verifica formato de dia ========================================
						path1_dia=path1.find('2008')
						c_dia=path1[path1_dia+5:path1_dia+8]
						if len(str(c_dia))==1:
							c_dia='0'+str(c_dia)
						else:
							c_dia=str(c_dia)

					##print 'tipo de variable c_dia', type(c_dia)
					#*************************************************************************************************
					#*************************************************************************************************

					# Genera los canales HHE, HHN

					busqueda_hhz=path1.find('HHZ')
					path_HHE=path1[0:busqueda_hhz]+'HHE'+path1[busqueda_hhz+3:len(path1)]
					path_HHN=path1[0:busqueda_hhz]+'HHN'+path1[busqueda_hhz+3:len(path1)]
					#print 'HHE', path_HHE
					#print 'HHN', path_HHN
					stE=obspy.read(path_HHE)
					stN=obspy.read(path_HHN)
					self.senalE=stE[0].data
					self.senalN=stN[0].data


					# Se generar los nuevos intervalos de datos
					stE_new=self.senalE[indice_inicio_resp-1000: (indice_inicio_resp)+len(self.senal02)]
					stN_new=self.senalN[indice_inicio_resp-1000: (indice_inicio_resp)+len(self.senal02)]
					#Se asiganan los nuevos intervalos de datos HHE
					stE[0].data=stE_new
					stE[0].stats.sac.nzhour=time_h
					stE[0].stats.sac.nzmin=time_m
					stE[0].stats.sac.nzsec=time_s
					stE[0].stats.starttime=time_inicio
					#stE[0].stats.endtime=time_final
					stE[0].stats.sac.npts=len(stE[0].data)


					# Asigna tiempos a la ventana candidata formato  SAC canal HHN
					stN[0].data=stN_new
					stN[0].stats.sac.nzhour=time_h
					stN[0].stats.sac.nzmin=time_m
					stN[0].stats.sac.nzsec=time_s
					stN[0].stats.sac.npts=len(stN[0].data)
					stN[0].stats.starttime=time_inicio
					#stN[0].stats.endtime=time_final
					stN[0].stats.sac.npts=len(stN[0].data)

					Busqueda_nombreGuardar=nombre_guardar.find('HHZ')
					nombre_guardar_E=nombre_guardar[0:Busqueda_nombreGuardar]+'HHE'+nombre_guardar[Busqueda_nombreGuardar+3:len(nombre_guardar)]
					nombre_guardar_N=nombre_guardar[0:Busqueda_nombreGuardar]+'HHN'+nombre_guardar[Busqueda_nombreGuardar+3:len(nombre_guardar)]



					#============================ Crea ruta donde se guardaran los resultados del analisis ============================================
					#print '+++++++++++++++++++++++'
					#print 'c_dia', c_dia
					#print '+++++++++++++++++++++++'
					path_salve_dia=ruta_guardar_resultados+'/'+c_dia
					if not os.path.exists(path_salve_dia):
						os.makedirs(path_salve_dia)

					#nombre_path_resultados=ruta_guardar_resultados+'/'+year+'.'+c_dia+'.'+c_hora
					nombre_path_resultados=path_salve_dia+'/'+year+'.'+c_dia+'.'+c_hora
					#print nombre_path_resultados
					# Verifica si la carpeta existe para guardar resultados, en otro caso genera l carpeta											
					

					if not os.path.exists(nombre_path_resultados):
						os.makedirs(nombre_path_resultados)
						st1.write(nombre_path_resultados+'/'+nombre_guardar, format='SAC')
						stE.write(nombre_path_resultados+'/'+nombre_guardar_E, format='SAC')
						stN.write(nombre_path_resultados+'/'+nombre_guardar_N, format='SAC')						
					else:
						st1.write(nombre_path_resultados+'/'+nombre_guardar, format='SAC')
						stE.write(nombre_path_resultados+'/'+nombre_guardar_E, format='SAC')
						stN.write(nombre_path_resultados+'/'+nombre_guardar_N, format='SAC')
					
					nombre_final=nombre_path_resultados+'/'+nombre_guardar_E
					opc=0	
					respuesta_picker_E=iniciaPicker.main(nombre_final, opc)
					#print respuesta_picker_E
					nombre_final=nombre_path_resultados+'/'+nombre_guardar_N	
					respuesta_picker_N=iniciaPicker.main(nombre_final, opc)
					#print respuesta_picker_N					
					#opcion=0 para guardar los datos en archivo txt y  regresa el dia en el que se encontro
					opcion=0
					Inicia_guardar_archivos.crea_nombre(path1, path2, path_salve_dia, nombre_guardar,indice_inicio_resp-1000, (indice_inicio_resp)+len(self.senal02), v_max[i], opcion, respuesta_picker,respuesta_picker_E, respuesta_picker_N )	
					#Inicia_guardar_archivos.crea_nombre(path1, path2, ruta_guardar_resultados, nombre_guardar,indice_inicio_resp-1000, (indice_inicio_resp)+len(self.senal02), v_max[i], opcion, respuesta_picker,respuesta_picker_E, respuesta_picker_N )	

					print '********************************************************************'
					print '********************************************************************'
					#Inicia_guardar_archivos.crea_nombre(path1, path2, ruta_guardar_resultados, nombre_guardar,indice_fin-3000, (indice_fin)+len(self.senal02), v_max[i], opcion, respuesta_picker)
			#se comentara provicionalmente realizado el dia 18/07/19
			'''
			Inicia_comprobar=Comprobar_Resultados()
			
			comprueba=Inicia_comprobar.trabaja_comprobar(self.senal01[(v_indice[i]*4)-len(self.senal02):(v_indice[i]*4)+(len(self.senal02)*2)], self.senal02)
			#print 'comprueba', comprueba
			#print 'comprueba[0][0]', comprueba[0][0]
			#print 'comprueba[0][1]', comprueba[0][1]
			if comprueba[0][0] != -1:
				print '************* valores maximo de correlacion                *************', comprueba[0][0]
				indice_fin=((v_indice[i]*4)-len(self.senal02))+comprueba[0][1]
				print '************* indice donde encuentra la maxima correlacion *************', ((v_indice[i]*4)-len(self.senal02))+comprueba[0][1]
				time_h=int(int(int((indice_fin)/100)/60)/60)
				time_m=int(int(int((indice_fin)/100)/60)%60)
				#time_h=int(int(int((v_indice[i]*4)/100)/60)/60)
				#time_m=int(int(int((v_indice[i]*4)/100)/60)%60)
				if time_m>0:
					time_s=time_m%60
				else:
					time_s=0

				#st=self.senal01[v_indice[i]*4: (v_indice[i]*4)+len(self.senal02)]
				st=self.senal01[indice_fin: (indice_fin)+len(self.senal02)]
			

				st1[0].data=st
				inicio_genera=Generar_Nombre()
				#ruta=inicio_genera.main(path1, str(time_h), str(time_m), str(time_s))
				nombre_guardar=inicio_genera.main(path1, str(time_h), str(time_m), str(time_s))
				Inicia_guardar_archivos=Genera_archivos()
				aux_nombre=Inicia_guardar_archivos.escribe_archivos(path1, path2, ruta_guardar_resultados, nombre_guardar, ((v_indice[i]*4)-len(self.senal02))+comprueba[0][1], len(self.senal02), comprueba[0][0])
				nombre_guardar=aux_nombre+nombre_guardar
				print nombre_guardar
				st1.write(ruta_guardar_resultados+'/'+nombre_guardar, format='SAC')
			'''
		#print (':)')
				#plt.figure(i+1)
				#plt.subplot(2,1,1)
				#plt.plot(self.senal02)
				#plt.subplot(2,1,2)
				#f=[self.senal01[i] for i in range(v_indice[i]*4, (v_indice[i]*4)+len(self.senal02))]
				#plt.plot(f)
				#
		#plt.show()
		#print 'fin'



#iniciar=scross()
#iniciar.main()
	
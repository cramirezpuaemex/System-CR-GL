import subprocess
import glob
from Pos_Cut_Sac import *
from Pos_archivos import *
import os

class Buscar_picker():
	def main(self, indicei, indicef, dia_a):
		#indicei='41509'
		#indicef='41624'
		estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']

		dia=[dia_a]
		#aa=indicei
		#ba=indicef
		opc=-2
		time_arrive=[]
		names=[]
		ruta_Z=[]
		ruta_N=[]
		ruta_E=[]
		for j in range(len(dia)):
	
			for i in range(len(estaciones)):

				p = subprocess.Popen(['sac'],
								stdout = subprocess.PIPE,
    							stdin  = subprocess.PIPE,
    							stderr = subprocess.STDOUT)
				s=''
				#aux_file='/home/carlos/Escritorio/CODEX_2006/'
				aux_file='/media/carlos/Disk_CRP/CODEX/'
				path1=aux_file+dia[j]+'/ZA.'+estaciones[i]+'..HHZ.M.2007.'+dia[j]+'.000000.SAC'
				print path1
				pathE=aux_file+dia[j]+'/ZA.'+estaciones[i]+'..HHE.M.2007.'+dia[j]+'.000000.SAC'
				pathN=aux_file+dia[j]+'/ZA.'+estaciones[i]+'..HHN.M.2007.'+dia[j]+'.000000.SAC'
				s = "echo on\n"
				line1='read '+path1+'\n'
				line2='cut '+str(indicei)+' '+str(indicef)+'\n'
				line3='read\n'
				line4='apk\n'
				s+=line1
				s+=line2
				s+=line3
				s+=line4

				s += "quit()\n"

				#print '========================================'
				#print s
				#print '========================================'

		
				out = p.communicate(s)
				a=out[0]

				#print a
				busqueda=a.find('apk')
				#print 'busqueda', busqueda
				#print '*************************************************+++'
				b=a[busqueda+5:busqueda+30]
				c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
				#print '******'
				#print c
				#print '******'
				if opc==-2:
					if c =='WARNING' or c== ' ERROR ':
						#print 'No encontro picker'
				
						b=-1
						#print b

					else:
						aux=''
						name_Z=b[0:8]
						year=b[8:11]
						month=b[11:13]
						day=b[13:15]
						hour=b[15:17]
						minutos=b[17:19]
						sec=b[19:24]
						name_full=''
						name_full+=name_Z
						#Crea formato de deteccion de la onda P
						for i in range(len(year)):
							if i==0:
								aux=aux+'2'
							elif i==1:
								aux=aux+'0'
							else:
								aux=aux+'0'
								aux=aux+year[i]
					
						aux=aux+' '

						for i in range(len(month)):
							if month[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+month[i]
						aux=aux+' '
						for i in range(len(day)):
							if day[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+day[i]
						aux=aux+' '
						for i in range(len(hour)):	
							if hour[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+hour[i]
						aux=aux+' '
						for i in range(len(minutos)):
							if minutos[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+minutos[i]
						#nombre_archivo=aux
						#nombre_archivo = nombre_archivo.replace(" ", ".")
						aux=aux+' '

						for i in range(len(sec)):
							if sec[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+sec[i]
						time_arrive.append(aux)
						names.append(name_full+' '+aux)
						ruta_Z.append(path1)
						ruta_N.append(pathN)
						ruta_E.append(pathE)
		conta=[]
		final_path=[]
		#print 'len(names)', len(names), names
		if len(names)>2:
			delay=[]
			suma=0
			for i in range(len(time_arrive)):
				for j in range(len(time_arrive)):
					n=float(time_arrive[i][14:16]+'.'+time_arrive[i][17:19])
					#print 'n', n
					m=float(time_arrive[j][14:16]+'.'+time_arrive[j][17:19])
					#print 'm', m
					delay.append(n-m)

				print delay
				for k in delay:
					suma+=abs(k)
					prom=float(suma/len(delay))
				#print prom
				#print time_arrive[i]
				#print names[i]

				aux_conta=[]
				aux_rutas=[]
				if prom < 0.9:
					aux_conta.append(prom)
					aux_conta.append(time_arrive[i])
					aux_conta.append(names[i])
					aux_rutas.append(ruta_Z[i])
					aux_rutas.append(ruta_N[i])
					aux_rutas.append(ruta_E[i])
					#print prom
					#print time_arrive[i]
					#print names[i]
					#print '+++++++++++++++++++++++++++'
				if len(aux_conta)>0:
					conta.append(aux_conta)
					final_path.append(aux_rutas)

		if len(conta)>2:
			aux_c=[]
			aux_r=[]
			for i in conta:
				if i not in aux_c:
					aux_c.append(i)
			for i in final_path:
				if i not in aux_r:
					aux_r.append(i)




			nombre_del_archivo=''
			dia_archivos=''
			hora_archivo=''
			dia_archivos=aux_c[0][1][8:10]
			if len(dia_archivos)==2:
				arch='0'
				arch+=dia_archivos
				dia_archivos=arch

			hora_archivo=aux_c[0][1][11:13]
			minutos_archivo=aux_c[0][1][14:16]
			for i in range(len(aux_c)):
				nombre_del_archivo=aux_c[i][1]
				nombre_del_archivo=nombre_del_archivo.replace(" ", ".")
				station=aux_c[i][2][0:4]

				#print '============='
				#print station
				#print '============='



				path_salve_dia='/home/carlos/Escritorio/Resultados_2007/'+dia_a
				#path_salve_dia='/home/carlos/Escritorio/probard/'+dia_a
				if not os.path.exists(path_salve_dia):
					print 'crea carpeta en', path_salve_dia
					os.makedirs(path_salve_dia)
				else:
					print 'ya existe la carpeta', path_salve_dia

				path_salve_hora=path_salve_dia+'/'+hora_archivo
				if not os.path.exists(path_salve_hora):
					print 'crea carpeta en', path_salve_hora
					os.makedirs(path_salve_hora)
				else:
					print 'ya existe la carpeta', path_salve_hora



				path_salve_minutos=path_salve_hora+'/'+minutos_archivo
				if not os.path.exists(path_salve_minutos):
					print 'crea carpeta en', path_salve_minutos
					os.makedirs(path_salve_minutos)
				else:
					print 'ya existe la carpeta', path_salve_minutos



				path2=path_salve_minutos+'/'+nombre_del_archivo+'.'+station+'.HHZ.SAC'
				if os.path.isfile(path2):
					print 'el archivo existe', path2
				else:

					
					path_name_N=path_salve_minutos+'/'+nombre_del_archivo+'.'+station+'.HHN.SAC'
					path_name_E=path_salve_minutos+'/'+nombre_del_archivo+'.'+station+'.HHE.SAC'
					nombre_z=nombre_del_archivo+'.'+station+'.HHZ'
					nombre_n=nombre_del_archivo+'.'+station+'.HHN'
					nombre_e=nombre_del_archivo+'.'+station+'.HHE'
					#print 'el archivo no existe', path2
					#print 'HHZ', path2
					#print 'HHN', path_name_N
					#print 'HHE', path_name_E
					#print indicei, indicef
					inicio_cut=Pos_Cut_Sac()
					
					
					path11=aux_file+dia_a+'/ZA.'+station+'..HHZ.M.2007.'+dia_a+'.000000.SAC'
					#print path1
					pathE1=aux_file+dia_a+'/ZA.'+station+'..HHE.M.2007.'+dia_a+'.000000.SAC'
					pathN1=aux_file+dia_a+'/ZA.'+station+'..HHN.M.2007.'+dia_a+'.000000.SAC'

					print 'rutas', path11, pathN1, pathE1
					
					inicio_cut.CutWindows(path11, path2, indicei, indicef)
					inicio_cut.CutWindows(pathN1, path_name_N, indicei, indicef)
					inicio_cut.CutWindows(pathE1, path_name_E, indicei, indicef)
					file_name=aux_c[0][1][0:16]
					file_name=file_name.replace(" ", ".")
					#print ':) :) :)', file_name
					inicio_pos_guarda=Pos_archivos()
					inicio_pos_guarda.main(path2, path_name_N, path_name_E, file_name, nombre_z, nombre_n, nombre_e,  path_salve_minutos, indicei, indicef)


			#for i in range(len(aux_c)):
				#print '+++++++++++++++++++++++++++'
				#for j in aux_c[i]:
					
					#print j
				#print '+++++++++++++++++++++++++++'

			#print aux_c
#inicio=Buscar_picker()
#name='2006.027.00.07.47.BAVA.ZA.HHZ.SAC'
#indicei='2576'  #'41509'
#indicef='2691'  #'41624'

#indicei='41509'
#indicef='41624'
#inicio.main(indicei, indicef)
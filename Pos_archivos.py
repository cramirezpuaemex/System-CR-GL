from Pos_picker import *

class Pos_archivos():
	def main(self, pathz, pathn, pathe, nombre_archivo, nombre_z, nombre_n, nombre_e, path_salve, indice_inicio, indice_fin):
		opc=-2
		picker_inicio=Pos_picker()
		picker_z=picker_inicio.main(pathz)
		picker_n=picker_inicio.main(pathn)
		picker_e=picker_inicio.main(pathe)

		#print picker_z, picker_n, picker_e
		#print a



		busqueda_z=picker_z.find('apk')
		#print 'busqueda', busqueda
		#print '*************************************************+++'
		b=picker_z[busqueda_z+5:busqueda_z+30]
		c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
		print '******'
		print 'aux_z', c
		print '******'
		if opc==-2:
			aux=''
			if c =='WARNING' or c== ' ERROR 'or c=='  ERROR ':
				#print 'No encontro picker'
				
				for i in range(11):
					aux+=' '
					#print b

			else:
				
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

		#===========================================================
		busqueda_n=picker_n.find('apk')
		b_n=picker_n[busqueda_n+5:busqueda_n+30]
		c_n=b_n[0]+b_n[1]+b_n[2]+b_n[3]+b_n[4]+b_n[5]+b_n[6]
		print '******'
		print 'c_n', c_n
		print '******'
		opc=-2
		aux_n=''
		if opc==-2:
			
			if c_n =='WARNING' or c_n==' ERROR ' :
				#print 'No encontro picker'
				
				for i in range(11):
					aux_n+=' '
						#print b

			else:
				hour_n=b_n[15:17]
				minutos_n=b_n[17:19]
				sec_n=b_n[19:24]				


				#Crea formato de deteccion de la onda P

				for i in range(len(hour_n)):	
					if hour_n[i]==' ':
						aux_n=aux_n+'0'
					else:
						aux_n=aux_n+hour_n[i]
				aux_n=aux_n+' '
				for i in range(len(minutos_n)):
					if minutos_n[i]==' ':
						aux_n=aux_n+'0'
					else:
						aux_n=aux_n+minutos_n[i]
				#nombre_archivo=aux
				#nombre_archivo = nombre_archivo.replace(" ", ".")
				aux_n=aux_n+' '

				for i in range(len(sec_n)):
					if sec_n[i]==' ':
						aux_n=aux_n+'0'
					else:
						aux_n=aux_n+sec_n[i]
		#===========================================================
		busqueda_e=picker_e.find('apk')
		b_e=picker_e[busqueda_e+5:busqueda_e+30]
		c_e=b_e[0]+b_e[1]+b_e[2]+b_e[3]+b_e[4]+b_e[5]+b_e[6]
		print '******'
		print 'c_e', c_e
		print '******'
		opc=-2
		aux_e=''
		if opc==-2:
			
			if c_e =='WARNING'or c_e==' ERROR ':
				#print 'No encontro picker'
				
				for i in range(11):
					aux_e+=' '
						#print b

			else:
				hour_e=b_e[15:17]
				minutos_e=b_e[17:19]
				sec_e=b_e[19:24]

				#Crea formato de deteccion de la onda P

				for i in range(len(hour_e)):	
					if hour_e[i]==' ':
						aux_e=aux_e+'0'
					else:
						aux_e=aux_e+hour_e[i]
				aux_e=aux_e+' '
				for i in range(len(minutos_e)):
					if minutos_e[i]==' ':
						aux_e=aux_e+'0'
					else:
						aux_e=aux_e+minutos_e[i]
				#nombre_archivo=aux
				#nombre_archivo = nombre_archivo.replace(" ", ".")
				aux_e=aux_e+' '

				for i in range(len(sec_e)):
					if sec_e[i]==' ':
						aux_e=aux_e+'0'
					else:
						aux_e=aux_e+sec_e[i]				



		fo = open(path_salve+'/'+nombre_archivo+'.txt', 'a')
		#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')
		
		print '=============DATOS A GUARDAR================'
		print 'aux', aux
		print 'aux_e', aux_e
		print 'aux_n', aux_n
		print '=============DATOS A GUARDAR================'

		fo.write(str(indice_inicio)+'--'+str(indice_fin)+'   '+'|'+'   ')
		fo.write(nombre_z+'   '+'|'+'   ')
		fo.write(name_Z+' '+aux+'   '+'|'+'   ')
		fo.write(aux_n+'   '+'|'+'   ')
		fo.write(aux_e)
		fo.write('\n')


		

		fo.close()

		



class Genera_archivos():
	def crea_nombre(self,path1, path2, ruta, nombre_guardar, indice_inicio, indice_fin, rate_correlation, opcion, picker, picker_E, picker_N):
		#fo = open(ruta+'/Resultados_analisis.txt', 'a')
		estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']
		for i in estaciones:
			if path1.find(i) !=-1:
				self.estacion_1=i
			if path2.find(i) != -1:
				self.estacion_2=i
		
		busqueda_estacion1=path1.find('2006.')
		busqueda_estacion2=path2.find('2006.')
		self.dia2=path2[busqueda_estacion2+5:busqueda_estacion2+8]
		self.dia1=path1[busqueda_estacion1+5:busqueda_estacion1+8]
		self.id_catalogo=path2[busqueda_estacion2:busqueda_estacion2+14]+self.estacion_2
		#fo.write(str(dia2)+" - "+estacion_2+' encontrada en el dia '+str(dia1)+' en la estacion '+estacion_1+' con un indice de correlacion de '+str(rate_correlation)+'\n')
		#fo.write(nombre+' \n')
		#fo.write(str(indice)+'-'+str(indice+lon_datos)+'\n')

		#fo.close()

		self.nombre=str(self.dia2)+'.'+self.estacion_2+'.'

		if opcion == 1:
			return self.nombre
		else:
			self.escribe_archivos(picker, ruta, rate_correlation, indice_inicio, indice_fin, nombre_guardar, picker_E, picker_N)

	def escribe_archivos(self, picker, ruta, rate_correlation, indice_inicio, indice_fin, nombre_guardar, picker_E, picker_N):


		aux=''
		aux_E=''
		aux_N=''
		nombre_archivo=''
		a=picker
		name_Z=a[0:8]
		year=a[8:11]
		month=a[11:13]
		day=a[13:15]
		hour=a[15:17]
		minutos=a[17:19]
		sec=a[19:24]

		if picker_E != -1:
			b=picker_E
			name_E=b[0:8]
			hour_E=b[15:17]
			minutos_E=b[17:19]
			sec_E=b[19:24]
			aux_E=''
			for i in range(len(hour_E)):
				if hour_E[i]==' ':
					aux_E=aux_E+'0'
				else:
					aux_E=aux_E+hour_E[i]
			aux_E=aux_E+' '
			for i in range(len(minutos)):
				if minutos_E[i]==' ':
					aux_E=aux_E+'0'
				else:
					aux_E=aux_E+minutos_E[i]
			aux_E=aux_E+' '
			for i in range(len(sec_E)):
				if sec_E[i]==' ':
					aux_E=aux_E+'0'
				else:
					aux_E=aux_E+sec_E[i]

		else:

			for i in range(11):

				aux_E=aux_E+' '			
		#************************************************************************************
		#************************************************************************************
		if picker_N != -1:
			c=picker_N
			name_N=c[0:8]
			hour_N=c[15:17]
			minutos_N=c[17:19]
			sec_N=c[19:24]
			aux_N=''
			for i in range(len(hour_N)):
				if hour_N[i]==' ':
					aux_N=aux_N+'0'
				else:
					aux_N=aux_N+hour_N[i]
			aux_N=aux_N+' '
			for i in range(len(minutos)):
				if minutos_N[i]==' ':
					aux_N=aux_N+'0'
				else:
					aux_N=aux_N+minutos_N[i]
			aux_N=aux_N+' '
			for i in range(len(sec_N)):
				if sec_N[i]==' ':
					aux_N=aux_N+'0'
				else:
					aux_N=aux_N+sec_N[i]

		else:
			for i in range(11):
				aux_N=aux_N+' '	



		#************************************************************************************
		#************************************************************************************
		if rate_correlation>1:
			rate_correlation=rate_correlation-(rate_correlation-1)



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
		nombre_archivo=aux
		nombre_archivo = nombre_archivo.replace(" ", ".")
		aux=aux+' '

		for i in range(len(sec)):
			if sec[i]==' ':
				aux=aux+'0'
			else:
				aux=aux+sec[i]

				



		fo = open(ruta+'/'+nombre_archivo+'.txt', 'a')
		#fo.write('\n'+str(self.dia2)+" - "+self.estacion_2+' encontrada en el dia '+str(self.dia1)+' en la estacion '+self.estacion_1+'\n')
		fo.write(self.id_catalogo+'<->'+str(self.dia1)+'.'+self.estacion_1+'\t'+'|'+'\t')
		fo.write(str(indice_inicio)+'--'+str(indice_fin)+'\t'+'|'+'\t')
		fo.write(str(rate_correlation)+'\t'+'|'+'\t')
		fo.write(nombre_guardar+'\t'+'|'+'\t')
		fo.write(name_Z+' '+aux+'\t'+'|'+'\t')
		fo.write(aux_E+'\t'+'|'+'\t')
		fo.write(aux_N+'\n')


		

		fo.close()

		

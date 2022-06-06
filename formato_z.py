class formato_z():
	def main(self, picker_z, busqueda_z):
		opc=-2
		b=picker_z[busqueda_z+5:busqueda_z+30]
		print 'fase_z', b
		c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
		#print 'fase_z', c
		if opc==-2:
			aux=''
			if c =='WARNING' or c== ' ERROR ':
				#print 'No encontro picker'
				
				aux=-1
				#print b

			else:
				
				name_Z=b[0:8]
				year=b[8:11]
				month=b[11:13]
				day=b[13:15]
				hour=b[15:17]
				minutos=b[17:19]
				sec=b[19:24]
				print 'sec', sec, len(sec)
				name_full=''
				name_full+=name_Z
				aux+=name_Z
				aux=aux+' '
				#Crea formato de deteccion de la onda P
				for i in range(len(year)):
					if i==0:
						#aux=aux+'0'
						continue
					elif i==1:
						continue
						#aux=aux+'0'
					else:
						aux=aux+'0'
						aux=aux+year[i]
					
				#aux=aux+' '

				for i in range(len(month)):
					if month[i]==' ':
						aux=aux+'0'
					else:
						aux=aux+month[i]
				#aux=aux+' '
				for i in range(len(day)):
					if day[i]==' ':
						aux=aux+'0'
					else:
						aux=aux+day[i]
				#aux=aux+' '
				for i in range(len(hour)):	
					if hour[i]==' ':
						aux=aux+'0'
					else:
						aux=aux+hour[i]
				#aux=aux+' '
				for i in range(len(minutos)):
					if minutos[i]==' ':
						aux=aux+'0'
					else:
						aux=aux+minutos[i]
				#nombre_archivo=aux
				#nombre_archivo = nombre_archivo.replace(" ", ".")
				#aux=aux+' '

				for i in range(len(sec)):
					print 'sec[', i, ']', sec[i]
					if sec[i]==' ':
						aux=aux+'0'
					else:
						aux=aux+sec[i]

		if aux !=-1:
			#regresa=b		
			regresa=aux
		else:
			regresa=-1
		return regresa


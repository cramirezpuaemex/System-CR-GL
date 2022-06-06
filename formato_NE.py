class formato_NE():
	def main(self, picker_n, picker_e)		:
		regresa=[]

		#===========================================================
		busqueda_n=picker_n.find('apk')
		b_n=picker_n[busqueda_n+5:busqueda_n+30]
		c_n=b_n[0]+b_n[1]+b_n[2]+b_n[3]+b_n[4]+b_n[5]+b_n[6]
		#print '******'
		#print 'c_n', c_n
		#print '******'
		opc=-2
		aux_n=''
		if opc==-2:
			
			if c_n =='WARNING' or c_n==' ERROR ' :
				#print 'No encontro picker'
				
				#for i in range(11):
					#aux_n+=' '
				aux_n='0'
						#print b

			else:
				hour_n=b_n[15:17]
				minutos_n=b_n[17:19]
				sec_n=b_n[19:24]				


				#Crea formato de deteccion de la onda P
				'''
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
				'''
				for i in range(len(sec_n)):
					if sec_n[i]==' ':
						aux_n=aux_n+'0'
					else:
						aux_n=aux_n+sec_n[i]
		regresa.append(aux_n)
		#===========================================================
		busqueda_e=picker_e.find('apk')
		b_e=picker_e[busqueda_e+5:busqueda_e+30]
		c_e=b_e[0]+b_e[1]+b_e[2]+b_e[3]+b_e[4]+b_e[5]+b_e[6]
		#print '******'
		#print 'c_e', c_e
		#print '******'
		opc=-2
		aux_e=''
		if opc==-2:
			
			if c_e =='WARNING'or c_e==' ERROR ':
				#print 'No encontro picker'
				
				#for i in range(11):
					#aux_e+=' '
				aux_e='0'
						#print b

			else:
				hour_e=b_e[15:17]
				minutos_e=b_e[17:19]
				sec_e=b_e[19:24]

				#Crea formato de deteccion de la onda P
				'''
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
				'''
				for i in range(len(sec_e)):
					if sec_e[i]==' ':
						aux_e=aux_e+'0'
					else:
						aux_e=aux_e+sec_e[i]
		regresa.append(aux_e)
		return regresa
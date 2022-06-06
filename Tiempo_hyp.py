

class Tiempo_hyp():
	"""docstring for ClassName"""
	def proceso_tiempo(self, hora_llegada, minuto_llegada, tiempo_llegada, estaciones_llegada):
		
		#print hora_llegada
		#print minuto_llegada
		#print tiempo_llegada
		#print estaciones_llegada				
		tiempo=[]
		estaciones=[]
		horas=[]
		minutos=[]

		#print 'inicia lo nuevo'

		vec_aux_h=[]
		vec_aux_m=[]
		vec_aux_s=[]
		vec_aux_e=[]	
		vec_aux_full=[]
		for i in range(len(hora_llegada)):
			aux_f=''
			aux_f=str(hora_llegada[i])+str(minuto_llegada[i])+str(tiempo_llegada[i])
			vec_aux_full.append(float(aux_f))




		indice_aux=[]
		while len(indice_aux)!=len(hora_llegada):
			aux_index=vec_aux_full.index(min(vec_aux_full))
			#print 'el minimo es :', min(hora_llegada)
			indice_aux.append(vec_aux_full[aux_index])
			vec_aux_full[aux_index]=vec_aux_full[aux_index]*1000



		#print 'vector organizado', indice_aux



		vec_aux_full=[]
		for i in range(len(hora_llegada)):
			aux_f=''
			aux_f=str(hora_llegada[i])+str(minuto_llegada[i])+str(tiempo_llegada[i])
			vec_aux_full.append(float(aux_f))

		#print 'vector no organizado', vec_aux_full
		indice_a=[]
		while len(indice_a)!= len(hora_llegada):
			for i in range(len(vec_aux_full)):
				for j in range(len(vec_aux_full)):
					if indice_aux[i]==vec_aux_full[j]:
						#print j
						indice_a.append(j)
						indice_aux[i]=indice_aux[i]+8

		##print indice_a

		for i in (indice_a):
			vec_aux_h.append(hora_llegada[i])
			vec_aux_m.append(minuto_llegada[i])
			vec_aux_s.append(tiempo_llegada[i])
			vec_aux_e.append(estaciones_llegada[i])


		horas=vec_aux_h
		minutos=vec_aux_m
		tiempo=vec_aux_s
		estaciones=vec_aux_e

		'''


		vec_aux_h=[]
		vec_aux_m=[]
		vec_aux_s=[]
		vec_aux_e=[]		
		while len(tiempo_llegada)!=0:
			aux_index=hora_llegada.index(min(hora_llegada))
			print 'el minimo es :', min(hora_llegada)
			vec_aux_h.append(hora_llegada[aux_index])
			vec_aux_m.append(minuto_llegada[aux_index])
			vec_aux_s.append(tiempo_llegada[aux_index])
			vec_aux_e.append(estaciones_llegada[aux_index])
			hora_llegada.pop(aux_index)
			minuto_llegada.pop(aux_index)
			estaciones_llegada.pop(aux_index)
			tiempo_llegada.pop(aux_index)

		hora_llegada=vec_aux_h
		minuto_llegada=vec_aux_m
		tiempo_llegada=vec_aux_s
		estaciones_llegada=vec_aux_e



		vec_aux_h=[]
		vec_aux_m=[]
		vec_aux_s=[]
		vec_aux_e=[]

		while len(tiempo_llegada)!=0:
			aux_index=minuto_llegada.index(min(minuto_llegada))
			print 'el minimo es :', min(minuto_llegada)
			vec_aux_h.append(hora_llegada[aux_index])
			vec_aux_m.append(minuto_llegada[aux_index])
			vec_aux_s.append(tiempo_llegada[aux_index])
			vec_aux_e.append(estaciones_llegada[aux_index])
			hora_llegada.pop(aux_index)
			minuto_llegada.pop(aux_index)
			estaciones_llegada.pop(aux_index)
			tiempo_llegada.pop(aux_index)

		hora_llegada=vec_aux_h
		minuto_llegada=vec_aux_m
		tiempo_llegada=vec_aux_s
		estaciones_llegada=vec_aux_e


		while len(tiempo_llegada)!=0:
			aux_index=tiempo_llegada.index(min(tiempo_llegada))
			print 'el minimo es :', min(tiempo_llegada)
			horas.append(hora_llegada[aux_index])
			minutos.append(minuto_llegada[aux_index])
			tiempo.append(tiempo_llegada[aux_index])
			estaciones.append(estaciones_llegada[aux_index])
			hora_llegada.pop(aux_index)
			minuto_llegada.pop(aux_index)
			estaciones_llegada.pop(aux_index)
			tiempo_llegada.pop(aux_index)


		#termina lo nuevo
		#*********************************************************************
		
		aux_hora=min(hora_llegada)
		veces_hora=hora_llegada.count(aux_hora)
		if veces_hora != len(hora_llegada):
			print 'horas diferentes'
			aux_index=hora_llegada.index(min(hora_llegada))
			horas.append(hora_llegada[aux_index])
			minutos.append(minuto_llegada[aux_index])
			tiempo.append(tiempo_llegada[aux_index])
			estaciones.append(estaciones_llegada[aux_index])
			hora_llegada.pop(aux_index)
			minuto_llegada.pop(aux_index)
			estaciones_llegada.pop(aux_index)
			tiempo_llegada.pop(aux_index)			
		else:
			vec_aux_h=[]
			vec_aux_m=[]
			vec_aux_s=[]
			vec_aux_e=[]

			print 'la hora es la misma'
			#*****************************************************
			aux_min=0
			print 'inicia lo nuevo'
			while len(tiempo_llegada)!=0:
				aux_index=minuto_llegada.index(min(minuto_llegada))
				print 'el minimo es :', min(minuto_llegada)
				vec_aux_h.append(hora_llegada[aux_index])
				vec_aux_m.append(minuto_llegada[aux_index])
				vec_aux_s.append(tiempo_llegada[aux_index])
				vec_aux_e.append(estaciones_llegada[aux_index])
				hora_llegada.pop(aux_index)
			 	minuto_llegada.pop(aux_index)
			 	estaciones_llegada.pop(aux_index)
			 	tiempo_llegada.pop(aux_index)

			hora_llegada=vec_aux_h
			minuto_llegada=vec_aux_m
			tiempo_llegada=vec_aux_s
			estaciones_llegada=vec_aux_e

			while len(tiempo_llegada)!=0:
				aux_index=tiempo_llegada.index(min(tiempo_llegada))
			 	horas.append(hora_llegada[aux_index])
			 	minutos.append(minuto_llegada[aux_index])
			 	tiempo.append(tiempo_llegada[aux_index])
			 	estaciones.append(estaciones_llegada[aux_index])
			 	hora_llegada.pop(aux_index)
			 	minuto_llegada.pop(aux_index)
			 	estaciones_llegada.pop(aux_index)
			 	tiempo_llegada.pop(aux_index)


				

			#*****************************************************
			aux_minuto=min(minuto_llegada)
			veces_minuto=minuto_llegada.count(aux_minuto)
			if veces_minuto != len(minuto_llegada):
				
			 	aux_index=minuto_llegada.index(min(minuto_llegada))
			 	horas.append(hora_llegada[aux_index])
			 	minutos.append(minuto_llegada[aux_index])
			 	tiempo.append(tiempo_llegada[aux_index])
			 	estaciones.append(estaciones_llegada[aux_index])
			 	hora_llegada.pop(aux_index)
			 	minuto_llegada.pop(aux_index)
			 	estaciones_llegada.pop(aux_index)
			 	tiempo_llegada.pop(aux_index)

				while len(tiempo_llegada)!=0:
					aux_index=tiempo_llegada.index(min(tiempo_llegada))
			 		horas.append(hora_llegada[aux_index])
			 		minutos.append(minuto_llegada[aux_index])
			 		tiempo.append(tiempo_llegada[aux_index])
			 		estaciones.append(estaciones_llegada[aux_index])
			 		hora_llegada.pop(aux_index)
			 		minuto_llegada.pop(aux_index)
			 		estaciones_llegada.pop(aux_index)
			 		tiempo_llegada.pop(aux_index)

			else:	
				print 'los minutos son los mismos'	
				while len(tiempo_llegada)!=0:
					aux_index=tiempo_llegada.index(min(tiempo_llegada))
			 		horas.append(hora_llegada[aux_index])
			 		minutos.append(minuto_llegada[aux_index])
			 		tiempo.append(tiempo_llegada[aux_index])
			 		estaciones.append(estaciones_llegada[aux_index])
			 		hora_llegada.pop(aux_index)
			 		minuto_llegada.pop(aux_index)
			 		estaciones_llegada.pop(aux_index)
			 		tiempo_llegada.pop(aux_index)
			'''
		aux_resultados=[]
		aux_resultados.append(horas)
		aux_resultados.append(minutos)
		aux_resultados.append(tiempo)
		aux_resultados.append(estaciones)

		return aux_resultados
	

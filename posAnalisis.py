# archivo-entrada.py
# f = open ('/home/carlos/Escritorio/Analisis_Resultados/027/2006.027.00/2006.01.27.00.09.txt','r')
# array=[]
# mensaje = f.read()

# f.close()

# print (mensaje)

from Buscar_picker import *

class posAnalisis():
	def main(self, path, dia_a):

		inicio_bp=Buscar_picker()
		#print path
		file=open(path, "r")
		#file=open("/home/carlos/Escritorio/Analisis_Resultados/027/2006.027.00/2006.01.27.00.29.txt", "r")
		infile=file.readlines()
		vec=[]
		for i in infile:
			vec.append(i)



		estaciones=[]
		contenido=[]
		cont=0
		v_indice=[]
		v_name=[]
		tiempo_llegada=[]
		if len(vec)>=2:
			aux=''
			for i in vec:

				v_aux=[]
				for j in range(len(i)):
					if i[j].find('\t')!= 0:
						aux+=i[j]
					else:
						if  aux != '|':
							v_aux.append(aux)
							aux=''
						else:
							aux=''
				
				v_indice.append(v_aux[1])
				v_name.append(v_aux[3])
				tiempo_llegada.append(v_aux[4])
		else:
			aux=''
			v_aux=[]
			for j in range(len(vec[0])):
				if i[j].find('\t')!= 0:
					aux+=i[j]
				else:
					if  aux != '|':
						v_aux.append(aux)
						aux=''
					else:
						aux=''
			v_indice.append(v_aux[1])
			v_name.append(v_aux[3])			
			tiempo_llegada.append(v_aux[4])


	 	estaciones=[]
	 	time=[]
	 	for i in range(len(v_name)):
	 		estaciones.append(v_name[i][18:22])
	 		time.append(v_name[i][5:17])

	 	time=sorted(time)
	 	esta_aux=[]
	 	for i in range(len(v_indice)):
	 		s=''
	 		s+=v_indice[i]+'.'+v_name[i]+'/'+tiempo_llegada[i]
	 		esta_aux.append(s)

	 	name_estaciones=[]
	 	indicei=[]
	 	indicef=[]
	 	arrive=[]
	 	files=[]
	 	#print time
	 	#print esta_aux
	 	for i in range(len(time)):
	 		for j in range(len(esta_aux)):
	 			
	 			b=esta_aux[j].find('--')
	 			p=esta_aux[j].find('.')
	 			l=esta_aux[j].find('/')
	 			d=esta_aux[j][p+6:p+18]
	 			if d == time[i]:
	 					if esta_aux[j][p+1:len(esta_aux[j])]   not in files:

	 						
	 						if esta_aux[j][p+19:p+23] not in name_estaciones:
	 							files.append(esta_aux[j][p+1:l])
	 							name_estaciones.append(esta_aux[j][p+19:p+23])
	 							indicei.append(esta_aux[j][0:b])
	 							indicef.append(esta_aux[j][b+2:p])
	 							arrive.append(esta_aux[j][l+21:len(esta_aux[j])])
	 					
	 	for i in range(len(indicei)):
	 		indicei[i]=int(int(indicei[i])/100)
	 		indicef[i]=int(int(indicef[i])/100)


		for i in range(len(name_estaciones)):

			#print name_estaciones[i]
			#print indicei[i], indicef[i]
			#print indicef[i]
			#print files[i]
			#print arrive[i]
			inicio_bp.main(indicei[i], indicef[i], dia_a)	

		#print name_estaciones




		#print '=========================================================================='

#inicio=posAnalisis()
#name="/home/carlos/Escritorio/Analisis_Resultados/027/2006.027.00/2006.01.27.00.29.txt"
#inicio.main(name)
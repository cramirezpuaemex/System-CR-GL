import os


class File_Data_hypDD():
	def main(self, ruta_loca, model):
		#model='codex_18'
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


		for i in elementos1:
			aux=[]
			#print i[0], i[4], i[5]
	
			if i[0]!='SEQ':
				if i[3][2] !=' ':
					#print 'FALLA'
					latitud=i[4][1:len(i[4])-1]
					longuitud='-'+i[5][0:len(i[5])-1]
					longuitud=longuitud.replace('W', ' ')
					valor_f=float(latitud[len(latitud)-5:len(latitud)])
					valor_f=valor_f/60
					valor_i=int(latitud[0:3])
					
					latitud=round(valor_i+valor_f,4)
					valor_f=float(longuitud[len(longuitud)-5:len(longuitud)])
					valor_f=valor_f/60
					
					valor_i=int(longuitud[0:4])

					longuitud=round(valor_i-valor_f, 4)
					mes_dia=i[2].replace('-', '')
					mes_dia=mes_dia.replace(' ', '0')
					fecha=i[1]+mes_dia
					identificador=i[0]
					hora=i[3]
					aux_h1=i[3][0:4]
					aux_h2=i[3][5:len(i[3])]
					aux_h2=aux_h2.replace(' ', '0')
					hora=aux_h1+aux_h2
					
					#hora=hora.replace(' ', '')
					hora=hora.replace('.', '')
					#print i[3], aux_h1, aux_h2, hora
					depth=round(float(i[6]), 3)
					mag=i[9]
					eh=i[11]
					ev=i[10]
					rms=i[7]

					ruta_salve_file_data=(os.path.dirname(os.path.realpath(__file__)))
					fo = open(ruta_salve_file_data+'/Files_HypDD/'+model+'.dat', 'a')
					fo.write(str(fecha)+'\t'+str(hora)+'\t'+str(latitud)+'\t'+str(longuitud)+'\t'+str(depth)+'\t'+mag+'\t'+eh+'\t'+ev+'\t'+rms+'\t'+identificador+'\n')
					print fecha, hora, latitud, longuitud, depth, mag, eh, ev, rms, identificador
					aux.append(i[0])
					#aux.append(i[4][0:len(i[4])])
					#aux.append('-'+i[5])
					aux.append(latitud)
					aux.append(longuitud)
					archivos.append(aux)



		
#inicio_grupos=relocalizacion()
#inicio_grupos.main()

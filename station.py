import os

class station():
	def main(self, ruta_loca, model):
		#model='codex_16'
		#ruta_loca='/home/carlos/Escritorio/codex_station.dat'
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
			lista=i.split(" ")
			#lista.remove("\n")
			elementos1.append([(e) for e in lista])
		
		archivos=[]


		for i in elementos1:
			estaciones=i[0]
			valor_i=int(i[6])
			valor_f=float(i[7])
			valor_f=valor_f/60
			latitud=round(valor_i+valor_f,6)
			valor_i=int(i[8])
			valor_f=float(i[9][0:len(i[9])-1])
			valor_f=valor_f/60
			longuitud=round((valor_i+valor_f)*-1,6)
			ruta_salve_file_stations=(os.path.dirname(os.path.realpath(__file__)))
			fo = open(ruta_salve_file_stations+'/Files_HypDD/'+model+'_sta.dat', 'a')
			fo.write(estaciones+'\t'+str(latitud)+'\t'+str(longuitud)+'\n')
			print estaciones, latitud, longuitud
			
			
	




		
#inicio_grupos=station()
#inicio_grupos.main()

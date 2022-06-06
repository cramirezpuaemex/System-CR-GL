

class Hyp_Lectura_file():
	def main(self, path):
		f = open(path,"r")
		arreglo= []
		contLin=0
		while True:
			linea = f.readline()
			if linea:
				datos = linea.split('\n')
				datos = datos[0].split(',')
				arreglo.append(datos)
			else:
				break

		return arreglo


class Input_model():
	def main(self):
		
		print("Por favor ingrese el numero de capas que tendra el modelo: ")
		capas = (input())

		#capas = int(capas)
		profunidad=[]
		velocidad=[]
		print capas*2

		for i in range(capas):
			print "Profundidad para la capa: ", i
			profunidad.append(input())
			print "Velocidad para la capa: ", i
			velocidad.append(input())

		print "Ingresa Nombre del modelo:"
		name=str(input())
		print "MOdel Velocity (", name,")"
		for i in range(capas):
			print profunidad[i], "   ", velocidad[i]
			



inicio=Input_model()
inicio.main()
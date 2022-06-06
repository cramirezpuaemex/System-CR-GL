import numpy as np

class Diezmado():
	def proceso(self, senal, valor):
		
		
		
		for j in range(2):
			aux=[]
			for i in range(len(senal)):
				if i % 2 == 0:
					aux.append(senal[i])
			senal=aux

		return senal
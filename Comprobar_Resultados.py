import math
from Correlacion import *
class Comprobar_Resultados():

	def trabaja_comprobar(self, senal01, senal02):

		if len(senal01)>=len(senal02):
			ex=math.log(len(senal01),2)
			
		
			
		else:
			ex=math.log(len(senal02),2)
			

		ex=math.floor(ex)

		xcross=Correlacion()
		R_xy=xcross.trabaja(senal01, senal02, ex)

		maximo=max(R_xy)
		indice=R_xy.index(maximo)
		aux=[]
		resul=[]
		if maximo>=0.80 and maximo <1.003:
			aux.append(maximo)
			#print maximo
			aux.append(indice)
			#print indice
			resul.append(aux)
			return resul
		else:
			aux.append(-1)
			aux.append(-1)
			resul.append(aux)
			#print resul
			return resul


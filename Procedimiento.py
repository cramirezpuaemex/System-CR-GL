import math
import numpy as np
from Correlacion import *

class Procedimiento():
	def proceso(self, senal01, senal02, valor):
		tamano01 = len(senal01)
		tamano02 = len(senal02)
		#print 'tamano01', tamano01
		valor=int(math.log(tamano01,2))
		#print 'valor nuevo', valor
		l=tamano01/valor
		l=int(math.floor(l))
		if l>=len(senal02):
			ex=math.log(l,2)
			lon_mx=len(senal01)
		
			
		else:
			ex=math.log(len(senal02),2)
			lon_mx=len(senal02)

		self.ex=math.floor(ex)
		self.v_max=[]
		self.v_indice=[]

		#========== Se generar los rangos de la senal correspondiente a un dia completo =====================
		for p in range(valor):
			aux=[]
			mitad=l/2
			mitad=int(math.floor(mitad))

			#====================== Inicia la creacion de la clase correlacion ===============================
			xcross=Correlacion()
			#====================== Termina la creacion de la clase correlacion ==============================
						
			if p==0:
				parte=senal01[0:l]
				#== Inicia la correlacion entre el rango generado de la senal01 y la senal02 correspondiente a la senales del catalogo de sismos ==
				self.R_xy=xcross.trabaja(parte, senal02, self.ex)

				self.valor_indice(p, l)

				#nuevo analisis implementado el dia 18/07/2019 PRUEBA IMPLEMENTACION
				parte=senal01[mitad:(mitad*2)+1]
				self.R_xy=xcross.trabaja(parte, senal02, self.ex)
				self.valor_indice(p, l)
			else:

				if p ==valor-1:
					parte=senal01[l*p: len(senal01)]
					self.R_xy=xcross.trabaja(parte, senal02, self.ex)
					self.valor_indice(p, l)
				else:
					parte=senal01[l*p: l*(p+1)]
					#== Inicia la correlacion entre el rango generado de la senal01 y la senal02 correspondiente a la senales del catalogo de sismos ==
					self.R_xy=xcross.trabaja(parte, senal02, self.ex)

					self.valor_indice(p, l)

				#nuevo analisis implementado el dia 18/07/2019 PRUEBA IMPLEMENTACION
				if (l*(p+1)+(mitad*2)+1) <= tamano01:
					parte=senal01[(l*p)+mitad: l*(p+1)+(mitad*2)+1]
					self.R_xy=xcross.trabaja(parte, senal02, self.ex)
					self.valor_indice(p, l)

		# Termina analisis por ventanas generadas de la senal  correspondiente a un dia completo ==============
		valores=[]
		valores.append(self.v_max)

		valores.append(self.v_indice)
		return valores


	def  valor_indice(self, p, l):

		#====================== se calcula el valor maximo e indice de correlacion por ventana ================
		maximo=max(self.R_xy)
		indice=self.R_xy.index(maximo)
		if maximo>=0.75 and maximo <1.003:
			self.v_max.append(maximo)
			self.v_indice.append(indice+(p*l))

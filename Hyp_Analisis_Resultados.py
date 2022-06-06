class Hyp_Analisis_Resultados():

	def main(self, errores_ERZ):
		#print '------------------------Analisis_Resultados---------------------'
		#print len(errores_ERZ)
		#print len(errores_ERH)
		#print '----------------------------------------------------------------'
		aux_min_ERZ=min(errores_ERZ)
		#aux_min_ERH=min(errores_ERH)

		aux_uz=errores_ERZ.index(aux_min_ERZ)
		#aux_depth=depth.index(aux_min_ERZ)
		#aux_uh=errores_ERH.index(aux_min_ERH)


		resultados=[]

		resultados.append(aux_uz)
		#resultados.append(aux_depth)

		return resultados




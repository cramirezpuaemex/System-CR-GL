

class Generar_Nombre:
	def main(self, path, hora, minutos, segundos):
		#print path
		estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']
		if len(hora)==1:
			hora='0'+hora
		if len(minutos)==1:
			minutos='0'+minutos
		if len(segundos)==1:
			segundos='0'+segundos					
		for i in estaciones:
			if path.find(i) !=-1:
				if path.find('2006.')!=-1:
					#print 'entra al 2006'
					busqueda_nombre=path.find('2006.')
					nombre_guardar=path[busqueda_nombre:busqueda_nombre+8]
					#print nombre_guardar
					respuesta=nombre_guardar+'.'+str(hora)+'.'+str(minutos)+'.'+str(segundos)+'.'+i+'.ZA.HHZ.SAC'
					return respuesta
				elif path.find('2007.')!=-1:
					#print 'entra al 2007pritn '
					busqueda_nombre=path.find('2007.')
					nombre_guardar=path[busqueda_nombre:busqueda_nombre+8]
					#print nombre_guardar
					respuesta=nombre_guardar+'.'+str(hora)+'.'+str(minutos)+'.'+str(segundos)+'.'+i+'.ZA.HHZ.SAC'
					return respuesta
				else:
					busqueda_nombre=path.find('2008.')
					#print 'entra al 2008'
					nombre_guardar=path[busqueda_nombre:busqueda_nombre+8]
					#print nombre_guardar
					respuesta=nombre_guardar+'.'+str(hora)+'.'+str(minutos)+'.'+str(segundos)+'.'+i+'.ZA.HHZ.SAC'
					return respuesta					



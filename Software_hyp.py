import os.path
import subprocess
import glob
import math
from os import remove
class Software_hyp():

	def main(self,fecha, a1, a2, a3, a4, arreglo, file_name, seq, salve_name_file):

		#print '*************************************'
		#print 'Software Hyp1.40'
		#print '*************************************'
		depth=0
		errores_ERH=[]
		errores_ERZ=[]
		ubicacion=[]
		profunidad=[]
		while  depth < 200:

			depth+=1.0
			#print 'depth', depth
			trial='      '+fecha+str(a1)+' '+str(a2)+str(a3)+' '+str(a4)+' '+str(depth)
			#trial='      105733.219 26.7104  0.5 '+str(depth)
		
			nombre_del_archivo=salve_name_file+'/File_hyp/codex.phs'



			
			
			for j in arreglo:
				fo = open(nombre_del_archivo, 'a')
				fo.write(j[0])
				fo.write('\n')
				#print j[0]
			fo.write(trial)
			fo.write('\n')
			fo.close()

			#print j[0]
			#sprint 'TRIAL', trial

			p = subprocess.Popen(['./hyp1.40'],
                     			stdout = subprocess.PIPE,
                     			stdin  = subprocess.PIPE,
                     			stderr = subprocess.STDOUT )

			
			s=''
			line1='@codex.hyp\n'
			s+=line1
			

			out = p.communicate( s )
			#print out
			if out[0].find('SEQ ')!=-1 and out[0].find('Note:')!=-1:

				aux=out[0].find('SEQ')
				#print aux
				aux1=out[0].find('Note:')
				#print aux1
				datos_ubicacion= out[0][aux:aux1]
	
				errores= datos_ubicacion[len(datos_ubicacion)-20:len(datos_ubicacion)-10]
				ERH=errores[0:4]
				ERZ=errores[5:9]
				#print '************************'
				#print 'datos_ubicacion', datos_ubicacion
				#print  ERZ
				#print '************************'
				#errores_ERH.append(ERH)
				#errores_ERZ.append(ERZ)
				#ubicacion.append(datos_ubicacion)
				if len(ERZ)!=0 and len(ERH)!=0:
					if float(ERH) < 100 and float(ERZ)< 100:
						errores_ERH.append(ERH)
						errores_ERZ.append(ERZ)
						ubicacion.append(datos_ubicacion)
						profunidad.append(depth)
					#print datos_ubicacion
			remove(nombre_del_archivo)
			'''
			if depth == 1:

				nombre_del_archivo_revisar='/home/carlos/Dropbox/hyp/file/codex_'+str(file_name)+'.phs'
				for j in arreglo:
					fo = open(nombre_del_archivo_revisar, 'a')
					fo.write(j[0])
					fo.write('\n')
					#print j[0]
				fo.write(trial)
				fo.write('\n')
				fo.close()
			'''

		resultados=[]
		resultados.append(errores_ERZ)
		resultados.append(errores_ERH)
		resultados.append(ubicacion)
		resultados.append(profunidad)

		return resultados

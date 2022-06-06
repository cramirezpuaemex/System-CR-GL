import os.path
import subprocess
import glob
import math
from os import remove
class Software_hyp_ptr():

	def main(self,fecha, a1, a2, a3, a4, arreglo, depth, name_salve_file):

		#print '*************************************'
		#print 'Software Software_hyp_ptr'
		#print '*************************************'
		#depth=0


		#print 'depth', depth
		trial='      '+fecha+str(a1)+' '+str(a2)+str(a3)+' '+str(a4)+' '+str(depth)
		#trial='      105733.219 26.7104  0.5 '+str(depth)
		
		nombre_del_archivo=name_salve_file+'/File_hyp/codex.phs'



			
			
		for j in arreglo:
			fo = open(nombre_del_archivo, 'a')
			fo.write(j[0])
			fo.write('\n')
				#print j[0]
		fo.write(trial)
		fo.write('\n')
		fo.close()



		p = subprocess.Popen(['./hyp1.40'],
                     		stdout = subprocess.PIPE,
                     		stdin  = subprocess.PIPE,
                     		stderr = subprocess.STDOUT )

			
		s=''
		line1='@codex.hyp\n'
		s+=line1
			

		out = p.communicate( s )
		#print out

		remove(nombre_del_archivo)


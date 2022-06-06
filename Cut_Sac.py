#!/usr/bin/env python

import subprocess
import glob

class Cut_Sac():

	def CutWindows(self, path1, path2, indicei, indicef):
		print ' Entra Cut_Sac'
		print 'origen', path1
		print ' guarda como', path2
		p = subprocess.Popen(['sac'],
                     		stdout = subprocess.PIPE,
                     		stdin  = subprocess.PIPE,
                     		stderr = subprocess.STDOUT )

		s = "echo on\n"
		line1='read '+path1+'\n'
		line2='cut '+str(int(indicei/100))+' '+str(int(indicef/100))+'\n'
		line3='read\n'
		line4='write '+path2+'\n'

		#s+='''
		#read ZA.COLM..HHZ.M.2006.027.000000.SAC
		#cut 18045 18100
		#read
		#write test.SAC
		#'''

		s+=line1
		s+=line2
		s+=line3
		s+=line4
		#for filename in glob.glob("*.SAC"):

    		#s += '''
       		#read %(file)s
       		#write 
       

    			#''' % ( {'file': filename }) 
		s += "quit\n"
		#print '========================================'
		#print s
		#print '========================================'

		out = p.communicate( s )
		print out


#inicio=Cut_Sac()
#nombre='ZA.COLM..HHZ.M.2006.027.000000.SAC'
#path1='/home/carlos/Escritorio/CODEX_2006/027'
#path2= '/home/carlos/Escritorio/a_res'
#name_salve='Cut_prueba.SAC'
#indice_inicial=18045
#indice_final=18100

#inicio.CutWindows(nombre, path1, path2, name_salve, indice_inicial, indice_final)

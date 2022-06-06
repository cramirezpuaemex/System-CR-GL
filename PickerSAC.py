#!/usr/bin/env python
from os import remove
import os
import subprocess
import glob
class PickerSAC():

	def main(self, nombre, opc):
		
		
		p = subprocess.Popen(['sac'],
                     		stdout = subprocess.PIPE,
                     		stdin  = subprocess.PIPE,
                     		stderr = subprocess.STDOUT )

		s = "echo on\n"

		#filename=self.nombre
		#print filename
		s += '''
   			read %(file)s
   			apk

		''' % ( {'file': nombre} )
		s += "quit()\n"
		busqueda_s_apk=s.find('apk')
		busqueda_s_quit=s.find('quit')
		aux_s=s[0:12]+s[15:busqueda_s_apk-4]+s[busqueda_s_apk:busqueda_s_quit-2]+s[busqueda_s_quit:busqueda_s_quit+7]
		s=aux_s
		#print len(s)
		#for i in range(len(s)):
			#print 'i:', i, s[i]
		out = p.communicate( s )
		a=out[0]
		#print a
		busqueda=a.find('apk')
		#print 'busqueda', busqueda
		#print '*************************************************+++'
		b=a[busqueda+5:busqueda+30]
		c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
		if opc==-2:
			if c =='WARNING' or c== ' ERROR ':
				#print 'No encontro picker'
				if os.path.isfile(nombre):
					remove(nombre)
				b=-1
				return b
			else:
				if os.path.isfile(nombre):
					remove(nombre)
				#remove(nombre)
				return b
		else:
			if c =='WARNING' or c== ' ERROR ':
				#print 'No encontro picker'
				#remove(nombre)
				#if os.path.isfile(nombre):
					#remove(nombre)
				b=-1
				return b
			else:
				#if os.path.isfile(nombre):
					#remove(nombre)
				return b			


#nombre='/home/carlos/Escritorio/Resutados_Imple_Doc/036.COMA.2006.036.10.23.23.COMA.ZA.HHZ.SAC'
#inicia=PickerSAC()
#respuesta=inicia.main(nombre)
#print respuesta
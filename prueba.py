#!/usr/bin/env python
from os import remove
import subprocess
import glob

class prueba(object):
 	"""docstring for ClassName"""
 	def __init__(self):
 		super(prueba, self).__init__()
 		
 		self.nombre='036.COMA.2006.027.01.41.41.SCRI.ZA.HHZ.SAC'
		
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

		''' % ( {'file':self.nombre} )
		s += "quit()\n"
		out = p.communicate( s )
		a=out[0]
		print a
		print '*************************************************+++'
		b=a[181:205]
		c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]

		if c =='WARNING':
			print 'No encontro picker'
			remove(filename)
			b=-1
			return b
		else:
			return b

inicia=prueba()


#!/usr/bin/env python
from os import remove
import subprocess
import glob

p = subprocess.Popen(['sac'],
                     stdout = subprocess.PIPE,
                     stdin  = subprocess.PIPE,
                     stderr = subprocess.STDOUT )

s = "echo on\n"
nombre='/home/carlos/Escritorio/036.COMA.2006.027.02.31.31.CANO.ZA.HHZ.SAC'
filename=nombre
print filename
s += '''
   read %(file)s
   apk

''' % ( {'file': filename } )
s += "quit()\n"
print len(s)
for i in range(len(s)):
	print 'i:', i, s[i]
out = p.communicate( s )
a=out[0]
print a

busqueda=a.find('apk')
print 'busqueda', busqueda
#print '*************************************************+++'
b=a[busqueda+5:busqueda+27]
c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]

print 'Carlos', len(c)
for i in c:
	print i
if c =='WARNING':
	print 'No encontro picker'
	#remove(filename)
else:
	print b
#!/usr/bin/env python

import subprocess
import glob

p = subprocess.Popen(['sac'],
                     stdout = subprocess.PIPE,
                     stdin  = subprocess.PIPE,
                     stderr = subprocess.STDOUT )

s = "echo on\n"
for filename in glob.glob("*.SAC"):

    s += '''
       read %(file)s
       apk

    	''' % ( {'file': filename } )
s += "quit()\n"
out = p.communicate( s )
a=out[0]
print a
b=a[189:213]
print b
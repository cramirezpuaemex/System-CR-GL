
from Tkinter import Tk
import os
import os.path
from tkinter import filedialog
from Tkinter import *
import tkFileDialog
import subprocess
import glob
import copy as copy
class Cut_Files_SAC():
	def main(self):
		indicei= 39290
		indicef= 39550
		Tk().withdraw()
		#file=filedialog.askdirectory()
		file=tkFileDialog.askdirectory()
		archivos=os.listdir(file)
		archivos=sorted(archivos)
		directorios=[]
		path=[]
		for i in range(len(archivos)):
			archivos[i]= file+'/'+archivos[i]
			#if os.path.isdir(archivos[i])==True:
				#temp=os.listdir(archivos[i])
				#temp=sorted(temp)
				#for j in range(len(temp)):
					#if temp[j].find('.SAC')!=-1:
						#path.append(archivos[i]+'/'+temp[j])


		for i in range(len(archivos)):
			if archivos[i].find('.SAC')!=-1:
				path.append(archivos[i])

		#path= archivos
		print len(path)



		Tk().withdraw()
		file2=tkFileDialog.askdirectory()
		path2=os.listdir(file2)
		path2=sorted(path2)
		for i in range(len(path2)):
			path2[i]=file2+'/'+path2[i]
		#print 'asasasasasas', path2
		

		print len(path2)
		estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']
		lista1=[]
		for i in path:
			lista1.append(i)

		aux_e=[]
		lista2 = []
		aux2=''
		for e in estaciones:
			
			for x in lista1:
				if x.find(e)!=-1:
					aux2=e
					if e not in aux_e: 
						aux_e.append(e)
		print aux_e
		for e in aux_e:
			for x in path2:
				if x.find(e) !=-1:
					lista2.append(x)
		path1=[]
		for e in aux_e:
			for x in range(len(path)):

				if path[x].find(e) !=-1 and path[x] not in path1:
					print path[x]
					print e
					path1.append(path[x])



		print 'lista2 estaciones', len(lista2)	
		print 'lista3 ejemplos', len(path1)	

							
		#for i in range(len(path)):
			#print path[i]
			#print lista2[i]

		
		for i in range(len(path1)):



			p = subprocess.Popen(['sac'],
                     		stdout = subprocess.PIPE,
                     		stdin  = subprocess.PIPE,
                     		stderr = subprocess.STDOUT )

			s = "echo on\n"
			line1='read '+lista2[i]+'\n'
			line2='cut '+str(indicei)+' '+str(indicef)+'\n'
			line3='read\n'
			line4='write '+path1[i]+'\n'



			s+=line1
			s+=line2
			s+=line3
			s+=line4

       

 
			s += "quit()\n"
			#print '========================================'
			#print s
			#print '========================================'

			out = p.communicate( s )
			#print out

			
inicio=Cut_Files_SAC()


inicio.main()

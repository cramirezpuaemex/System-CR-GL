from tkinter import filedialog
from Tkinter import *
import tkFileDialog
import subprocess
import glob
from Tkinter import Tk
import os
import os.path
from tkinter import messagebox



class Promedio_Magnitud():
	def main(self, path_salve, id_file):

		print "*******************************************************"
		print "Comienza a realizar el concentrado del Coda magnitude"
		print "*******************************************************"
		print "\n"
		Tk().withdraw()
		#file=filedialog.askdirectory()
		file=path_salve+id_file+'/'
		print "*******************************************************"
		print "path file coda magnitude is: ", file
		print "*******************************************************"
		print "\n"
		#file=tkFileDialog.askdirectory(initialdir = "/home",title = "Path of magnitude coda")
		archivos=os.listdir(file)
		archivos=sorted(archivos)
		directorios=[]


		path=[]
		path= archivos
		'''
		for i in range(len(archivos)):
			archivos[i]= file+'/'+archivos[i]
			print archivos[i]
			if os.path.isdir(archivos[i])==True:
				temp=os.listdir(archivos[i])
				temp=sorted(temp)
				print "temp", temp
				for j in range(len(temp)):
					if temp[j].find('.txt')!=-1:

						path.append(archivos[i]+'/'+temp[j])
						print "++++", archivos[i]+'/'+temp[j]
			else:
				path.append(archivos[i])
		'''
		print "---------------------"
		#for i in path:
			#print i
		print "---------------------"
		############################################################################################################################################################################################################
		grado_0=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_3=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_4=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_5=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_6=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_7=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_8=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_9=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		grado_10=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		for i in path:
			
			i=file+i
			print "i: ", i
			f = open(i,"r")
			self.arreglo= []
			contLin=0
			while True:
				linea = f.readline()
				if linea:
					datos = linea.split('\n')
					datos = datos[0].split(',')
					index=  datos[0].find('Magnitud:')
					valor=datos[0][index+10:len(datos[0])]
					self.arreglo.append(valor)


				##print  len(datos) 
					#try:
						#data = [decimal.Decimal(elemento) for elemento in datos]
						#contLin=contLin+1
						#print  contLin
						#self.arreglo.append(data)
					#except Exception, e:
						#print  e
				else:
					break

			print "//////////////////"
			for i in self.arreglo:
				print i
			print "/////////////////"
			promedio=0
			aux=0
			for i in self.arreglo:
				aux+=float(i)
			promedio=float(aux)/len(self.arreglo)
			print 'termina de leer el archivo'
			print self.arreglo
			print promedio
			
			#fo = open(Promedio_Magnitud'.txt', 'a')
			#fo.write(promedio)
			#fo.write('\n')
			#fo.close()
			if promedio >=  0 and promedio<0.1:
				grado_0[0]+=1
			elif promedio >=  0.1 and promedio<0.2:
				grado_0[1]+=1
			elif promedio >=  0.2 and promedio<0.3:
				grado_0[2]+=1
			elif promedio >=  0.3 and promedio<0.4:
				grado_0[3]+=1
			elif promedio >=  0.4 and promedio<0.5:
				grado_0[4]+=1
			elif promedio >=  0.5 and promedio<0.6:
				grado_0[5]+=1
			elif promedio >=  0.6 and promedio<0.7:
				grado_0[6]+=1
			elif promedio >=  0.7 and promedio<0.8:
				grado_0[7]+=1
			elif promedio >=  0.8 and promedio<0.9:
				grado_0[8]+=1
			elif promedio >=  0.9 and promedio<1.0:
				grado_0[9]+=1
			elif promedio >=  1.0 and promedio<1.1:
				grado_1[0]+=1
			elif promedio >=  1.1 and promedio<1.2:
				grado_1[1]+=1
			elif promedio >=  1.2 and promedio<1.3:
				grado_1[2]+=1
			elif promedio >=  1.3 and promedio<1.4:
				grado_1[3]+=1
			elif promedio >=  1.4 and promedio<1.5:
				grado_1[4]+=1
			elif promedio >=  1.5 and promedio<1.6:
				grado_1[5]+=1
			elif promedio >=  1.6 and promedio<1.7:
				grado_1[6]+=1
			elif promedio >=  1.7 and promedio<1.8:
				grado_1[7]+=1
			elif promedio >=  1.8 and promedio<1.9:
				grado_1[8]+=1
			elif promedio >=  1.9 and promedio<2.0:
				grado_1[9]+=1
			elif promedio >=  2.0 and promedio<2.1:
				grado_2[0]+=1
			elif promedio >=  2.1 and promedio<2.2:
				grado_2[1]+=1
			elif promedio >=  2.2 and promedio<2.3:
				grado_2[2]+=1
			elif promedio >=  2.3 and promedio<2.4:
				grado_2[3]+=1
			elif promedio >=  2.4 and promedio<2.5:
				grado_2[4]+=1
			elif promedio >=  2.5 and promedio<2.6:
				grado_2[5]+=1
			elif promedio >=  2.6 and promedio<2.7:
				grado_2[6]+=1
			elif promedio >=  2.7 and promedio<2.8:
				grado_2[7]+=1
			elif promedio >=  2.8 and promedio<2.9:
				grado_2[8]+=1
			elif promedio >=  2.9 and promedio<3.0:
				grado_2[9]+=1
			elif promedio >=  3.0 and promedio<3.1:
				grado_3[0]+=1
			elif promedio >=  3.1 and promedio<3.2:
				grado_3[1]+=1
			elif promedio >=  3.2 and promedio<3.3:
				grado_3[2]+=1
			elif promedio >=  3.3 and promedio<3.4:
				grado_3[3]+=1
			elif promedio >=  3.4 and promedio<3.5:
				grado_3[4]+=1
			elif promedio >=  3.5 and promedio<3.6:
				grado_3[5]+=1
			elif promedio >=  3.6 and promedio<3.7:
				grado_3[6]+=1
			elif promedio >=  3.7 and promedio<3.8:
				grado_3[7]+=1
			elif promedio >=  3.8 and promedio<3.9:
				grado_3[8]+=1
			elif promedio >=  3.9 and promedio<4.0:
				grado_3[9]+=1
			elif promedio >=  4.0 and promedio<4.1:
				grado_4[0]+=1
			elif promedio >=  4.1 and promedio<4.2:
				grado_4[1]+=1
			elif promedio >=  4.2 and promedio<4.3:
				grado_4[2]+=1
			elif promedio >=  4.3 and promedio<4.4:
				grado_4[3]+=1
			elif promedio >=  4.4 and promedio<4.5:
				grado_4[4]+=1
			elif promedio >=  4.5 and promedio<4.6:
				grado_4[5]+=1
			elif promedio >=  4.6 and promedio<4.7:
				grado_4[6]+=1
			elif promedio >=  4.7 and promedio<4.8:
				grado_4[7]+=1
			elif promedio >=  4.8 and promedio<4.9:
				grado_4[8]+=1
			elif promedio >=  4.9 and promedio<5.0:
				grado_4[9]+=1
			elif promedio >=  5.0 and promedio<5.1:
				grado_5[0]+=1
			elif promedio >=  5.1 and promedio<5.2:
				grado_5[1]+=1
			elif promedio >=  5.2 and promedio<5.3:
				grado_5[2]+=1
			elif promedio >=  5.3 and promedio<5.4:
				grado_5[3]+=1
			elif promedio >=  5.4 and promedio<5.5:
				grado_5[4]+=1
			elif promedio >=  5.5 and promedio<5.6:
				grado_5[5]+=1
			elif promedio >=  5.6 and promedio<5.7:
				grado_5[6]+=1
			elif promedio >=  5.7 and promedio<5.8:
				grado_5[7]+=1
			elif promedio >=  5.8 and promedio<5.9:
				grado_5[8]+=1
			elif promedio >=  5.9 and promedio<6.0:
				grado_5[9]+=1
			elif promedio >=  6.0 and promedio<6.1:
				grado_6[0]+=1
			elif promedio >=  6.1 and promedio<6.2:
				grado_6[1]+=1
			elif promedio >=  6.2 and promedio<6.3:
				grado_6[2]+=1
			elif promedio >=  6.3 and promedio<6.4:
				grado_6[3]+=1
			elif promedio >=  6.4 and promedio<6.5:
				grado_6[4]+=1
			elif promedio >=  6.5 and promedio<6.6:
				grado_6[5]+=1
			elif promedio >=  6.6 and promedio<6.7:
				grado_6[6]+=1
			elif promedio >=  6.7 and promedio<6.8:
				grado_6[7]+=1
			elif promedio >=  6.8 and promedio<6.9:
				grado_6[8]+=1
			elif promedio >=  6.9 and promedio<7.0:
				grado_6[9]+=1
			elif promedio >=  7.0 and promedio<7.1:
				grado_7[0]+=1
			elif promedio >=  7.1 and promedio<7.2:
				grado_7[1]+=1
			elif promedio >=  7.2 and promedio<7.3:
				grado_7[2]+=1
			elif promedio >=  7.3 and promedio<7.4:
				grado_7[3]+=1
			elif promedio >=  7.4 and promedio<7.5:
				grado_7[4]+=1
			elif promedio >=  7.5 and promedio<7.6:
				grado_7[5]+=1
			elif promedio >=  7.6 and promedio<7.7:
				grado_7[6]+=1
			elif promedio >=  7.7 and promedio<7.8:
				grado_7[7]+=1
			elif promedio >=  7.8 and promedio<7.9:
				grado_7[8]+=1
			elif promedio >=  7.9 and promedio<8.0:
				grado_7[9]+=1
			elif promedio >=  8.0 and promedio<9.1:
				grado_8[0]+=1
			elif promedio >=  8.1 and promedio<9.2:
				grado_8[1]+=1
			elif promedio >=  8.2 and promedio<9.3:
				grado_8[2]+=1
			elif promedio >=  8.3 and promedio<9.4:
				grado_8[3]+=1
			elif promedio >=  8.4 and promedio<9.5:
				grado_8[4]+=1
			elif promedio >=  8.5 and promedio<9.6:
				grado_8[5]+=1
			elif promedio >=  8.6 and promedio<9.7:
				grado_8[6]+=1
			elif promedio >=  8.7 and promedio<9.8:
				grado_8[7]+=1
			elif promedio >=  8.8 and promedio<9.9:
				grado_8[8]+=1
			elif promedio >=  8.9 and promedio<9.0:
				grado_8[9]+=1

		Total=0
		fo = open(path_salve+'/'+'Mc_'+id_file+'.txt', 'a')

		for i in range(len(grado_0)):
			if grado_0[i]!=0:
				print 'Total del Grado 0.', i, 'es: ', grado_0[i]
				fo.write('Total del Grado 0.'+str(i)+'es: '+str(grado_0[i]))
				fo.write('\n')

				Total+=grado_0[i]
		for i in range(len(grado_1)):
			if grado_1[i]!=0:
				print 'Total del Grado 1.', i, 'es: ', grado_1[i]
				fo.write('Total del Grado 1.'+str(i)+'es: '+str(grado_1[i]))
				fo.write('\n')
				Total+=grado_1[i]
		for i in range(len(grado_2)):
			if grado_2[i]!=0:
				print 'Total del Grado 2.', i, 'es: ', grado_2[i]
				fo.write('Total del Grado 2.'+str(i)+'es: '+str(grado_2[i]))
				fo.write('\n')
				Total+=grado_2[i]
		for i in range(len(grado_3)):
			if grado_3[i]!=0:
				print 'Total del Grado 3.', i, 'es: ', grado_3[i]
				fo.write('Total del Grado 3.'+str(i)+'es: '+str(grado_3[i]))
				fo.write('\n')
				Total+=grado_3[i]
		for i in range(len(grado_4)):
			if grado_4[i]!=0:
				print 'Total del Grado 4.', i, 'es: ', grado_4[i]
				fo.write('Total del Grado 4.'+str(i)+'es: '+str(grado_4[i]))
				fo.write('\n')
				Total+=grado_4[i]
		for i in range(len(grado_5)):
			if grado_5[i]!=0:
				print 'Total el Grado 5.', i, 'es: ', grado_5[i]
				fo.write('Total del Grado 5.'+str(i)+'es: '+str(grado_5[i]))
				fo.write('\n')
				Total+=grado_5[i]
		for i in range(len(grado_6)):
			if grado_6[i]!=0:
				print 'Total del Grado 6.', i, 'es: ', grado_6[i]
				fo.write('Total del Grado 6.'+str(i)+'es: '+str(grado_6[i]))
				fo.write('\n')
				Total+=grado_6[i]
		for i in range(len(grado_7)):
			if grado_7[i]!=0:
				print 'Total del Grado 7.', i, 'es: ', grado_7[i]
				fo.write('Total del Grado 7.'+str(i)+'es: '+str(grado_7[i]))
				fo.write('\n')
				Total+=grado_7[i]
		for i in range(len(grado_8)):
			if grado_8[i]!=0:
				print 'Total del Grado 8.', i, 'es: ', grado_8[i]
				fo.write('Total del Grado 8.'+str(i)+'es: '+str(grado_8[i]))
				fo.write('\n')
				Total+=grado_8[i]

		print 'print numero total de eventos analisados: ', Total

		fo.write('number of event seismic: '+str(Total))
		fo.close()
		messagebox.showinfo(message="process completed successfully", title="Message")

#inicia= Promedio_Magnitud()

#file="/home/carlos/Escritorio/MagnitudPrueba/Magnitud_2006/"
#year="2006"

#inicia.main(file, year)
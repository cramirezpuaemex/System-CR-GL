import subprocess
import glob
from Cut_Sac import *

class Buscar_picker():
	def main(self, indicei, indicef):
		#indicei='41509'
		#indicef='41624'
		estaciones=['ALPI', 'BAVA', 'CANO', 'CDGZ', 'COLM', 'COMA', 'CUAT','EBMG', 'ESPN', 'GARC','HIGA', 'JANU', 'MAZE', 'MORA', 'OLOT', 'PAVE', 'PERC', 'SANM', 'SCRI', 'SINN', 'SNID', 'ZAPO']

		dia=['027']
		aa=indicei
		ba=indicef
		opc=-2
		time_arrive=[]
		names=[]
		for j in range(len(dia)):
	
			for i in range(len(estaciones)):

				p = subprocess.Popen(['sac'],
								stdout = subprocess.PIPE,
    							stdin  = subprocess.PIPE,
    							stderr = subprocess.STDOUT)
				s=''
				path1='/home/carlos/Escritorio/CODEX_2006/'+dia[j]+'/ZA.'+estaciones[i]+'..HHZ.M.2006.027.000000.SAC'
				#print path1

				s = "echo on\n"
				line1='read '+path1+'\n'
				line2='cut '+str(aa)+' '+str(ba)+'\n'
				line3='read\n'
				line4='apk\n'
				s+=line1
				s+=line2
				s+=line3
				s+=line4

				s += "quit()\n"

				#print '========================================'
				#print s
				#print '========================================'

		
				out = p.communicate(s)
				a=out[0]

				#print a
				busqueda=a.find('apk')
				#print 'busqueda', busqueda
				#print '*************************************************+++'
				b=a[busqueda+5:busqueda+30]
				c=b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
				#print '******'
				#print c
				#print '******'
				if opc==-2:
					if c =='WARNING' or c== ' ERROR ':
						#print 'No encontro picker'
				
						b=-1
						#print b

					else:
						aux=''
						name_Z=b[0:8]
						year=b[8:11]
						month=b[11:13]
						day=b[13:15]
						hour=b[15:17]
						minutos=b[17:19]
						sec=b[19:24]
						name_full=''
						name_full+=name_Z
						#Crea formato de deteccion de la onda P
						for i in range(len(year)):
							if i==0:
								aux=aux+'2'
							elif i==1:
								aux=aux+'0'
							else:
								aux=aux+'0'
								aux=aux+year[i]
					
						aux=aux+' '

						for i in range(len(month)):
							if month[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+month[i]
						aux=aux+' '
						for i in range(len(day)):
							if day[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+day[i]
						aux=aux+' '
						for i in range(len(hour)):	
							if hour[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+hour[i]
						aux=aux+' '
						for i in range(len(minutos)):
							if minutos[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+minutos[i]
						#nombre_archivo=aux
						#nombre_archivo = nombre_archivo.replace(" ", ".")
						aux=aux+' '

						for i in range(len(sec)):
							if sec[i]==' ':
								aux=aux+'0'
							else:
								aux=aux+sec[i]
						time_arrive.append(aux)
						names.append(name_full+' '+aux)
		
		if len(names)>2:
			delay=[]
			suma=0
			for i in range(len(time_arrive)):
				for j in range(len(time_arrive)):
					n=float(time_arrive[i][14:16]+'.'+time_arrive[i][17:19])
					m=float(time_arrive[j][14:16]+'.'+time_arrive[j][17:19])
					delay.append(n-m)

				for k in delay:
					suma+=abs(k)
					prom=float(suma/len(delay))
				print prom
				print time_arrive[i]
				print names[i]
		
				if prom < 0.5:
					print '+++++++++++++++++++++++++++'
					print prom
					print time_arrive[i]
					print names[i]
					print '+++++++++++++++++++++++++++'


inicio=Buscar_picker()
name='2006.027.00.07.47.BAVA.ZA.HHZ.SAC'
#indicei='2576'  #'41509'
#indicef='2691'  #'41624'

indicei='41509'
indicef='41624'
inicio.main(indicei, indicef)
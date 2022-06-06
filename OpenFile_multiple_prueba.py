from tkinter import filedialog
from Tkinter import Tk
import os

class OpenFile():
	def main(self):
		Tk().withdraw()
		file=filedialog.askdirectory()
		archivos=os.listdir(file)
		archivos=sorted(archivos)
		path=[]
		for i in range(len(archivos)):
			archivos[i]= file+'/'+archivos[i]
			temp=os.listdir(archivos[i])
			temp=sorted(temp)
			for j in range(len(temp)):
				if temp[j].find('HHZ')!=-1:
					path.append(archivos[i]+'/'+temp[j])

		print len(path)

		for i in path:
			print i


inicia=OpenFile()
inicia.main()
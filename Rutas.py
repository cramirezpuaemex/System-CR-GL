from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkinter import filedialog
class Rutas():
	filename = ""
	def main(self, tipo):
		#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		#self.filenames = askopenfilename(initialdir = "/home",title = tipo, filetypes =(("all files","*.*"),)) # show an "Open" dialog box and return the path to the selected file
		#self.files = filedialog.askopenfilenames( initialdir="/home", title='Please selfiletypes = (("ect files',filetypes = (("SAC files","*.SAC"),("all files","*.*")))
		

		root4 = Tk()
		filename =  askopenfilename(initialdir = "/home",title = tipo,filetypes = (("all files","*.*"),("all files","*.*")))
		root4.destroy()
		return filename
#inicio=Rutas()
#archivos=inicio.main()




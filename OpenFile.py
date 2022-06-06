from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkinter import filedialog
class OpenFile():
	filename = ""
	def pathfile(self):
		Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
		#self.filenames = askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("SAC files","*.SAC"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
		self.files = filedialog.askopenfilenames( initialdir="/home", title='Please select files',filetypes = (("SAC files","*.SAC"),("all files","*.*")))
		return(self.files)

	'''
	def open(self):
		root = Tk()
		root.filename =  filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
		print (root.filename)
	'''
	def directorio(self)
	directorio = eg.diropenbox(msg="Abrir directorio:",
                           title="Control: diropenbox",
                           default='/home/')
inicio=OpenFile()

archivos=inicio.pathfile()
archivos=sorted(archivos)
for i in archivos:
	print i

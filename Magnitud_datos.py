
from tkinter import *
 

class Magnitud_datos():
 
	def Take_input(self):

		self.INPUT = self.inputtxt.get("1.0", "end-1c")
		print(self.INPUT)
		a=0
		if self.INPUT!="":
			self.root.destroy()
			print "*****"
			self.main()
			#print "INPUT", self.INPUT


	def datos_regreso(self):
		print "INPUT", self.INPUT
		return self.INPUT




	def Input_data(self):

		self.root = Tk()
		self.root.geometry("300x100")
		self.root.title(" Input name to identifier")
		#INPUT=""     
		self.inputtxt = Text(self.root, height = 2,
		                width = 35,
		                bg = "light yellow")
		 
		self.Display = Button(self.root, height = 2,
		                 width = 20,
		                 text ="Show",
		                 command = lambda:self.Take_input())
		 

		self.inputtxt.pack()
		self.Display.pack()
		mainloop()

	def main(self):

		
		print "finaliza"
	
#inicio=Magnitud_datos()
#inicio.Input_data()
#year=inicio.datos_regreso()
#print "year", year


from tkinter import *
from Rutas_Dir import *
from hyp_path import *

class option_multiple():
	def MenuPrincipal_localizacion(self):
		self.root10 = Tk()
		self.root10.geometry("400x400")
		#self.root.config(width=300, height=100)
		self.root10.title("Localizacion model velocity")
		#INPUT=""     

		 
		self.Display = Button(self.root10, height = 2,
		                 width = 40,
		                 text ="Create model velocity",
		                 command = lambda:self.main())

		self.Display2 = Button(self.root10, height = 2,
		                 width = 40,
		                 text ="Start localization",
		                 command = lambda:self.Localizacion())


		self.Display3 = Button(self.root10, height = 2,
		                 width = 40,
		                 text ="Quit",
		                 command = lambda:self.quit())
		#self.inputtxt.pack()
		self.Display.pack()
		self.Display2.pack()
		self.Display3.pack()

		mainloop()

	def quit(self):
		self.root10.destroy()

	def Localizacion(self):
		self.root10.destroy()
		inicio=hyp_path()
		inicio.main()
		messagebox.showinfo(message="process completed successfully", title="Message")
	def main(self):
		self.root10.destroy()
		self.vel=[]
		self.cap=[]
		Tipo=" Input the number of depth"
		self.Input_data(Tipo)
		self.menu()

		Tipo="Name of the model velocity"
		self.Input_data(Tipo)
		self.salve_file()

	def salve_file(self):
		inicio_Rutas_dir=Rutas_Dir()
		Tipo="path for salve model velocity"
		path_salve_model=inicio_Rutas_dir.pathfile(Tipo)
		fo = open(path_salve_model+'/'+self.INPUT +'.crh', 'a')

		fo.write(self.INPUT+'\n')
		for i in range(len(self.vel)):
			a1=(float(self.cap[i]))
			a2=(float(self.vel[i]))
			

			fo.write(str(a2)+'   '+str(a1)+'\n')
		fo.close()

		messagebox.showinfo(message="process completed successfully", title="Message")#


	def Capas(self):
	    #r.set( float(n1.get()) + float(n2.get()) )

	    print self.n1.get(), self.n2.get()
	    self.vel.append(self.n1.get())
	    self.cap.append(self.n2.get())
	    self.borrar()
	    self.root1211.destroy()
	    if len(self.vel)==int(self.INPUT):
	    	print "verifica"
	    	#self.root1211.destroy()
	    	print self.vel, self.cap
	    else:
	    	self.menu()

	def Velocity(self):
	    #r.set( float(n1.get()) - float(n2.get()) )
	    self.root1211.destroy()
	    self.borrar()

	def borrar(self):
	    self.n1.set("")
	    self.n2.set("")


	def menu(self):

		self.root1211 = Tk()
		self.root1211.config(bd=15)

		self.n1 = StringVar()
		self.n2 = StringVar()
		r = StringVar()
	
		Label(self.root1211, text="depth number "+str(len(self.vel))).pack()
		Entry(self.root1211, justify="center", textvariable=self.n1).pack()
		
		Label(self.root1211, text="Velocity number  "+str(len(self.vel))).pack()
		Entry(self.root1211, justify="center", textvariable=self.n2).pack()
		
		Label(self.root1211, text="").pack()  # Separador
		
		Button(self.root1211, text="ok", command=self.Capas).pack(side="left")
		Button(self.root1211, text="quit", command=self.Velocity).pack(side="left")
		
	

		self.root1211.mainloop()

 	def Take_input(self):

		self.INPUT = (self.inputtxt.get("1.0", "end-1c"))
		print(self.INPUT)
		a=0
		if self.INPUT!="":
			self.root12.destroy()
			print "*****"
			#self.Work(self.INPUT)
			#print "INPUT", self.INPUT
	



	def Input_data(self, tipo):

		self.root12 = Tk()
		self.root12.geometry("300x100")
		self.root12.title(tipo)
		#INPUT=""     
		self.inputtxt = Text(self.root12, height = 2,
		                width = 35,
		                bg = "light yellow")
		 
		self.Display = Button(self.root12, height = 2,
		                 width = 20,
		                 text ="ok",
		                 command = lambda:self.Take_input())
		 

		self.inputtxt.pack()
		self.Display.pack()
		mainloop()  

#inicio=option_multiple()
#inicio.MenuPrincipal_localizacion()
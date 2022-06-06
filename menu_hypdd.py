import tkinter as tk
from tkinter import ttk
from Tkinter import *

class menu_hypdd():
	def menu(self):
		self.root = tk.Tk()
		self.root.config(width=300, height=200)
		self.root.title("Module using HypoDD program")
		boton = ttk.Button(text="1.- Crear archivo de configuracion (inp)", command=self.settings)
		boton1 = ttk.Button(text="2.- Localizar usando HypoDD", command=self.HypoDD)
		boton2 = ttk.Button(text="3.- Crear archivo  station", command=self.station)
		boton3 = ttk.Button(text="Salir", command=self.salir)
		boton.place(x=10, y=20)
		boton1.place(x=10, y=50)
		boton2.place(x=10, y=80)
		boton3.place(x=100, y=120)
		self.root.mainloop()

	def settings(self):
		print ':)  ******* settings'

	def HypoDD(self):
		print ':)  ******* HypoDD'
	def station(self):
		print ':)  ******* station'
	def salir(self):
		#self.root = tk.Tk()
		self.root.destroy()


inicio_menu_hypdd=menu_hypdd()
inicio_menu_hypdd.menu()
from tkinter import *
import os, sys, time

class Screen(Frame):
	def __init__(self, surface=None, **kwargs):
		super().__init__(surface, **kwargs)

		self.surface = surface
		self.options = kwargs

	def build(self):
		text = Label(self, text="I am in the 'build' method!")
		text.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")

	def run(self):
		self.pack(fill=BOTH, expand=1)

class Main(Tk):
	def __init__(self):
		super().__init__()
		self.wm_attributes('-fullscreen', 1)

	def build(self):
		return Screen(self)

	def run(self):
		self.widget = self.build()
		
		try:
			self.widget.build()
			self.widget.run()
		except AttributeError:
			self.widget.pack(fill=BOTH, expand=1)

		self.mainloop()

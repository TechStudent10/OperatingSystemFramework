from tkinter import *

class Textbox(Label):
	def __init__(self, surface=None, text=None, **kwargs):
		super().__init__(surface, text=text, **kwargs)

		self.surface = surface
		self.text = text
		self.options = kwargs

	def center(self):
		self.place(x=0, y=0, relx=0.5, rely=0.5, anchor="center")

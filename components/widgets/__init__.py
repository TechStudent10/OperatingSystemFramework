from tkinter import *

class Textbox(Label):
	def __init__(self, surface=None, text=None, **kwargs):
		super().__init__(surface, text=text, **kwargs)

		self.surface = surface
		self.text = text
		self.options = kwargs

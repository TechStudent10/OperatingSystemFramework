from components import Main, Screen
from components.widgets import Textbox, TextInputBox, PushButton

# Example of costum widget:
# from components.widgets import InheirtWidget
# from tkinter import (
# 	Label,
# )
# class CostumTextBox(InheirtWidget):
# 	def __init__(self, surface=None, x=0, y=0, text="", **kwargs):
# 		super().__init__(surface, x, y, **kwargs)

# 		self.text = text
# 		# This is where the real fun begins:
# 		# We create a Label using _create from the InheirtWidget class (which also inheirts from the Widget class)
# 		# We pass in the: Class of the tkinter widget, The X position, The Y position (self.x and self.y are both created when we call super().__init__()), 
# 		# and last but not least, we define all the other options that the user passes in (self.options is created when we call super().__init__()). 
# 		self._create(Label, self.x, self.y, text=self.text, **self.options)

class MainScreen(Screen):
	def build(self):
		Textbox(self, text="Enter some text", x=850, y=200, font=('segoe ui', 20))
		textbox = TextInputBox(self, multiline=True)
		textbox.insert("Hello!")
		textbox.clear()
		textbox.center()

		button = PushButton(self, text="Get Input", x=900, y=800, command=lambda: Textbox(self, text=textbox.get(), x=900, y=900))

class ManOS(Main):
	def build(self):
		return MainScreen()

if __name__ == '__main__':
	main = ManOS()
	main.run()

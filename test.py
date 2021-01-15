from components import Main, Screen
from components.widgets import Textbox

class MainScreen(Screen):
	def build(self):
		textbox = Textbox(self, text="I am in a class!")
		textbox.center()

class ManOS(Main):
	def build(self):
		return MainScreen()

if __name__ == '__main__':
	main = ManOS()
	main.run()

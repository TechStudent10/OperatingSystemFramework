from components import Main, Screen
from components.widgets import Textbox, TextInputBox, PushButton

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

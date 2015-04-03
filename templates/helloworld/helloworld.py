
from kivy.uix.floatlayout import FloatLayout

class HelloWorld(FloatLayout):
    pass
    
from kivy.app import App

class HelloWorldApp(App):
    def build(self):
        return HelloWorld()
        
HelloWorldApp().run()

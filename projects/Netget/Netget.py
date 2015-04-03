
from kivy.uix.floatlayout import FloatLayout

class Netget(FloatLayout):
    pass
    
from kivy.app import App

class NetgetApp(App):
    def build(self):
        return Netget()
        
NetgetApp().run()


from kivy.uix.floatlayout import FloatLayout

class OJBX(FloatLayout):
    pass
    
from kivy.app import App

class OJBXApp(App):
    def build(self):
        return OJBX()
        
OJBXApp().run()

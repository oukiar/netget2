from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class Login(BoxLayout):
    def __init__(self, **kwargs):
        
        super(Login, self).__init__(size_hint=(None,None), size=(400,300), orientation='vertical', **kwargs)
        self.center = Window.center
        
        self.lb_superiormenu = Label(text='Tour    |    Sign up    |    Contact')
        
        self.lb_netget = Label(text='Netget', font_size=36)
        
        self.txt_username = TextInput(size_hint_y=None, height=50)
        self.txt_password = TextInput(size_hint_y=None, height=50)
        
        self.btn_submit = Button(text='Login')
        
        self.add_widget(self.lb_superiormenu)
        self.add_widget(self.lb_netget)
        self.add_widget(self.txt_username)
        self.add_widget(self.txt_password)
        self.add_widget(self.btn_submit)

class Netget(FloatLayout):
    def __init__(self, **kwargs):
        
        super(Netget, self).__init__(**kwargs)
        
        #de momento el background un solo color 
        #self.img_background = Image(source='background.jpg')
        #self.add_widget(self.img_background)
        
        #fondo
        with self.canvas.before:
            Color(.1, .1, .1, 1)  # colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)

        
        self.login = Login()
        self.login.btn_submit.bind(on_press=self.on_login)
        
        self.add_widget(self.login)
        
    def on_login(self, w):
        self.remove_widget(self.login)
        
        #self.img_loading = RotatingImage()
        #self.add_widget(self.img_loading)
        
        self.add_widget(Label(text='Iniciando sesion'))

if __name__ == '__main__':
    
    from kivy.base import runTouchApp
    
    runTouchApp(Netget() )

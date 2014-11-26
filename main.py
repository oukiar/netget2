from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock

from widget3D import Image3D, Widget3D
from utils import Request





class TextBox(TextInput):
    def __init__(self, **kwargs):
        super(TextBox, self).__init__(**kwargs)
    
    def insert_text(self, substring, from_undo=False):
        print substring
        
        #if TAB was pressed
        if substring == '\t':
            #set the focus to the next children
            self.parent.children[self.parent.children.index(self)-1].focus = True
            return
        
        super(TextBox, self).insert_text(substring)
        
    def on_focus(self, w, val):
        if val == True:
            print "Selecting all text"
            self.select_all()
            
        super(TextBox, self).on_focus(w, val)

class Searcher(Widget3D):
    def __init__(self, **kwargs):
        super(Searcher, self).__init__(pos_z=-280, pos_y=170, pos_x=-50, **kwargs)
        
        
        self.layout = BoxLayout(size_hint=(None,None), width=300, height=30)
        
        self.img_find = Image(source='find_48x48.png', size_hint_x=None, width=50)
        self.layout.add_widget(self.img_find)
        
        self.txt_search = TextBox(text='Keywords to search ...')
        self.layout.add_widget(self.txt_search)
        
        
        self.btn_search = Button(text='Send', size_hint_x=None, width=70)
        self.layout.add_widget(self.btn_search)
        
        self.add_widget(self.layout)

class Loading(Image3D):
    def __init__(self, **kwargs):
        super(Loading, self).__init__(size_hint=(None, None), size=(70,70), **kwargs)
        
        self.reanimate()
        
    def reanimate(self, anim=None, w=None):
        self.rotate_z = 0
        self.anim = Animation(rotate_z=360, duration=1)
        self.anim.bind(on_complete=self.reanimate)
        self.anim.start(self)
        
class SignUp(Popup):
    def __init__(self, **kwargs):
        
        super(SignUp, self).__init__(title='Sign Up', size_hint=(None,None), size=(400,300), **kwargs)
        
        self.layout = BoxLayout(padding=30, spacing=5, orientation='vertical')
        
        self.email = TextBox(text='Email')
        self.username = TextBox(text='Username')
        self.password = TextBox(text='Password', password=True)
        self.rpassword = TextBox(text='Retype Password', password=True)
        
        self.btn_submit = Button(text='Sign Up', size_hint_x=.7)
        
        self.layout.add_widget(self.email)
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.password)
        self.layout.add_widget(self.rpassword)
        self.layout.add_widget(self.btn_submit)
        
        self.content = self.layout
    

class Login(BoxLayout):
    def __init__(self, **kwargs):
        
        super(Login, self).__init__(size_hint=(None,None), size=(400,300), orientation='vertical', **kwargs)
        self.center = Window.center
        
        self.lb_superiormenu = Label(text='Tour    |    [ref=signup]Sign up[/ref]    |    Contact', markup=True)
        
        
        self.lb_netget = Label(text='Netget', font_size=36)
        
        self.txt_username = TextInput(size_hint_y=None, height=50)
        self.txt_password = TextInput(size_hint_y=None, height=50)
        
        self.btn_submit = Button(text='Login')
        
        self.add_widget(self.lb_superiormenu)
        self.add_widget(self.lb_netget)
        self.add_widget(self.txt_username)
        self.add_widget(self.txt_password)
        self.add_widget(self.btn_submit)
        
      
class CenterLog(BoxLayout):
    def __init__(self, **kwargs):
        
        super(CenterLog, self).__init__(orientation='vertical', **kwargs)
        
    def add_widget(self, w, index=0):
        
        if len(self.children) > 0:

            anim = Animation(opacity=1, height=w.height, duration=1)
            w.height -= 50
            w.opacity = 0
            anim.start(w)
        
        super(CenterLog, self).add_widget(w, index)
    
    

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
        self.login.lb_superiormenu.bind(on_ref_press=self.on_headerloginpress)
        
        self.add_widget(self.login)


        self.searcher = Searcher()
        
    def on_login(self, w):
        self.remove_widget(self.login)
        
        #enviar peticion de login al servidor principal
        
        
        #poner icono de loading
        self.imgloading = Loading(source='loading.png')
        self.add_widget(self.imgloading)
        
        self.boxlogin = CenterLog()
        
        self.boxlogin.add_widget(Label(text='[color=000000]Iniciando sesion ...[/color]', markup=True))
        
        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancelar inicio de sesion[/color]', markup=True))
        
        self.add_widget(self.boxlogin)
        
        #set the event for create the cancel option ... 
        Clock.schedule_once(self.on_sendsignupdata, 3)
        

        
    def on_headerloginpress(self, w, value):
        if value == 'signup':
            self.remove_widget(self.login)
            
            self.signup = SignUp()
            self.signup.open()
            self.signup.btn_submit.bind(on_press=self.on_signup)
            
    def on_signup(self, w):
        

        self.signup.dismiss()
        
        #----------
        
        #poner icono de loading
        self.imgloading = Loading(source='loading.png')
        self.add_widget(self.imgloading)
        
        self.boxlogin = CenterLog()
        
        self.boxlogin.add_widget(Label(text='[color=000000]Signing up in the netget network[/color]', markup=True))

        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancelar inicio de sesion[/color]', markup=True, size_hint_y=None, height=500))
        
        #set the event for create the cancel option ... 
        Clock.schedule_once(self.on_sendsignupdata, 3)
        
        self.add_widget(self.boxlogin)

    def on_sendsignupdata(self, dt):
        
        #datos POST que se enviaran al script PHP
        data = {'email':self.signup.email.text,
                'username':self.signup.username.text,
                'password':self.signup.password.text
                }
        
        #intentar crear cuenta
        Request(action='http://www.orgboat.com/netget/ngsignup.php', data=data, callback=self.res_signup)
        
        
    def res_signup(self, response):
        if response == "OK":
            
            print "Signup succesfull"
            
            self.remove_widget(self.imgloading)
            self.remove_widget(self.boxlogin)

            self.add_widget(self.searcher)

if __name__ == '__main__':
    
    from kivy.base import runTouchApp
    
    runTouchApp(Netget() )

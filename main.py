

'''
Netget p2p networking for anything


Neurons Art & Technology 2012-2014 All rights reserved.
'''

#imports of kivy stuff
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
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

#devslib imports
from widget3D import Image3D, Widget3D
from utils import Request, alert, MessageBoxTime, fade_in

#rest of libraries
import json

class Test3D(Widget3D):
    def __init__(self, **kwargs):
        '''
        Test the correction of coords from 3Dview to 2Dview
        '''
        
        ratio = float(Window.width)/Window.height
        
        xratiofix = 100.0/(Window.width/2)*ratio
        yratiofix = 100.0/(Window.height/2)
        
        super(Test3D, self).__init__(pos_x=-1*ratio, pos_y=-1, scale_x=1.0/100*xratiofix, scale_y=1.0/100*yratiofix, pos_z=-1, **kwargs)
        
        
        
        self.add_widget(Button(text='Hi', size_hint=(None,None),  ))

class TextBox(TextInput):
    def __init__(self, **kwargs):
        super(TextBox, self).__init__(**kwargs)
    
    def insert_text(self, substring, from_undo=False):
        #print substring
        
        #if TAB was pressed
        if substring == '\t':
            #set the focus to the next children
            #self.parent.children[self.parent.children.index(self)-1].focus = True
            return
                
        super(TextBox, self).insert_text(substring)
        
    def on_focus(self, w, val):
        super(TextBox, self).on_focus(w, val)
        
        if val == True:
            Clock.schedule_once(self.select_alltext, 0)
            
    def select_alltext(self, dt):
        self.select_all()


class Loading(Image3D):
    def __init__(self, **kwargs):
        super(Loading, self).__init__(size_hint=(None, None), size=(2,2), **kwargs)
        
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
        
        self.message = Label(markup=True)
        
        self.layout.add_widget(self.email)
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.password)
        self.layout.add_widget(self.rpassword)
        self.layout.add_widget(self.btn_submit)
        self.layout.add_widget(self.message)
        
        self.content = self.layout
    

class Login(BoxLayout):
    def __init__(self, **kwargs):
        
        super(Login, self).__init__(size_hint=(None,None), spacing=10, size=(400,300), orientation='vertical', **kwargs)
        self.center = Window.center
        
        self.lb_superiormenu = Label(text='Tour    |    [ref=signup]Sign up[/ref]    |    Contact', markup=True)
        
        
        self.lb_netget = Label(text='Netget', font_size=36)
        
        self.txt_username = TextBox(text='Username', size_hint_y=None, height=40)
        self.txt_password = TextBox(text='Password', size_hint_y=None, height=40, password=True)
        
        self.btn_submit = Button(text='Login')
        
        self.message = Label(markup=True)
        
        self.add_widget(self.lb_superiormenu)
        self.add_widget(self.lb_netget)
        self.add_widget(self.txt_username)
        self.add_widget(self.txt_password)
        self.add_widget(self.btn_submit)
        self.add_widget(self.message)
        
      
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

class ScrollBox(ScrollView):
    
    def __init__(self, **kwargs):
    
        self.orientation = kwargs.pop('orientation', 'vertical')
    
        super(ScrollBox, self).__init__(**kwargs)
            
        if self.orientation == 'vertical':
            self.layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
            self.layout.height = 0
        else:
            self.layout = BoxLayout(size_hint_x=None, spacing=10)
            self.layout.width = 0
    
    
        super(ScrollBox, self).add_widget(self.layout)
        
    def add_widget(self, w, index=0):
        
        self.layout.add_widget(w)
        
        if self.orientation == 'vertical':
            self.layout.height += (w.height + len(self.layout.children)*(self.layout.spacing/2))
        else:
            self.layout.width += (w.width + len(self.layout.children)*(self.layout.spacing/2))
    
class Searcher(AnchorLayout):
    def __init__(self, **kwargs):
        #super(Searcher, self).__init__(pos_z=-280, pos_y=170, pos_x=-50, **kwargs)
        super(Searcher, self).__init__(padding=10, anchor_x='center', anchor_y='top', **kwargs)
        
        self.layout = BoxLayout(size_hint=(None,None), width=300, height=30)
        
        self.img_find = Image(source='navigate.png', size_hint_x=None, width=50, allow_stretch=True)
        self.layout.add_widget(self.img_find)
        
        self.txt_search = TextBox(text='Keywords to search ...')
        self.layout.add_widget(self.txt_search)
        
        
        self.btn_search = Button(text='Search', size_hint_x=None, width=70)
        self.layout.add_widget(self.btn_search)
        
        self.add_widget(self.layout)
        
class ContactItem(BoxLayout):
    def __init__(self, **kwargs):
        
        super(ContactItem, self).__init__(size_hint_y=None, height=40, spacing=10, **kwargs)
    
        self.img_profile = Image(source=kwargs.get('profileimage'), 
                                    allow_stretch=True, 
                                    keep_ratio=False, 
                                    size_hint_x=None, 
                                    width=40)
                                    
        self.lb_nickcname = Label(text=kwargs.get('nickname'))
        
        self.add_widget(self.img_profile)
        self.add_widget(self.lb_nickcname)
        
        
        
'''
class FriendsList(ScrollBox):
    def __init__(self, **kwargs):
        
        super(FriendsList, self).__init__(size_hint_x=None, width=300, **kwargs)
    
        self.layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.layout.height = 0
    
        super(FriendsList, self).add_widget(self.layout)
        
    def add_widget(self, w, index=0):
        
        self.layout.add_widget(w)
        self.layout.height += (w.height + len(self.layout.children)*(self.layout.spacing/2))
'''

class NetgetUI(FloatLayout):
    '''
    Interfaz de usuario principal de netget, aqui es donde los usuarios interactuan
    en netget
    '''
    def __init__(self, **kwargs):
        
        super(NetgetUI, self).__init__(**kwargs)
    
        #SEARCHER
        self.searcher = Searcher()
        self.add_widget(self.searcher)
        self.searcher.btn_search.bind(on_release=self.on_search)
        
        #SEARCH RESULT
        
        #CONTACT LIST
        self.lst_friends = ScrollBox(orientation='vertical', size_hint_x=None, width=300)
        self.add_widget(self.lst_friends)
        
        #iniciar obtencion de contactos
        Clock.schedule_once(self.get_contacts, 1)
        
    def get_contacts(self, dt):
        print 'Obteniendo contactos'
        
    def on_search(self, w):
        print "Searching: ", self.searcher.txt_search.text
        
        Request(action='http://www.orgboat.com/netget/ngsearch.php', 
                data={'txt_search':self.searcher.txt_search.text}, 
                callback=self.res_search)
        
    def res_search(self, response):
        print 'Search response: ', response
        
        resdict = json.loads(response)
        
        for nick in resdict:
            usrID = resdict[nick]
            print "Nick: %s, ID: %s" % (nick, usrID)
            
            contact = ContactItem(profileimage='profile_32x32.png', nickname=nick)
            
            remoteimage = 'http://www.orgboat.com/netget/profilepictures/' + usrID + ".jpg"
            
            self.lst_friends.add_widget(contact)

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

        '''
        self.test3D = Test3D()
        self.add_widget(self.test3D)
        '''
        
    def on_login(self, w):
        self.remove_widget(self.login)
        
        #enviar peticion de login al servidor principal
        
        
        #poner icono de loading
        self.imgloading = Loading(source='loading_32x32.png')
        self.add_widget(self.imgloading)
        
        self.boxlogin = CenterLog()
        
        self.boxlogin.add_widget(Label(text='[color=EEEEEE]Iniciando sesion ...[/color]', markup=True, font_size=32))
        
        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancelar inicio de sesion[/color]', markup=True))
        
        self.add_widget(self.boxlogin)
        
        #set the event for create the cancel option ... 
        Clock.schedule_once(self.on_sendlogindata, 3)
        
    def on_sendlogindata(self, dt):
        
        #datos POST que se enviaran al script PHP
        data = {
                'username':self.login.txt_username.text,
                'password':self.login.txt_password.text
                }
        
        #intentar crear cuenta
        Request(action='http://www.orgboat.com/netget/nglogin.php', data=data, callback=self.res_login)
        
    def res_login(self, response):

        print response

        self.remove_widget(self.imgloading)
        self.remove_widget(self.boxlogin)
        
        if response == 'OK_LOGIN':
            print "Login succesfull"
            
            self.netgetui = NetgetUI()
            
            self.add_widget(self.netgetui)
            
        elif response == 'PASSDIFF_LOGIN':
            
            self.login.message.text = '[color=FF0000]Password incorrect[/color]'
            self.add_widget(self.login)
            
        elif response == 'USERFAIL_LOGIN':
            
            self.login.message.text = '[color=FF0000]User is not registered[/color]'
            self.add_widget(self.login)

        
    def on_headerloginpress(self, w, value):
        if value == 'signup':
            self.remove_widget(self.login)
            
            self.signup = SignUp()
            self.signup.open()
            self.signup.btn_submit.bind(on_press=self.on_signup)
            
    def on_signup(self, w):
        
        if self.signup.password.text != self.signup.rpassword.text:
            self.signup.message.text = "[color=FF0000]Passwords does not match[/color]"
            fade_in(self.signup.message)
            self.signup.password.focus = True
            return

        self.signup.dismiss()
        
        #----------
        
        #poner icono de loading
        self.imgloading = Loading(source='loading_32x32.png')
        self.add_widget(self.imgloading)
        
        self.boxlogin = CenterLog()
        
        self.boxlogin.add_widget(Label(text='[color=EEEE]Signing up in the netget network[/color]', font_size=32, markup=True))

        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancelar inicio de sesion[/color]', markup=True, size_hint_y=None, height=200))
        
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
        
        self.remove_widget(self.imgloading)
        self.remove_widget(self.boxlogin)
        
        if response == "OK":
            
            print "Signup succesfull"
            
            self.netgetui = NetgetUI()
            self.add_widget(self.netgetui)
            
        elif response == "EMAIL_EXISTS":
            
            self.signup.message.text = "[color=FF0000]Email is already in use[/color]"
            self.signup.open()
            
        elif response == "USER_EXISTS":
            
            self.signup.message.text = "[color=FF0000]The user already exists[/color]"
            self.signup.open()

if __name__ == '__main__':
    
    from kivy.base import runTouchApp
    
    runTouchApp(Netget() )



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

from kivy.uix.behaviors import ButtonBehavior

from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty

#devslib imports
from widget3D import Image3D, Widget3D
from utils import Request, alert, MessageBoxTime, fade_in
from scrollbox import ScrollBox

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


class ImageButton(ButtonBehavior, Image):
    pass
    
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
    
class ResultSearch(Popup):
    
    def __init__(self, **kwargs):
        
        super(ResultSearch, self).__init__(title='Search result', size_hint=(None,None), size=(300,500),  **kwargs)
        
        self.content = ScrollBox(orientation='vertical')
        
    
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
        
        #SEARCH RESULT
        #self.lst_result = ScrollBox(orientation='vertical')
        
        #self.layout.add_widget(self.lay_search)
        #self.layout.add_widget(self.lst_result)
        
        self.add_widget(self.layout)
        
class ContactMenu(Popup):
    
    def __init__(self, **kwargs):
        
        super(ContactMenu, self).__init__(title='Contact options', size_hint=(None,None), size=(200,150), **kwargs)
        
        self.content = BoxLayout(orientation='vertical')
        
        self.btn_chat_window = LabelOver(text='Open chat window')
        self.btn_publicshares = LabelOver(text='Open public shares')
        self.btn_deletecontact = LabelOver(text='Delete contact')
        
        self.content.add_widget( self.btn_chat_window )
        self.content.add_widget( self.btn_publicshares )
        self.content.add_widget( self.btn_deletecontact )
        
class ContactItem(BoxLayout):
    def __init__(self, **kwargs):
        
        self.contactID = kwargs.pop('contactID')
        self.bfriend = kwargs.pop('friend', False)
        
        super(ContactItem, self).__init__(size_hint_y=None, height=30, spacing=10, **kwargs)
    
        self.img_profile = ImageButton(source=kwargs.get('profileimage'), 
                                    allow_stretch=True, 
                                    keep_ratio=False, 
                                    size_hint_x=None, 
                                    width=30)
                                    
        self.lb_nickcname = Label(text=kwargs.get('nickname'))
        
        self.lb_nickcname.bind(size=self.fixLabelText )
        
        self.add_widget(self.img_profile)
        self.add_widget(self.lb_nickcname)
        
        if self.bfriend == False:
            self.btn_add = ImageButton(source='add_32x32.png', 
                                    allow_stretch=True, 
                                    keep_ratio=False, 
                                    size_hint_x=None, 
                                    width=30
                                    )
        
            self.add_widget(self.btn_add)
            
        else:
            self.btn_menu = ImageButton(source='menu_32x32.png', 
                                    allow_stretch=True, 
                                    keep_ratio=False, 
                                    size_hint_x=None, 
                                    width=30
                                    )
        
            self.add_widget(self.btn_menu)
                    
        
    def fixLabelText(self, w, val):
        '''
        Trickly fix for align text to left in a label
        '''
        w.text_size = val
        
        
        
class LabelOver(Button):
    def __init__(self, **kwargs):
        
        super(LabelOver, self).__init__(markup=True, **kwargs)
    
        #for mouse over event
        Window.bind(mouse_pos=self.check_over)
        
        self.opacity = .7
        
    def check_over(self, instance, value):
        if self.collide_point(value[0], value[1]):
            self.opacity = 1
        else:
            self.opacity = .7

class ProfileMenu(Popup):
    
    def __init__(self, **kwargs):
        
        super(ProfileMenu, self).__init__(title='Profile options', size_hint=(None,None), size=(150,150), **kwargs)
        
        self.content = BoxLayout(orientation='vertical')
        
        self.btn_editprofile = LabelOver(text='Edit profile')
        self.btn_godevices = LabelOver(text='Go to devices')
        self.btn_logout = LabelOver(text='Logout')
        
        self.content.add_widget( self.btn_editprofile )
        self.content.add_widget( self.btn_godevices )
        self.content.add_widget( self.btn_logout )
        
        
class ProfileAccess(BoxLayout):
    def __init__(self, **kwargs):
                
        super(ProfileAccess, self).__init__(size_hint=(None,None), size=(300,40), spacing=10, **kwargs)
        
        #profile picture snap
        self.img_profile = ImageButton(source='profile_32x32.png', 
                                    allow_stretch=True, 
                                    keep_ratio=False, 
                                    size_hint_x=None, 
                                    width=40)
        self.img_profile.bind(on_press=self.openmenu)
                                    
        self.txt_nickname = Label(markup=True, font_size=28)
        self.txt_nickname.bind(size=self.fixLabelText )
        
        self.add_widget(self.img_profile)
        self.add_widget(self.txt_nickname)
        
        self.menu = ProfileMenu()
        self.menu.btn_editprofile.bind(on_release=self.on_editprofile)
        
        self.btn_save = Button(text='Save', size_hint_x=None, width=50, on_press=self.save)
        
        
    def save(self, w):
        
        Request(action='http://www.orgboat.com/netget/ngsaveprofile.php', 
                data={'usrID':self.usrID, 'newnickname':self.txt_nickname.text}, 
                callback=self.res_save)
                
        self.remove_widget(self.btn_save)
        
        self.loading = Loading(source='gear-icon_128x128.png')
        
        self.add_widget( self.loading )
        
    def res_save(self, response):
        print "Save response: ", response
        
        self.remove_widget(self.loading)
        
        if response == "PROFILE_SAVED":
            
            nickname = self.txt_nickname.text
            self.remove_widget(self.txt_nickname)
            self.txt_nickname = Label(text=nickname, markup=True, font_size=28)
            self.txt_nickname.bind(size=self.fixLabelText )
            self.add_widget(self.txt_nickname)
        
        
    def fixLabelText(self, w, val):
        '''
        Trickly fix for align text to left in a label
        '''
        w.text_size = val
        
    def openmenu(self, w):
        print 'Editing profile'
        self.menu.open()
        self.menu.x = self.x
        self.menu.y = self.y - self.menu.height
        
        
    def on_editprofile(self, w):
        nickname = self.txt_nickname.text
        self.remove_widget(self.txt_nickname)
        
        self.txt_nickname = TextInput(text=nickname, font_size=28)
        self.add_widget(self.txt_nickname)
        
        #button for save
        self.add_widget(self.btn_save)
        
        self.menu.dismiss()
        
        self.txt_nickname.focus = True
        
        
        

class NetgetUI(FloatLayout):
    '''
    Interfaz de usuario principal de netget, aqui es donde los usuarios interactuan
    en netget
    '''
    
    usrID = StringProperty("-1")  # -1 means logout
    usrNickName = StringProperty()
    
    def __init__(self, **kwargs):
        
        super(NetgetUI, self).__init__(**kwargs)
    
        #SEARCHER
        self.searcher = Searcher()
        self.add_widget(self.searcher)
        self.searcher.btn_search.bind(on_release=self.on_search)
        
        self.left_box = BoxLayout(orientation='vertical', padding=20, size_hint_x=None, width=200)
        
        #NAT
        self.left_box.add_widget(Label(text='Neurons Art & Technology', size_hint_y=None, height=40))
        
        #PROFILE
        self.profile = ProfileAccess()
        
        
        self.profile.menu.btn_godevices.bind(on_release=self.on_godevices)
        
        self.left_box.add_widget(self.profile)
        
        
        
        #CONTACT LIST
        self.lst_friends = ScrollBox(orientation='vertical')
        self.left_box.add_widget(self.lst_friends)
        
        
        #
        self.add_widget(self.left_box)
                
        #RESULT SEARCH
        self.resultsearch = ResultSearch()
        
        #contact menu
        self.contactmenu = ContactMenu()
        
    def on_godevices(self, w):
        print 'Going to manage my devices'
        
        
    def on_usrID(self, w, val):
        self.profile.usrID = val
        
    def get_contacts(self, dt):
        print 'Obteniendo contactos'
        
        Request(action='http://www.orgboat.com/netget/nglistcontacts.php', 
                data={'usrID':self.usrID}, 
                callback=self.res_get_contacts)
                
    def res_get_contacts(self, response):
        print 'Contacts list: ', response
        
        
        self.lst_friends.layout.clear_widgets()
        self.lst_friends.layout.height = 0
        
        self.contactlistdata = json.loads(response)
        
        Clock.schedule_once(self.fill_contact_list, 0)
        
    def fill_contact_list(self, dt):
        
        for nick in self.contactlistdata:
            
            usrID = self.contactlistdata[nick]
            
            print "Nick: %s, ID: %s" % (nick, usrID)
            
            contact = ContactItem(contactID=usrID, profileimage='profile_32x32.png', nickname=nick, friend=True)
            contact.btn_menu.bind(on_release=self.on_contactmenu)
            
            remoteimage = 'http://www.orgboat.com/netget/profilepictures/' + usrID + ".jpg"
            
            self.lst_friends.add_widget(contact)
            
        fade_in(self.lst_friends)
        
        
    def on_contactmenu(self, w):
        
        self.contactmenu.open()
        print w.pos
        
        #self.contactmenu.x = w.x
        #self.contactmenu.y = w.y - self.contactmenu.height
        
    def on_search(self, w):
        print "Searching: ", self.searcher.txt_search.text
        
        Request(action='http://www.orgboat.com/netget/ngsearch.php', 
                data={'txt_search':self.searcher.txt_search.text}, 
                callback=self.res_search)
        
    def res_search(self, response):
        print 'Search response: ', response
        
        self.resultsearch.content.layout.clear_widgets()
        self.resultsearch.content.layout.height = 0
        
        self.resultsearchdata = json.loads(response)
        
        Clock.schedule_once(self.showresultsearch)
                
            
    def showresultsearch(self, dt):
        
        for nick in self.resultsearchdata:
            
            usrID = self.resultsearchdata[nick]
            
            print "Nick: %s, ID: %s" % (nick, usrID)
            
            contact = ContactItem(contactID=usrID, profileimage='profile_32x32.png', nickname=nick)
            contact.btn_add.bind(on_release=self.on_addcontact)
            
            remoteimage = 'http://www.orgboat.com/netget/profilepictures/' + usrID + ".jpg"
            
            self.resultsearch.content.add_widget(contact)
            
    
        self.resultsearch.open()
        
        
    def on_addcontact(self, w):
        
        self.resultsearch.dismiss()
        
        Request(action='http://www.orgboat.com/netget/ngaddcontact.php', 
                data={'usrID':self.usrID, 'friendID':w.parent.contactID}, 
                callback=self.res_addcontact)
        
    def res_addcontact(self, response):
        print 'Add contact response: ', response
        
        
        if "CONTACT_ADDED" in response:
            
            res, friendID, friendNickName = response.split(":")
        
            contact = ContactItem(contactID=friendID, profileimage='profile_32x32.png', nickname=friendNickName, friend=True)
            contact.btn_menu.bind(on_release=self.on_contactmenu)
            
            remoteimage = 'http://www.orgboat.com/netget/profilepictures/' + friendID + ".jpg"
            
            self.lst_friends.add_widget(contact)
        

class Netget(FloatLayout):
    def __init__(self, **kwargs):
        
        super(Netget, self).__init__(**kwargs)
        
        #de momento el background es de un solo color 
        #self.img_background = Image(source='background.jpg')
        #self.add_widget(self.img_background)
        
        self.login = Login()
        self.login.btn_submit.bind(on_press=self.on_login)
        self.login.lb_superiormenu.bind(on_ref_press=self.on_headerloginpress)
        
        self.add_widget(self.login)
        
        #self.add_widget(Searcher() )
        self.netgetui = NetgetUI()
        self.netgetui.profile.menu.btn_logout.bind(on_release=self.on_logout)

        '''
        self.test3D = Test3D()
        self.add_widget(self.test3D)
        '''
        
    def on_logout(self, w):
        print 'Loging out'
        
        self.netgetui.profile.menu.dismiss()
        self.remove_widget(self.netgetui)
        
        self.add_widget(self.login)
        fade_in(self.login)
        
    def on_size(self, instance, val):
        if self.canvas == None:
            return
        
        with self.canvas.before:
            Color(.1, .1, .1, 1)  # colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=Window.size)
        
        
    def on_login(self, w):
        self.remove_widget(self.login)
        
        #poner icono de loading
        self.imgloading = Loading(source='loading_32x32.png')
        self.add_widget(self.imgloading)
        
        self.boxlogin = CenterLog()
        
        self.boxlogin.add_widget(Label(text='[color=EEEEEE]Iniciando sesion ...[/color]', markup=True, font_size=32))
        
        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancelar inicio de sesion[/color]', markup=True, size_hint_y=None, height=200))
        
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
        
        if 'OK_LOGIN' in response:
            print "Login succesfull"
            
            res, usrID, usrNickName = response.split(':')
            
            self.netgetui.profile.txt_nickname.text = usrNickName
            
            self.netgetui.usrID = usrID
            self.netgetui.usrNickName = usrNickName
            
            Clock.schedule_once(self.netgetui.get_contacts, 1)
            
            self.add_widget(self.netgetui)
            fade_in(self.netgetui)
            
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

        self.boxlogin.add_widget(Label(text='[color=EE0000]Cancel subscription[/color]', markup=True, size_hint_y=None, height=200))
        
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
        
        if "OK" in response:
            
            print "Signup succesfull"
            
            res, usrID, usrNickName = response.split(':')
            
            self.netgetui.profile.txt_nickname.text = usrNickName
            
            self.netgetui.usrID = usrID
            self.netgetui.usrNickName = usrNickName
            
            
            self.add_widget(self.netgetui)
            fade_in(self.netgetui)
            
            
        elif response == "EMAIL_EXISTS":
            
            self.signup.message.text = "[color=FF0000]Email is already in use[/color]"
            self.signup.open()
            
        elif response == "USER_EXISTS":
            
            self.signup.message.text = "[color=FF0000]The user already exists[/color]"
            self.signup.open()

if __name__ == '__main__':
    
    from kivy.base import runTouchApp
    
    runTouchApp(Netget() )

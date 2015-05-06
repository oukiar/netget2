
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty
from kivy.animation import Animation

from ngvars import NGFactory

from devslib.widget3D import Loading, Widget3D

import md5 #FIXME, USE THE LIBSODIUM HASH
import json

'''


'''


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

class NetgetSession(FloatLayout):
    pass
  
class Msg(Popup):
    message = StringProperty()
  
  
class FriendsList(BoxLayout):
    pass
  
class NetgetLogin(AnchorLayout):
    txt_user = ObjectProperty()
    txt_pass = ObjectProperty()
    
class NetgetSignUp(Popup):
    txt_user = ObjectProperty()
    txt_pass = ObjectProperty()
    txt_rpass = ObjectProperty()
    
class NetgetBase(FloatLayout):
    login = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(NetgetBase, self).__init__(**kwargs)
        self.factory = NGFactory()
    
    def do_signup(self):
        print "Creating account"
    
        if len(self.signup.txt_user.text) > 5:
        
            if self.signup.txt_pass.text == self.signup.txt_rpass.text:
                
                #create password hash, that will be used as public key
        
                #encrypt password
                hashpass = md5.new()
                hashpass.update(self.signup.txt_pass.text)
                
    
                ngvar = self.factory.Extends('NGUsers')
                #we save the password only encripted
                ngvar.save(Username=self.signup.txt_user.text, Password=hashpass.hexdigest(), callback=self.res_signup)
                self.signup.dismiss()
            
                self.loading = Loading(source='loading.png')
                self.add_widget(self.loading)

            else:
                pass
                
    def res_signup(self, result):
        print "Signup response: ", result
        
        if result == 'Fail':
            return
        
        self.user = json.loads(result)

        #remove the loading screen and login form
        self.remove_widget(self.loading)
        self.remove_widget(self.login)
        

    def do_login(self):
        print "Logining into netget network: "
                
        self.loading = Loading(source='loading.png')
        self.add_widget(self.loading)
        
        #screenlog
        self.boxlogin = CenterLog()
        self.boxlogin.add_widget(Label(text='[color=EEEEEE]Iniciando sesion ...[/color]', markup=True, font_size=32))
        self.boxlogin.add_widget(Label(text='[color=FFFFFF]Cancelar inicio de sesion[/color]', markup=True, size_hint_y=None, height=200))
        self.add_widget(self.boxlogin)
        
        self.factory.Search(collection='NGUsers', 
                                    conditions={"equalTo":{"Username":self.login.txt_user.text}}, 
                                    callback=self.res_login)
        
    def res_login(self, results):
        print "Login result: ", results
        
        results = json.loads(results)
        
        if len(results) == 0:
            Msg(message="No user registered", title="Try again").open()
            return
            
        self.user = results[0]
        
        #encrypt password from the login form
        hashpass = md5.new()
        hashpass.update(self.login.txt_pass.text)
        
        #the current password and the saved password must be the same
        if hashpass.hexdigest() == self.user['Password']:
            self.remove_widget(self.loading)
            self.remove_widget(self.login)
            
            self.add_widget(NetgetSession(user=self.user) )
        else:
            Msg(message="Your password does not match, please try again", title="Try again").open()
            self.remove_widget(self.loading)
        
    def show_signup(self):
        print "Open signup"
        self.signup = NetgetSignUp()
        self.signup.open()
        
      
from kivy.app import App
            
class NetgetApp(App):
    def build(self):
        return NetgetBase()
        
    def on_stop(self):
        pass
    
        
    def on_pause(self):
        return True
        
    def on_resume(self):
        pass

if __name__ == '__main__':
    
    NetgetApp().run()

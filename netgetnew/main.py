
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from ngvars import NGFactory

from devslib.widget3D import Loading

import md5 #FIXME, USE THE LIBSODIUM HASH
import json

'''


'''
  
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
        self.factory = NGFactory(serverurl='http://104.236.181.245/ngcloud/')
    
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

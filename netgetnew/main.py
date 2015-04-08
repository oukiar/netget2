
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

from ngvars import NGFactory

from devslib.widget3D import Loading

import md5 #FIXME, USE THE LIBSODIUM HASH

'''


'''
  
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
        self.factory = NGFactory(serverurl='http://www.devsinc.com.mx/ngcloud/')
    
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
        print result
        
        if result == 'Fail':
            return
        
        self.user = json.loads(result)

        #remove the loading screen and login form
        self.remove_widget(self.loading)
        self.remove_widget(self.login)
        

    def do_login(self):
        print "Logining into netget network: "
        
        query = self.factory.Search('NGUsers')
        query.get(Username=self.login.txt_user.text, callback=self.res_login)
        
    def res_login(self, result):
        print result
        
        self.user = json.loads(result)
        
        #encrypt password from the login form
        hashpass = md5.new()
        hashpass.update(self.login.txt_pass.text)
        
        #the current password and the saved password must be the same
        if hashpass.hexdigest() == self.user['Password']:
            self.remove_widget(self.loading)
            self.remove_widget(self.login)
            
        
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

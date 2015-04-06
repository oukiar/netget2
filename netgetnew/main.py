
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

from ngvars import NGFactory

from devslib.widget3D import Loading
  
class NetgetLogin(AnchorLayout):
    pass
    
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
    
                ngvar = self.factory.Extends('NGUsers')
                ngvar.save(Username=self.signup.txt_user.text, Password=self.signup.txt_pass.text)
                self.signup.dismiss()
            
                seld.add_widget(Loading(source='loading.png'))

            else:
                pass

    def do_login(self):
        print "Logining into netget network"
        
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

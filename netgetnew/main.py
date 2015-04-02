
from kivy.uix.popup import Popup
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
  
class NetgetLogin(AnchorLayout):
    pass
    
class NetgetSignUp(Popup):
    pass
    
class NetgetBase(FloatLayout):
    login = ObjectProperty()
    
    def do_signup(self):
        print "Creating account"
    
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

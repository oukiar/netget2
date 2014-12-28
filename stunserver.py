from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from devslib.network import Network
from devslib.utils import Request

import json

import socket #only for the hostname-machinename

'''
::documentation
http://es.wikipedia.org/wiki/STUN
'''

class StunServer(FloatLayout):
    def __init__(self, **kwargs):
        super(StunServer, self).__init__(**kwargs)
            
        #network object
        self.net = Network()
                
        #create conection
        if self.net.create_connection(self.incoming):
            #try to discover netget devices on the local network
            self.net.host_discover()
        else:
            print "Error creating connection"
            self.net = None

        #logs


        #visual gui
        self.log = TextInput()
        self.add_widget(self.log)

        #informar al server principal el ip de este servidor stun ... 
        Request(action='http://www.orgboat.com/netget/ngaddstunserver.php', 
                data={
                'machinename':socket.gethostname()}, 
                callback=self.res_addstun)
                
        #enviar cada cierto tiempo nuestro update request ping
        Clock.schedule_interval(self.updatealive, 30)
        
    def updatealive(self, dt):
        
        Request(action='http://www.orgboat.com/netget/ngpingstunalive.php', 
                data={}, 
                callback=self.res_stunalive)
                
    def res_stunalive(self, response):
        print 'Update stun alive response: ', response
                
    def res_addstun(self, response):
        print 'Add stun server response: ', response

    def incoming(self, datajson, addr):
        print datajson

        data = json.loads(datajson)

        if data['msg'] == 'stun_request':
            self.log.text += 'Solving public IP for %s' % str(addr)
            self.net.send(addr, {'addr':addr})

    def __del__(self, **kwargs):
        self.net.network_shutdown()

if __name__ == '__main__':
    from kivy.base import runTouchApp

    runTouchApp(StunServer() )

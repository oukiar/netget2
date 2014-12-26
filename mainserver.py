from kivy.uix.floatlayout import FloatLayout

from devslib.network import Network

import json

class MainServer(FloatLayout):
    def __init__(self, **kwargs):
        super(MainServer, self).__init__(**kwargs)
            
        #global network object
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


        #

    def incoming(self, datajson, addr):
        print datajson

        data = json.loads(datajson)

        if data['msg'] == 'stun_request':
            self.net.send(addr, {'addr':addr})


if __name__ == '__main__':
    from kivy.base import runTouchApp

    runTouchApp(MainServer() )

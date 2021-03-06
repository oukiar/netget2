
'''
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
'''

from devslib.network import Network, Request, TimerInterval

import json

import socket #only for the hostname-machinename ... NOTE: Move this to network.py

'''
::documentation
http://es.wikipedia.org/wiki/STUN
'''

class StunServer:
    def __init__(self, **kwargs):
        #super(StunServer, self).__init__(**kwargs)
            
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
        self.log = 'Log initialized'

        #visual gui
        #self.log = TextInput()
        #self.add_widget(self.log)

        #informar al server principal el ip de este servidor stun ... 
        Request(action='http://www.orgboat.com/netget/ngaddstunserver.php', 
                data={
                'machinename':socket.gethostname()}, 
                callback=self.res_addstun)
                
        #enviar cada cierto tiempo nuestro update request ping
        TimerInterval(self.updatealive, 30)
        
        self.menu()
        
    def menu(self):
        while True:
            print '''
                    Selecciona una opcion:
                    
                    1. Ver log
                    2. Informacion de conexion
                    3. Solicitudes atendidas
                    4. Reiniciar conexion
                    5. Salir
                    '''
                    
            opc = raw_input()
            
            print "Ejecutando opcion: ", opc
            
            if opc == '1':
                print self.log
            elif opc == '5':
                self.net.shutdown_network()
                return
        
        
    def updatealive(self, dt=None):
        
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
            slog =  'Solving public IP for %s\n' % str(addr)
            
            self.log += slog
            
            #data to send
            tosend = json.dumps({'msg':'your_public_address', 'data':addr})

            self.net.send(addr, tosend)

    def __del__(self, **kwargs):
        self.net.network_shutdown()

if __name__ == '__main__':
    #from kivy.base import runTouchApp

    #runTouchApp(StunServer() )
    
    StunServer()


'''
Las netgevars son "Variables" que  se actualizan automaticamente a
nivel cloud, usando la tecnologia disponible de sincronizacion.

El entorno de sesion y accesso a los datos es realizado on-the-fly.

Neurons art & technology 2012-2015
'''


'''
Acerca de la sincronizacion inicial.

Se usara la solucion de php como backend inspirada en parse.
'''

from kivy.properties import StringProperty, NumericProperty
from kivy.uix.widget import Widget
import json

from devslib.utils import Request

class NGVar(Widget):
    varname = StringProperty()
    vartype = StringProperty('Universal')
    data = StringProperty() #in json format
    objectId = NumericProperty(-1)
    appId = StringProperty()
    appKey = StringProperty()
    
        
    def save(self, **kwargs):
        
        datadict = kwargs.copy()
        datadict.update({'objectId':self.objectId,
                                'appId':self.appId,
                                'appkey':self.appKey,
                                'varname':self.varname
                                })
        
        #enviar peticion de creacion ... php backend por ahora
        Request(action='http://www.devsinc.com.mx/ngcloud/extends.php', 
                data=datadict, 
                callback=self.res_save)
        
    def res_save(self, response):
        print response
    
    def get(self, fields):
        pass
        
    def query(self, **kwargs):
        pass
        
        
class NGFile(Widget):
    '''
    NGFile representa un archivo netget que actualiza su contenido
    automaticamente en cloud del app y sesion donde sea creado.
    '''
    pass
    
class NGFactory(Widget):
    
    serverurl = StringProperty()

    def Extends(self, name, **kwargs):
        return NGVar(varname=name, **kwargs)

    def Search(self, **kwargs):
        pass
        
    def Save(self, ngvar):
        ngvar.save()

    def Insert(self):
        pass
        
    def Update(self):
        pass
        
    def Delete(self):
        pass

if __name__ == '__main__':
    
    factory = NGFactory(serverurl='http://www.devsinc.com.mx/ngcloud/')
    ngvar = factory.Extends('Users')
    
    ngvar.save(Name="Nat synapses", Email="natsynapses@gmail.com")
    
    from kivy.base import runTouchApp
    
    runTouchApp(ngvar)
    

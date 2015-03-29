
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

from kivy.properties import StringProperty

class NGVar(Widget):
    name = StringProperty()
    data = StringProperty()
    
    def save(self, **kwargs):
        
    
class NGFactory(widget):
    
    serverurl = StringProperty()

    def Create(self, name, **kwargs):
        print kwargs
        return NGVar(name=name)

    def Search(self):
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
    
    creator = NGFactory(serverurl='http://www.devsinc.com.mx/ngcloud/')
    ngvar = creator.Create('Users')
    
    ngvar.save(Name="Oscar Alcantara", Email="oukiar@gmail.com"})
    
    
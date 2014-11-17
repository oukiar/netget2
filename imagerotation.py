
from kivy.animation import Animation

from kivy.core.window import Window

from kivy.properties import NumericProperty

from kivy.graphics import Color, Rectangle

from kivy.graphics.opengl import *
from kivy.graphics import *


class RotatingImage(Widget):
    
    rotate_z = NumericProperty(0)
    
    def __init__(self, **kwargs):
        
        super(RotatingImage, self).__init__(
                                            size_hint=(None,None),
                                            size=(32,32),
                                            **kwargs)
        
        with self.canvas.before:
            PushMatrix()    #save the current opengl state
            self.translate = Translate(-32, -32, 0)
            self._rotatez = Rotate(angle=self.rotate_z, axis=(0, 0, 1) )
        
        with self.canvas:
            Rectangle(source='donutloading.png', size=(64,64) )
        
        with self.canvas.after:
            PopMatrix() #restore the previous opengl state 
            
        self.animrot = Animation(rotate_z=180, duration=1)
        self.animrot.bind(on_complete=self.reanimate)
        
        self.reanimate()
        
    def reanimate(self, anim=None, w=None):
        self.rotate_z = 0
        self.animrot.start(self)

    def on_rotate_z(self, w, val):
        self._rotatez.angle = val

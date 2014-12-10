
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation


class Launcher(Image):
    def __init__(self, **kwargs):
        super(Launcher, self).__init__(source='docklauncher512.png',
                                        size_hint=(None,None),
                                        pos=(-50,-50),
                                        #size=(100,100),
                                        #pos_x=-1900,
                                        #pos_y=-1100,
                                        #pos_z=-1400, 
                                        #scale_x=.5, 
                                        #scale_y=.5, 
                                        **kwargs)
        
        print 'Launcher image size: ', self.size
            
        #for mouse over event
        Window.bind(mouse_pos=self.mouse_over)
    
        self.animin = Animation(size=(100,100), duration=1)
        self.animax = Animation(size=(300,300), duration=1)
        
        self.animin.bind(on_complete=self.on_minimized)
        self.animax.bind(on_complete=self.on_maximized)

        self.state = 'minimising'
    
        self.animin.start(self)

    def mouse_over(self, instance, pos):
        if self.collide_point(pos[0], pos[1]):
            if self.state == 'iddle_min':
                self.state = 'maximising'
                self.animax.start(self)
        else:
            if self.state == 'iddle_max':
                self.state = 'minimising'
                self.animin.start(self)

    def on_minimized(self, anim, w):
        self.state = 'iddle_min'

    def on_maximized(self, anim, w):
        self.state = 'iddle_max'


if __name__ == '__main__':
    from kivy.base import runTouchApp
    
    
    runTouchApp( Launcher() )


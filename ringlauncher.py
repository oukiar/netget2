
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation

from devslib.widget3D import Image3D, Widget3D
from devslib.utils import ImageButton

class Launcher(Image):
    def __init__(self, **kwargs):
        
        pos = kwargs.pop('pos', (-100,-100))
        
        super(Launcher, self).__init__(source='docklauncher512.png',
                                        size_hint=(None,None),
                                       allow_stretch=True,
                                        **kwargs)
        
        #icons sizes
        self.selected_scale = 1.5
        self.unselected_scale = .3
        
        print 'Launcher image size: ', self.size
            
        #for mouse over event
        Window.bind(mouse_pos=self.mouse_over)
    
    
        self.animin = Animation(width=100, height=100, duration=.3)
        self.animax = Animation(width=400, height=400, duration=.3)
        
        
        '''
        self.animin = Animation(scale_x=1, scale_y=1, duration=.3)
        self.animax = Animation(scale_x=2, scale_y=2, duration=.3)
        '''
            
        self.animin.bind(on_complete=self.on_minimized)
        self.animax.bind(on_complete=self.on_maximized)

        self.state = 'minimizing'
    
        self.animin.start(self)
    

    def mouse_over(self, instance, pos):
        #if self.collide_point(pos[0], pos[1]):
        if self.collide_point(pos[0], pos[1]):
            if self.state == 'iddle_min':
                self.state = 'maximising'
                self.animax.start(self)
        else:
            if self.state == 'iddle_max':
                self.state = 'minimising'
                self.animin.start(self)


    
    
    
    def on_size(self, w, val):
        
        radio = self.width*.7
        
        for i in self.children:
            #newsize = (val[0]*self.unselected_scale, val[1]*self.unselected_scale )
            #print 'Newsize: ', newsize
            i.size = (val[0]*self.unselected_scale, val[1]*self.unselected_scale)




    def on_minimized(self, anim, w):
        self.state = 'iddle_min'

    def on_maximized(self, anim, w):
        self.state = 'iddle_max'


if __name__ == '__main__':
    
    def on_iconpress(object):
        print 'Pressed icon'
    
    from kivy.base import runTouchApp
    
    launcher = Launcher()
    
    img = ImageButton(size_hint=(None,None),
                  size=(100,100),
                source='shotcam.png',
                allow_stretch=True,
                      on_press=on_iconpress
                  )
                  
    img.pos = (50,50)
    
    launcher.add_widget(img)
    '''
    img = Image(size_hint=(None,None),
                  size=(100,100),
                  source='clock.png'
                  )
        
    launcher.add_widget(img)
    '''
    runTouchApp( launcher )


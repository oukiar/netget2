

from kivy.uix.image import Image

from widget3D import Image3D

class Launcher(Image3D):
    def __init__(self, **kwargs):
        super(Launcher, self).__init__(source='bglauncher.png', 
                                        #pos_x=-400, 
                                        #pos_y=-250, 
                                        #pos_z=-500, 
                                        #scale_x=.5, 
                                        #scale_y=.5, 
                                        **kwargs)
        
        
        
        print 'Launcher image size: ', self.size

if __name__ == '__main__':
    from kivy.base import runTouchApp
    
    runTouchApp( Launcher() )

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.button import Button
from kivy.extras.highlight import KivyLexer
from kivy.properties import StringProperty
from kivy.uix.filechooser import FileChooserListView

import os

class Editor(BoxLayout):
    
    filename = StringProperty("")
    
    def __init__(self, **kwargs):
        self.codeinput = CodeInput()
        
        super(Editor, self).__init__(orientation='vertical', **kwargs)
        
        self.add_widget(self.codeinput)
        
        self.buttons = BoxLayout(size_hint_y=None, height=50)
        self.buttons.add_widget(Button(text='Save', on_press=self.on_save))
        self.buttons.add_widget(Button(text='Run', on_press=self.on_run))
        self.buttons.add_widget(Button(text='Open', on_press=self.on_open))
        self.buttons.add_widget(Button(text='Close'))
        
        self.add_widget(self.buttons)
        
    def on_filename(self, w, val):
        with open(val) as f:
            self.codeinput.text = f.read()
            
    def on_save(self, w):
        with open(val, 'w+') as f:
             f.write(self.codeinput.text)
             
    def on_run(self, w):
        os.system("python " + self.filename)
        
    def on_open(self, w):
        self.files = FileChooserListView(on_submit=self.fileselected)
        self.add_widget(self.files)
        
    def fileselected(self, w, selection, touch):
        print "Selected: ", selection

if __name__ == '__main__':
    from kivy.base import runTouchApp

    runTouchApp(Editor(filename='editor.py'))

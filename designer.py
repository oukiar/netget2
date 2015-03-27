from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.extras.highlight import KivyLexer
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.filechooser import FileChooserListView
from kivy.clock import Clock

import os

'''
Widgets permitidos

BoxLayout
Label
Button
Select
Tab
TabItem

- Planear interfaz
    - Seccion para elejir widget a insertar
    

'''

class TextCode(CodeInput):
    pass

class Designer(BoxLayout):
    
    filename = StringProperty()
    codefiles = ObjectProperty()

    def openfile(self):
        
        if self.codeinput == None or len(self.filename) == 0:
            return
        if not os.path.exists(self.filename):
            return
        
        with open(self.filename) as f:
            self.codeinput.text = f.read()
    
    def on_save(self):
        with open(self.filename, 'w+') as f:
             f.write(self.codeinput.text)
             
    def on_run(self):
        os.system("python " + self.filename)
    
    def on_close(self):
        os.system("python " + self.filename)
    
    def on_new(self):
        os.system("python " + self.filename)
    
    def on_open(self):
        self.files = FileChooserListView(on_submit=self.fileselected, path='.')
        self.add_widget(self.files)
        
    def fileselected(self, w, selection, touch):
        print "Selected: ", selection
        self.filename = selection[0]
        self.remove_widget(self.files)

if __name__ == '__main__':
    from kivy.app import App
    
    class DesignerApp(App):
        def build(self):
            designer = Designer()
            return designer

    DesignerApp().run()

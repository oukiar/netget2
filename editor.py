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

class Editor(BoxLayout):
    
    filename = StringProperty()
    codeinput = ObjectProperty()

    def openfile(self):
        print "Opening ", self.filename
        if self.codeinput == None or len(self.filename) == 0:
            return
        if not os.path.exists(self.filename):
            return
        
        with open(self.filename) as f:
            self.codeinput.text = f.read()

        print "opened"
    
    def on_save(self):
        with open(val, 'w+') as f:
             f.write(self.codeinput.text)
             
    def on_run(self):
        os.system("python " + self.filename)
        
    def on_open(self):
        self.files = FileChooserListView(on_submit=self.fileselected)
        self.add_widget(self.files)
        
    def fileselected(self, w, selection, touch):
        print "Selected: ", selection
        self.filename = selection[0]

if __name__ == '__main__':
    from kivy.app import App
    
    class EditorApp(App):
        def build(self):
            editor = Editor()
            editor.filename = "editor.py"
            return editor

    EditorApp().run()

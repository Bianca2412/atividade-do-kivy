from kivy.app import App 
from kivy.uix.button import Button
class Myapp(App):
    def build(self):
        return Button(text="Hello word! This is my frist program in kivy \n I'm a SESIANO Student, and I love my Teacher")
if __name__ == '__main__':
    Myapp().run()
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(
            text='Olá SENAI!', 
            halign='left', #alinha o texto à esquerda 
            valign='top', #alinha o texto no topo 
            size_hirt=(None,None),
            size=(150,50),
            text_sixe=(150,None)
        )
    
if __name__ == "__main__":
    MyApp().run()
from kivy.app import App
from kivy.uix.label import Label

class minhaapp(App):
    def build(self):
        return Label(text = 'Olá SENAI!', 
                    halign = 'left', #alinha o texto à esquerda 
                    valign = 'top' #alinha o texto no topo 
        )
    
if __name__ == "__main__":
    minhaapp().run()
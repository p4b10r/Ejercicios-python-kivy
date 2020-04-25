import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Dispo(BoxLayout):
    None

class Impres(GridLayout):
    None


class BoxygridApp(App):
    def build(self):
        return Dispo()
        return Impres()

if __name__ == '__main__':
    BoxygridApp().run()

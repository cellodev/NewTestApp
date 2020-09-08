#from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

#Config.set('kivy', 'log_name', '/storage/emulated/0/kivy_%d-%m-%y_%_.txt')
#Config.write()

class Home(Screen):
    teste = ObjectProperty(None)
    def captu(self):
        global canc
        if self.ids['btntest'].text == "Scanear":
            canc = Clock.schedule_interval(self.pap, 0.03)
        self.ids['btntest'].background_color = 1.0, 0.0, 0.0, 1.0
        self.ids['btntest'].text = "Scaneando..."

    def pap(self, dt):
        if len(self.teste) > 0:
            canc.cancel()
            self.ids['btntest'].background_color = 0, 1, 0, 1
            self.ids['btntest'].text = "Scanear"
            qrcode = str(self.teste[0].data)
            if qrcode == "Hello :)":
                self.parent.current = "secscreen"
                self.parent.transition.direction = 'left'

class Secscreen(Screen):
    pass


GUI = Builder.load_string('''
#:import ZBarCam zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol

GridLayout:
    cols: 1
    ScreenManager:
        id: screen_manager
        Home:
            name: "home"
            id: home
        Secscreen:
            name: "secscreen"
            id: secscreen

<Home>:
    teste: zbarcam.symbols
    GridLayout:
        cols: 1
        orientation: 'vertical'
        ZBarCam:
            id: zbarcam
            Widget:
                id: proxy
                XCamera:
                    id: xcamera
                    play: False
        Button:
            id: btntest
            on_press: root.captu()
            background_color: (0, 1, 0, 1)
            pos_hint: {'center_x': 0.5, 'center_y': 0}
            size_hint: 1, 0.35
            text: "Scanear"
            font_size: 60
<secscreen>:
    BoxLayout:
        Button:
            text: "Passou"

''')

class Home(Screen):
    teste = ObjectProperty(None)
    def captu(self):
        global canc
        if self.ids['btntest'].text == "Scanear":
            canc = Clock.schedule_interval(self.pap, 0.03)
        self.ids['btntest'].background_color = 1.0, 0.0, 0.0, 1.0
        self.ids['btntest'].text = "Scaneando..."

    def pap(self, dt):
        if len(self.teste) > 0:
            canc.cancel()
            self.ids['btntest'].background_color = 0, 1, 0, 1
            self.ids['btntest'].text = "Scanear"
            qrcode = str(self.teste[0].data)
            if qrcode == "Hello :)":
                self.parent.current = "sec"
                self.parent.transition.direction = 'left'


class secscreen(Screen):
    pass


class MainApp(App):
    def build(self):
        return GUI


if __name__ == '__main__':
    MainApp().run()


#Config.set('kivy', 'log_name', '/storage/emulated/0/kivy_%d-%m-%y_%_.txt')
#Config.write()

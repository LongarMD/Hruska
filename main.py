from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

from kivymd.app import MDApp

import style


class MainScreen(Screen):
    pass


class DrinksScreen(Screen):
    pass


class HruskaApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hruška"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"

        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '1024')
        Config.set('graphics', 'height', '600')

        super().__init__(**kwargs)

    def build(self):
        return Builder.load_string(style.root_kv)


if __name__ == "__main__":
    HruskaApp().run()

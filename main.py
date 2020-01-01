from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.config import Config

from kivymd.app import MDApp

import style
from ui import *
Builder.load_string(style.root_kv)


class HruskaApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hruška"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"

        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '1024')
        Config.set('graphics', 'height', '600')
        Config.write()

        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        main_screen, settings_screen = MainScreen(name='main'), SettingsScreen(name='settings')

        sm.add_widget(main_screen)
        sm.add_widget(settings_screen)

        return sm

    @staticmethod
    def get_size(x, y, orientation_x='h', orientation_y='v'):
        window_size = Window.size
        new_x = window_size[0] * x if orientation_x == 'h' else window_size[1] * x
        new_y = window_size[1] * y if orientation_y == 'v' else window_size[0] * y

        return new_x, new_y


if __name__ == "__main__":
    HruskaApp().run()

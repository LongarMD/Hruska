from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.config import Config

from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *

import style
Builder.load_string(style.root_kv)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.add_widget(DrinkPanel())

    def on_pre_enter(self, *args):
        print('yeet')


class SettingsScreen(Screen):
    pass


class DrinkPanel(Widget):
    def __init__(self, **kwargs):
        super(DrinkPanel, self).__init__(**kwargs)
        self.size = HruskaApp.get_size(0.45, 0.8)
        self.draw()

    def draw(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


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

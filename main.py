import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from kivymd.app import MDApp

from utils import get_size
from backend import DrinkManager

from frontend import style
from frontend import *
Builder.load_string(style.root_kv)

# TODO: Add a thumbnail


class HruskaApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hruška"
        self.icon = 'assets/logo/hruska.ico'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"

        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '1024')
        Config.set('graphics', 'height', '600')
        Config.write()

        recipes_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets/recipes')
        self.drink_manager = DrinkManager(recipes_dir)

        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        main_screen, settings_screen = MainScreen(self.drink_manager, name='main'), SettingsScreen(name='settings')

        self.drink_manager.load_drinks()
        self.drink_manager.display_drinks(main_screen)

        sm.add_widget(main_screen)
        sm.add_widget(settings_screen)

        return sm

    @staticmethod
    def get_size(x, y, orientation_x='h', orientation_y='v'):
        return get_size(x, y, orientation_x, orientation_y)


if __name__ == "__main__":
    HruskaApp().run()

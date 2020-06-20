import os

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.config import Config

from kivymd.app import MDApp
from utils import get_size
from backend import DrinkManager, MotorManager

from frontend import style
from frontend import *
Builder.load_string(style.root_kv)


Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.write()


class HruskaApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Hruška"
        self.icon = 'assets/logo/hruska.ico'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"

        recipes_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets/recipes')
        self.drink_manager = DrinkManager(recipes_dir)
        self.motor_manager = MotorManager()

        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        main_screen, settings_screen = MainScreen(self.drink_manager, name='main'), SettingsScreen(name='settings')
        loading_screen = LoadingScreen(name='loading')

        self.drink_manager.load_drinks()
        self.drink_manager.display_drinks(main_screen, self)

        sm.add_widget(main_screen)
        sm.add_widget(settings_screen)
        sm.add_widget(loading_screen)

        return sm

    def change_screen(self, name, transition=None):
        if transition is not None:
            self.root.transition = transition

        self.root.current = name

    @staticmethod
    def get_size(x, y, orientation_x='h', orientation_y='v'):
        return get_size(x, y, orientation_x, orientation_y)


if __name__ == "__main__":
    HruskaApp().run()

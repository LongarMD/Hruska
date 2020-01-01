from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen

from .panel_manager import DrinkPanel


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = AnchorLayout(anchor_x='center', anchor_y='center')

        layout.add_widget(DrinkPanel((1, 1, 1), (35/255, 35/255, 35/255), (139/255, 195/255, 74/255), anchor='right'))
        layout.add_widget(DrinkPanel((1, 1, 1), (35/255, 35/255, 35/255), (139/255, 195/255, 74/255), anchor='center'))
        layout.add_widget(DrinkPanel((1, 1, 1), (35/255, 35/255, 35/255), (139/255, 195/255, 74/255), anchor='left'))

        self.add_widget(layout)


class SettingsScreen(Screen):
    pass

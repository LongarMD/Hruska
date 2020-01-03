from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen

from .panels import DrinkPanel

lime = (139/255, 195/255, 74/255, 1)
dark = (35/255, 35/255, 35/255, 1)
red = (150/255, 0/255, 60/255, 1)
silver = (192/255, 192/255, 192/255, 1)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        layout = AnchorLayout(anchor_x='center', anchor_y='center')

        layout.add_widget(DrinkPanel(silver, dark, 'White Russian', 'assets/whiterussian.png', anchor='center'))
        layout.add_widget(DrinkPanel(lime, dark, 'Margarita', 'assets/margarita.png', anchor='right'))
        layout.add_widget(DrinkPanel(red, dark, 'Martini Negroni', 'assets/martini_negroni.png', anchor='left'))

        self.add_widget(layout)


class SettingsScreen(Screen):
    pass

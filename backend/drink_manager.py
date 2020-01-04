import json
import os

from kivy.uix.anchorlayout import AnchorLayout
from frontend.panels import DrinkPanel


class Drink:
    def __init__(self, json_str, path):
        self.drink_name = json_str['name']  # TODO: Add max char limit
        self.image_src = os.path.join(path, json_str['thumbnail_src'])
        self.primary_c = (json_str['primary_color']['r'],
                          json_str['primary_color']['g'],
                          json_str['primary_color']['b'],
                          json_str['primary_color']['a'])
        self.background_c = (json_str['background_color']['r'],
                             json_str['background_color']['g'],
                             json_str['background_color']['b'],
                             json_str['background_color']['a'])
        self.panel = None
    
    def set_panel(self, panel):
        self.panel = panel


class DrinkManager:
    def __init__(self, recipes_path):
        self.recipes_path = recipes_path
        self.drinks = []

    def load_drinks(self):
        drink_paths = [x[0] for x in os.walk(self.recipes_path)]

        for drink_path in drink_paths:
            try:
                json_path = os.path.join(drink_path, os.path.basename(drink_path) + '.json')
                with open(json_path, 'r') as json_file:
                    data = json.load(json_file)
                    self.drinks.append(Drink(data, drink_path))
            except FileNotFoundError:
                pass

        self.drinks.sort(key=lambda x: x.drink_name)

    def display_drinks(self, main_screen):

        layout = AnchorLayout(anchor_x='center', anchor_y='center')
        for i, drink in enumerate(self.drinks):
            panel = DrinkPanel(drink, i + 1)
            drink.set_panel(panel)

            layout.add_widget(panel)

        main_screen.add_widget(layout)

    def move_drinks(self, delta_pos):
        for drink in self.drinks:
            drink.panel.move_components(delta_pos)

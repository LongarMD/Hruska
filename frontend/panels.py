from kivy.core.window import Window

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.graphics import RoundedRectangle

from KivyMD.kivymd.uix.button import MDRoundFlatButton
from kivy.uix.image import Image

from utils import get_size

# TODO: Fix MDRoundFlatButton colours


class DrinkPanel(Widget):
    def __init__(self, drink, position, border_size=1.01, **kwargs):
        super(DrinkPanel, self).__init__(**kwargs)

        self.drink_name = drink.drink_name
        self.image_src = drink.image_src

        self.primary_c = drink.primary_c
        self.background_c = drink.background_c
        self.border_size = border_size

        self.position = position
        self.offset = (0, -0.1)
        self.size = get_size(0.45, 0.8)
        self.pos = self.get_position(self.size)

        self._components = []

        self.draw()

    def draw(self):
        radius = [(15., 15.) for x in range(4)]
        border_size = (self.size[0] * self.border_size, self.size[1] * self.border_size)
        border_position = self.get_position(border_size)
        shadow_pos = (border_position[0] - 6, border_position[1] - 6)

        with self.canvas.before:
            Color(.1, .1, .1, 0.6)
            self.add_components(('pos',
                                 RoundedRectangle(segments=20, radius=radius, pos=shadow_pos, size=border_size)))
            Color(*self.primary_c)
            self.add_components(('pos',
                                 RoundedRectangle(segments=20, radius=radius, pos=border_position, size=border_size)))
        with self.canvas:
            Color(*self.background_c)
            self.add_components(('pos', RoundedRectangle(segments=20, radius=radius, pos=self.pos, size=self.size)))

        layout = FloatLayout(size=Window.size)
        button = MDRoundFlatButton(text=self.drink_name, font_size=45, size_hint=(0.35, 0.15),
                                   pos_hint=self.get_button_pos(), theme_text_color="Custom",
                                   text_color=self.primary_c, md_bg_color=(1, 1, 1, 1))

        image = Image(source=self.image_src, size_hint=(0.35, .5), pos_hint=self.get_image_pos())

        layout.add_widget(button)
        layout.add_widget(image)

        self.add_components(('pos_hint', button), ('pos_hint', image))
        self.add_widget(layout)

    def get_position(self, size):
        offset = get_size(self.offset[0], self.offset[1])
        return self.position * Window.size[0] / 2 - size[0] / 2, (Window.size[1] - size[1] + offset[1]) / 2

    def get_button_pos(self):
        return {"center_x": self.position * 0.5, "center_y": .2}

    def get_image_pos(self):
        return {"center_x": self.position * 0.5, "center_y": .575}

    def add_components(self, *args):
        for obj in args:
            if obj not in self._components:
                self._components.append(obj)

    def move_components(self, delta_p):
        for obj in self._components:
            if obj[0] == 'pos':
                obj[1].pos = obj[1].pos[0] + delta_p[0], obj[1].pos[1] + delta_p[1]
            elif obj[0] == 'pos_hint':
                delta_pos_hint = delta_p[0] / Window.size[0], delta_p[1] / Window.size[1]
                obj[1].pos_hint = {'center_x': obj[1].pos_hint['center_x'] + delta_pos_hint[0],
                                   'center_y': obj[1].pos_hint['center_y'] + delta_pos_hint[1]}

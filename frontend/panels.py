from kivy.core.window import Window

from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.graphics import RoundedRectangle

from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.image import Image

from main import HruskaApp

# TODO: Fix MDRoundFlatButton colours


class DrinkPanel(Widget):
    def __init__(self, primary_c, background_c, drink_name, image_src,
                 secondary_c=None, border_size=1.01, anchor='center', **kwargs):
        super(DrinkPanel, self).__init__(**kwargs)

        if secondary_c is None:
            secondary_c = primary_c

        self.drink_name = drink_name  # TODO: Add max char limit
        self.image_src = image_src

        self.primary_c = primary_c
        self.background_c = background_c
        self.secondary_c = secondary_c
        self.border_size = border_size

        self.anchor = anchor
        self.offset = (0, -0.1)
        self.size = HruskaApp.get_size(0.45, 0.8)
        self.pos = self.get_position(self.size)

        self.draw()

    def draw(self):
        radius = [(15., 15.) for x in range(4)]
        border_size = (self.size[0] * self.border_size, self.size[1] * self.border_size)
        border_position = self.get_position(border_size)
        shadow_pos = (border_position[0] - 6, border_position[1] - 6)

        with self.canvas.before:
            Color(.1, .1, .1, 0.6)
            RoundedRectangle(segments=20, radius=radius, pos=shadow_pos, size=border_size)
            Color(*self.secondary_c)
            RoundedRectangle(segments=20, radius=radius, pos=border_position, size=border_size)
        with self.canvas:
            Color(*self.background_c)
            RoundedRectangle(segments=20, radius=radius, pos=self.pos, size=self.size)

        layout = FloatLayout(size=Window.size)
        button = MDRoundFlatButton(text=self.drink_name, font_size=45, size_hint=(0.35, 0.175),
                                   pos_hint=self.get_button_pos(), theme_text_color="Custom",
                                   text_color=self.primary_c, md_bg_color=(1, 0, 0, 1))

        image = Image(source=self.image_src, size_hint=(0.35, .5), pos_hint=self.get_image_pos())

        layout.add_widget(button)
        layout.add_widget(image)
        self.add_widget(layout)

    def get_position(self, size):
        offset = HruskaApp.get_size(self.offset[0], self.offset[1])
        if self.anchor == 'left':
            return -size[0] / 2, (Window.size[1] - size[1] + offset[1]) / 2
        elif self.anchor == 'center':
            return (Window.size[0] - size[0] + offset[0]) / 2, (Window.size[1] - size[1] + offset[1]) / 2
        elif self.anchor == 'right':
            return Window.size[0] - size[0] / 2, (Window.size[1] - size[1] + offset[1]) / 2

    def get_button_pos(self):
        if self.anchor == 'left':
            return {"center_x": 0, "center_y": .2}
        elif self.anchor == 'center':
            return {"center_x": .5, "center_y": .2}
        elif self.anchor == 'right':
            return {"center_x": 1, "center_y": .2}

    def get_image_pos(self):
        if self.anchor == 'left':
            return {"center_x": 0, "center_y": .575}
        elif self.anchor == 'center':
            return {"center_x": .5, "center_y": .575}
        elif self.anchor == 'right':
            return {"center_x": 1, "center_y": .575}

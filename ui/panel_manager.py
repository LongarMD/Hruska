from kivy.core.window import Window

from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.graphics import RoundedRectangle

from main import HruskaApp


class DrinkPanel(Widget):
    def __init__(self, primary_c, background_c, border_c, border_size=1.01, anchor='center', **kwargs):
        super(DrinkPanel, self).__init__(**kwargs)

        self.anchor = anchor
        self.offset = (0, -0.1)

        self.primary_c = primary_c
        self.background_c = background_c
        self.border_c = border_c
        self.border_size = border_size

        self.size = HruskaApp.get_size(0.45, 0.8)
        self.pos = self.get_position(self.size, anchor)

        self.draw()

    def draw(self):
        radius = [(15., 15.) for x in range(4)]
        border_size = (self.size[0] * self.border_size, self.size[1] * self.border_size)
        border_position = self.get_position(border_size, self.anchor)

        with self.canvas.before:
            Color(*self.border_c)
            RoundedRectangle(segments=20, radius=radius, pos=border_position, size=border_size)
        with self.canvas:
            Color(*self.background_c)
            RoundedRectangle(segments=20, radius=radius, pos=self.pos, size=self.size)

    def get_position(self, size, anchor):
        offset = HruskaApp.get_size(self.offset[0], self.offset[1])
        if anchor == 'left':
            return -size[0] / 2, (Window.size[1] - size[1] + offset[1]) / 2
        elif anchor == 'center':
            return (Window.size[0] - size[0] + offset[0]) / 2, (Window.size[1] - size[1] + offset[1]) / 2
        elif anchor == 'right':
            return Window.size[0] - size[0] / 2, (Window.size[1] - size[1] + offset[1]) / 2

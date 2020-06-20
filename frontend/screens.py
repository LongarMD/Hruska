from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.button import MDIconButton
from utils import get_size

class MainScreen(Screen):
    def __init__(self, drink_manager, app, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.drink_manager = drink_manager
        self.app = app
        self._mouse_pos = None

    def draw_settings(self):
        def goto_settings():
            self.app.root.transition = SlideTransition(direction='down')
            self.app.root.current = 'settings'
        layout = AnchorLayout(anchor_x='right', anchor_y='top')
        button = MDIconButton(icon='settings', text_color=[1, 1, 1, 1], size=get_size(.15, .15, 'v', 'v'),
                              user_font_size='40dp', on_release=lambda x: goto_settings())

        layout.add_widget(button)
        self.add_widget(layout)

    def on_touch_move(self, touch):
        if self._mouse_pos is None:
            self._mouse_pos = touch.pos

        delta_pos = touch.pos[0] - self._mouse_pos[0], 0
        self.drink_manager.move_drinks(delta_pos)
        self._mouse_pos = touch.pos

    def on_touch_up(self, touch):
        self._mouse_pos = None


class SettingsScreen(Screen):
    pass


class LoadingScreen(Screen):
    pass

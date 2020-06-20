from kivy.uix.screenmanager import Screen


class MainScreen(Screen):
    def __init__(self, drink_manager, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.drink_manager = drink_manager
        self._mouse_pos = None

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

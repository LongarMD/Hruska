from kivy.core.window import Window


def get_size(x, y, orientation_x='h', orientation_y='v'):
    window_size = Window.size
    new_x = window_size[0] * x if orientation_x == 'h' else window_size[1] * x
    new_y = window_size[1] * y if orientation_y == 'v' else window_size[0] * y

    return new_x, new_y

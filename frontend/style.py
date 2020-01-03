root_kv = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import MDRectangleFlatButton kivymd.uix.button.MDRectangleFlatButton

<MainScreen>:
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        MDIconButton:
            icon: 'settings'
            text_color: [1, 1, 1, 1]
            size: app.get_size(0.15, 0.15, 'v', 'v')
            user_font_size: '50dp'
            on_release:
                app.root.transition = SlideTransition(direction='down')
                app.root.current = 'settings'
    
<SettingsScreen>:
    BoxLayout:
        orientation: "vertical"
    
        FloatLayout:
            MDRaisedButton:
                pos_hint: {"center_x": .5, "center_y": .5}
                on_release:
                    app.root.transition = SlideTransition(direction='up')
                    root.manager.current = 'main'
                text: "Go back"
"""
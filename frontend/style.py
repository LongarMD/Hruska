root_kv = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

<MainScreen>:
    
    
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

<LoadingScreen>:
    FloatLayout:
        Image:
            source: 'assets/animations/loadingAnim.gif'
            pos_hint: {"center_x": .5, "center_y": .5}
            anim_delay: 0.05
"""
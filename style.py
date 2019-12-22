root_kv = """
ScreenManager:
    MainScreen:
    DrinksScreen:

<MainScreen>
    name: 'main_screen'
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'top'
        MDIconButton:
            icon: 'settings'
            text_color: [1, 1, 1, 1]
            
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'center'
        
    
        FloatLayout:
            MDRectangleFlatButton:
                text: "Rum & Coke"
                pos_hint: {"center_x": .5, "center_y": .5}
                font_size: 50
                size: 200, 120

    
<DrinksScreen>
    name: 'drinks_screen'
    BoxLayout:
        orientation: "vertical"
    
        FloatLayout:
    
            MDRaisedButton:
                text: "Go back"
                on_release: app.root.current = 'main_screen'
                pos_hint: {"center_x": .5, "center_y": .5}
"""
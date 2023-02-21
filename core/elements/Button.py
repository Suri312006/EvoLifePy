import core.util.Colors as color



class Button:
    def __init__(self, text="default", font='arial', text_size=10, text_color=color.black(),
                 width=75, height=15,
                 inactive_color=color.light_red(), active_color=color.red(),
                 action=None, action_target=None):

        self.text = text
        self.font = font
        self.text_size = text_size
        self.text_color = text_color
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action
        self.action_target = action_target

        self.clicked = False






from core.elements.Button import Button



class Player:
    def __init__(self, display, player_img, lmao):
        self.enemy = None
        self.player_img = player_img
        self.display = display
        self.char = lmao()

        self.move_button_font = "PKMN RBYGSC Regular"
        self.move_button_width = 300
        self.move_button_height = 75
        self.move_button_text_size = 30

    def set_enemy(self, enemy):
        self.enemy = enemy

    def button_move1(self):
        button = Button(display=self.display,text=self.char.get_move1()[0], font=self.move_button_font,
                        action=self.char.basic_attack, action_target=self.enemy.char,
                        width=self.move_button_width, height=self.move_button_height,
                        text_size=self.move_button_text_size)
        return button

    def button_move2(self):
        return Button(display=self.display,text=self.char.get_move2()[0], font=self.move_button_font,
                      action=self.char.move2, action_target=self.enemy.char,
                      width=self.move_button_width, height=self.move_button_height,
                      text_size=self.move_button_text_size)

    def button_move3(self):
        return Button(display=self.display,text=self.char.get_move3()[0], font=self.move_button_font,
                      action=self.char.move3, action_target=self.enemy.char,
                      width=self.move_button_width, height=self.move_button_height,
                      text_size=self.move_button_text_size)

    def button_move4(self):
        return Button(display=self.display,text=self.char.get_move4()[0], font=self.move_button_font,
                      action=self.char.move4, action_target=self.enemy.char,
                      width=self.move_button_width, height=self.move_button_height,
                      text_size=self.move_button_text_size)

    def get_char(self):
        return self.char

    def get_char_img(self):
        return self.char.get_img()

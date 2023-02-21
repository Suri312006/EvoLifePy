from core.elements.Button import Button


class Player:
    def __init__(self, player_img, lmao):
        self.enemy = None
        self.player_img = player_img
        self.char = lmao()

    def set_enemy(self, enemy):
        self.enemy = enemy

    def get_button1(self):
        button = Button(text=self.char.get_move1()[0], font="PKMN RBYGSC Regular", action=self.char.basic_attack,
                        action_target=self.enemy.char,
                        width=150, height=50, text_size=30)
        return button

    def get_button2(self):
        return Button(text=self.char.get_move2()[0], font="PKMN RBYGSC Regular", action=self.char.move2,
                      action_target=self.enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_button3(self):
        return Button(text=self.char.get_move3()[0], font="PKMN RBYGSC Regular", action=self.char.move3,
                      action_target=self.enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_button4(self):
        return Button(text=self.char.get_move4()[0], font="PKMN RBYGSC Regular", action=self.char.move4,
                      action_target=self.enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_char_hp_bar(self):
        return self.char.get_hp_bar()

    def get_char_img(self):
        return self.char.get_img()

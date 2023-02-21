from core.elements.Button import Button
from core.Characters.playablecharacters.Assassins.MutantRaven import MutantRaven


class Player:
    def __init__(self, player_img, lmao):
        self.player_img = player_img
        if lmao == MutantRaven:
            self.char = MutantRaven()


    def get_button1(self, enemy):
        button = Button(text=self.char.get_move1()[0], action=self.char.basic_attack, action_target=enemy.char,
                        width=150, height=50, text_size=30)
        return button

    def get_button2(self, enemy):
        return Button(text=self.char.get_move2()[0], action=self.char.move2, action_target=enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_button3(self, enemy):
        return Button(text=self.char.get_move3()[0], action=self.char.move3, action_target=enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_button4(self, enemy):
        return Button(text=self.char.get_move4()[0], action=self.char.move4, action_target=enemy.char, width=150,
                      height=50,
                      text_size=30)

    def get_char_hp_bar(self):
        return self.char.get_hp_bar()

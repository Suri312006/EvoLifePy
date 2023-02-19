
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

GREEN = (0, 255, 0)
LGREEN = (155, 255, 125)
YELLOW = (255, 255, 0)
LRED = (255, 155, 155)
RED = (255, 0, 0)
class Healthbar:

    def __init__(self, player, x_cord, y_cord, length=100, height=30, offset=10):
        self.max_hp = player.get_max_health()
        self.current_hp = player.health_report()[0]
        self.current_hp_percentage = player.health_report()[1]
        self.hp_color = GREEN
        self.hp_bar_length = (self.current_hp_percentage / 100) * length

    def get_color(self):

        if 60 < self.current_hp_percentage < 80:
            self.hp_color = LGREEN
        if 40 < self.current_hp_percentage < 60:
            self.hp_color = YELLOW
        if 20 < self.current_hp_percentage < 40:
            self.hp_color = LRED
        if 0 < self.current_hp_percentage < 20:
            self.hp_color = RED

        return self.hp_color

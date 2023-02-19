WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

GREEN = (0, 255, 0)
LGREEN = (155, 255, 125)
YELLOW = (255, 255, 0)
LRED = (255, 155, 155)
RED = (255, 0, 0)


class Healthbar:

    def __init__(self, player, length=100, height=30, offset=10):
        self._max_hp = player.get_max_health()
        self._current_hp = player.health_report()[0]
        self._current_hp_percentage = player.health_report()[1]
        self.hp_color = GREEN
        self.hp_bar_length = (self._current_hp_percentage / 100) * length
        self.hp_bar_height = height
        self._offset = offset

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

    def get_height(self):
        return self._height

    def get_offset(self):
        return self._offset

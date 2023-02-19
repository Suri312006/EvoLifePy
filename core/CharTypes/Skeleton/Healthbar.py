WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

GREEN = (0, 255, 0)
LGREEN = (155, 255, 125)
YELLOW = (255, 255, 0)
LRED = (255, 155, 155)
RED = (255, 0, 0)


class Healthbar:

    def __init__(self, player, length=100, height=30, offset=10):
        self._player = player

        self._max_hp = player.get_max_health()

        self._current_hp_percentage = None
        self._current_hp = None

        self._length = length
        self.hp_bar_height = height
        self.offset = offset

        self.hp_color = GREEN

    def update_status(self):
        self._current_hp = self._player.health_report()[0]
        self._current_hp_percentage = self._player.health_report()[1]

    def get_color(self):
        self.update_status()
        if 60 < self._current_hp_percentage < 80:
            self.hp_color = LGREEN
        if 40 < self._current_hp_percentage < 60:
            self.hp_color = YELLOW
        if 20 < self._current_hp_percentage < 40:
            self.hp_color = LRED
        if 0 < self._current_hp_percentage < 20:
            self.hp_color = RED

        return self.hp_color

    def get_current_length(self):
        self.update_status()
        return (self._current_hp_percentage / 100) * self._length

    def get_max_length(self):
        return self._length

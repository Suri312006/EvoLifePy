from core.util import Colors as color


class Healthbar:

    def __init__(self, player, length=100, height=30, offset=10):
        self._player = player

        self._max_hp = player.get_max_health()

        self._current_hp_percentage = None
        self._current_hp = None

        self._length = length
        self.hp_bar_height = height
        self.offset = offset

        self.hp_color = color.green()

    def update_status(self):
        self._current_hp = self._player.health_report()[0]
        self._current_hp_percentage = self._player.health_report()[1]

    def get_color(self):
        self.update_status()
        if 60 < self._current_hp_percentage < 80:
            self.hp_color = color.light_green()
        if 40 < self._current_hp_percentage < 60:
            self.hp_color = color.yellow()
        if 20 < self._current_hp_percentage < 40:
            self.hp_color = color.light_red()
        if 0 < self._current_hp_percentage < 20:
            self.hp_color = color.red()

        return self.hp_color

    def get_current_length(self):
        self.update_status()
        return (self._current_hp_percentage / 100) * self._length

    def get_max_length(self):
        return self._length

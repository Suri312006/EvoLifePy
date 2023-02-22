from core.util import Colors as color


class bar:
    def __init__(self, player,
                 max_value, current_value, current_value_percent, default_color,
                 length=300, height=30, offset=10):
        self._player = player

        self._max_value = max_value

        self._current_value = current_value
        self._current_value_percent = current_value_percent

        self._length = length
        self.bar_height = height
        self.offset = offset

        self.hp_color = default_color

    def update_status(self):
        pass

    def get_color(self):
        return self.hp_color

    def get_current_length(self):
        self.update_status()
        return (self._current_hp_percentage / 100) * self._length

    def get_max_length(self):
        return self._length


class Healthbar(bar):

    def __init__(self, player, length=300, height=30, offset=10):
        super().__init__(player, length=length, height=height, offset=offset,
                         max_value=player.get_max_health(), current_value=None, current_value_percent=None,
                         default_color=color.green())

    def update_status(self):
        self._current_value = self._player.health_report()[0]
        self._current_value_percent = self._player.health_report()[1]

    def get_color(self):
        self.update_status()
        if 60 < self._current_value_percent < 80:
            self.hp_color = color.light_green()
        if 40 < self._current_value_percent < 60:
            self.hp_color = color.yellow()
        if 20 < self._current_value_percent < 40:
            self.hp_color = color.light_red()
        if 0 < self._current_value_percent < 20:
            self.hp_color = color.red()

        return self.hp_color

    def get_current_length(self):
        self.update_status()
        return (self._current_value_percent / 100) * self._length


class Manabar(bar):

    def __init__(self, player, length=300, height=30, offset=10):
        self._player = player

        self._max_mana = player.get_mana()

        self._current_mana_percentage = None
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

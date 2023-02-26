from core.util import Colors as color


class bar:
    def __init__(self, char,
                 max_value, current_value, current_value_percent, default_color,
                 length=300, height=30, offset=10):
        self._char = char

        self._max_value = max_value

        self._current_value = current_value
        self._current_value_percent = current_value_percent

        self._length = length
        self.bar_height = height
        self.offset = offset

        self.color = default_color

    def update_status(self):
        pass

    def get_color(self):
        return self.color

    def get_current_length(self):
        self.update_status()
        return (self._current_value_percent / 100) * self._length

    def get_max_length(self):
        return self._length


class Healthbar(bar):

    def __init__(self, char, length=300, height=30, offset=10):
        super().__init__(char, length=length, height=height, offset=offset,
                         max_value=char.get_max_health(), current_value=None, current_value_percent=None,
                         default_color=color.green())

    def update_status(self):
        self._current_value = self._char.get_health()
        self._current_value_percent = (100 * round(self._char.get_health() / self._char.get_max_health(), 4))

    def get_color(self):
        self.update_status()
        if 60 < self._current_value_percent < 80:
            self.color = color.light_green()
        if 40 < self._current_value_percent < 60:
            self.color = color.yellow()
        if 20 < self._current_value_percent < 40:
            self.color = color.light_red()
        if 0 < self._current_value_percent < 20:
            self.color = color.red()

        return self.color

    def get_current_length(self):
        self.update_status()
        return (self._current_value_percent / 100) * self._length


class Manabar(bar):

    def __init__(self, char, length=300, height=30, offset=10):
        super().__init__(char, length=length, height=height, offset=offset,
                         max_value=char.get_max_health(), current_value=None, current_value_percent=None,
                         default_color=color.blue())

    def update_status(self):
        self._current_value = self._char.get_max_mana()
        self._current_value_percent = (100 * round(self._char.get_mana() / self._char.get_max_mana(), 4))


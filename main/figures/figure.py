class Figure:
    def __init__(self, name, color, position):
        self._name = name
        self._color = color
        self.position = position

    def move(self, cur_position, last_position, all_positions):
        self.cur_position = cur_position
        self.last_position = last_position
        self.all_position = all_positions
        return self.cur_position

    def possible_move(self, last_position, cur_position) -> bool:

        pass

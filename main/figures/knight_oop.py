class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.possible_move_knight_list = []
    def get_char(self):
        return 'N'

    def can_move(self, horizontal, vertical):
        start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

        a, b = self.horizontal, self.vertical
        for i in range(8):
            for j in range(8):
                if (8 - int(b) - 2 == i and j == start_row.index(a) - 1) or (
                        8 - int(b) - 2 == i and j == start_row.index(a) + 1) \
                        or (8 - int(b) + 2 == i and j == start_row.index(a) - 1) or (
                        8 - int(b) + 2 == i and j == start_row.index(a) + 1) \
                        or (8 - int(b) - 1 == i and j == start_row.index(a) - 2) or (
                        8 - int(b) - 1 == i and j == start_row.index(a) + 2) \
                        or (8 - int(b) + 1 == i and j == start_row.index(a) - 2) or (
                        8 - int(b) + 1 == i and j == start_row.index(a) + 2):
                    position = start_row[j] + str(8 - i)
                    self.possible_move_knight_list.append(position)
        self.h = horizontal
        self.v = vertical
        if self.h + str(self.v) in self.possible_move_knight_list:
            return True
        else:
            return False

    def move_to(self, horizontal, vertical):
        if self.can_move(horizontal=horizontal, vertical=vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        a, b = self.horizontal, self.vertical
        for i in range(8):
            for j in range(8):
                if j == start_row.index(a) and i == 8 - int(b):
                    print('N', end=' ')
                elif start_row[j] + str(8 - i) in self.possible_move_knight_list:
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(self.possible_move_knight_list)


if __name__ == '__main__':
    knight = Knight('c', 3, 'white')

    knight.draw_board()

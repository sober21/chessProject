class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.possible_move_knight_list = []

    def get_char(self):
        return 'N'

    def can_move(self, x, y):
        self.h, self.v = x,y
        a, b = self.horizontal, self.vertical
        for i in range(9):
            for j in 'abcdefgh':
                if (j == chr(ord(a) + 1) or j == chr(ord(a) - 1)) and (i == int(b) + 2 or i == int(b) - 2) or \
                        (j == chr(ord(a) + 2) or j == chr(ord(a) - 2)) and (i == int(b) + 1 or i == int(b) - 1):
                    if self.h + str(self.v) == j + str(i):
                        return True
        return False

    def move_to(self, x, y):
        if self.can_move(x=x, y=y):
            self.horizontal = x
            self.vertical = y

    def draw_board(self):
        a, b = self.horizontal, self.vertical
        for i in range(8, 0, -1):
            for j in 'abcdefgh':
                if j == a and i == int(b):
                    print('N', end=' ')

                elif (j == chr(ord(a) + 1) or j == chr(ord(a) - 1)) and (
                        i == int(b) + 2 or i == int(b) - 2) or \
                        (j == chr(ord(a) + 2) or j == chr(ord(a) - 2)) and (
                        i == int(b) + 1 or i == int(b) - 1):

                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()


if __name__ == '__main__':
    knight = Knight('c', 3, 'white')

    print(knight.color, knight.get_char())
    print(knight.horizontal, knight.vertical)
    knight.draw_board()
    knight.move_to('e', 4)
    knight.draw_board()

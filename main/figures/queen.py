def queen_move(position: str | list) -> None:
    a, b = position
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(8):
        for j in range(8):
            if j == row.index(a) and i == 8 - int(b):
                print('Q', end=' ')
            elif (j == row.index(a) and (8 - int(b) > i or 8 - int(b) < i)) or (
                    8 - int(b) == i and (j > row.index(a) or j < row.index(a))) or (
                    8 - int(b) - i == row.index(a) - j) or (
                    8 - int(b) == i + (8 - int(b) - i) and row.index(a) == j - (8 - int(b) - i)):
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()


if __name__ == '__main__':
    move = input('Сделайте ход:')
    queen_move(move)

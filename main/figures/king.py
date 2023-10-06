def king_move(position: str | list) -> None:
    a, b = position
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(8):
        for j in range(8):
            if j == row.index(a) and i == 8 - int(b):
                print('K', end=' ')
            elif (j == row.index(a) and (8 - int(b) == i+1 or 8 - int(b) == i-1)) or (
                    8 - int(b) == i and (j-1 == row.index(a) or j+1 == row.index(a))) or (
                    8 - int(b) == i - 1 and row.index(a) == j - 1) or (
                    8 - int(b) == i + 1 and row.index(a) == j + 1) or (
                    8 - int(b) == i - 1 and row.index(a) == j + 1) or (
                    8 - int(b) == i + 1 and row.index(a) == j - 1):
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()


if __name__ == '__main__':
    move = input('Сделайте ход:')
    king_move(move)
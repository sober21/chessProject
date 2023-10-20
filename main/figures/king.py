def possible_move_king(a_position='e1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_king_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (j == row.index(a) and (8 - int(b) == i + 1 or 8 - int(b) == i - 1)) or (
                    8 - int(b) == i and (j - 1 == row.index(a) or j + 1 == row.index(a))) or (
                         8 - int(b) == i - 1 and row.index(a) == j - 1) or (
                         8 - int(b) == i + 1 and row.index(a) == j + 1) or (
                         8 - int(b) == i - 1 and row.index(a) == j + 1) or (
                         8 - int(b) == i + 1 and row.index(a) == j - 1):
                position = row[j] + str(8 - i)
                possible_move_king_list.append(position)
    return possible_move_king_list


def king_move() -> None:
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['e1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_king(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
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
        print(end='\n \n \n')


if __name__ == '__main__':

    king_move()
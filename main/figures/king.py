def possible_move_king(a_position='e1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_king_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (j == start_row.index(a) and (8 - int(b) == i + 1 or 8 - int(b) == i - 1)) or (
                    8 - int(b) == i and (j - 1 == start_row.index(a) or j + 1 == start_row.index(a))) or (
                         8 - int(b) == i - 1 and start_row.index(a) == j - 1) or (
                         8 - int(b) == i + 1 and start_row.index(a) == j + 1) or (
                         8 - int(b) == i - 1 and start_row.index(a) == j + 1) or (
                         8 - int(b) == i + 1 and start_row.index(a) == j - 1):
                position = start_row[j] + str(8 - i)
                possible_move_king_list.append(position)
    return possible_move_king_list


def king_move() -> None:
    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['e1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_king(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == start_row.index(a) and i == 8 - int(b):
                    print('K', end=' ')
                elif start_row[j] + str(8-i) in possible_move_king(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':

    king_move()
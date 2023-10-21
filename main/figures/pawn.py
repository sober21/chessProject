def possible_move_pawn(a_position='e2') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_pawn_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if int(b) == 2 and (
                    (i == 8 - int(b) - 1 and j == start_row.index(a)) or (i == 8 - int(b) - 2 and j == start_row.index(a))):
                position = start_row[j] + str(8 - i)
                possible_move_pawn_list.append(position)
            elif i == 8 - int(b) - 1 and j == start_row.index(a):
                position = start_row[j] + str(8 - i)
                possible_move_pawn_list.append(position)
    return possible_move_pawn_list


def pawn_move() -> None:
    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['e2']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_pawn(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == start_row.index(a) and i == 8 - int(b):
                    print('p', end=' ')
                elif start_row[j] + str(8 - i) in possible_move_pawn(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    pawn_move()

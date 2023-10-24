def possible_move_pawn(a_position='e2') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''
    possible_move_pawn_list = []
    a, b = a_position
    for i in range(9):
        for j in 'abcdefgh':
            if int(b) == 2 and ((i == int(b) + 1 or i == int(b) + 2) and j == a):
                position = j + str(i)
                possible_move_pawn_list.append(position)
            elif i == int(b) + 1 and j == a:
                position = j + str(i)
                possible_move_pawn_list.append(position)
    return possible_move_pawn_list


def pawn_move() -> None:
    list_move = ['e2']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_pawn(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8, 0, -1):
            for j in 'abcdefgh':
                if j == a and i == int(b):
                    print('♙', end=' ')
                elif j + str(i) in possible_move_pawn(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    pawn_move()

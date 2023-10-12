def possible_move(a_position='a1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_rock_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (j == row.index(a) and (8 - int(b) > i or 8 - int(b) < i)) or (
                    8 - int(b) == i and (j > row.index(a) or j < row.index(a))):
                position = row[j] + str(8 - i)
                possible_move_rock_list.append(position)
    return possible_move_rock_list




# def valid_move(move='00') -> bool:
#     '''проверяет правильность введённого хода'''
#     before_move = 'a1'
#     if move in possible_move(before_move):
#         return True
#     else:
#         return False


def rock_move() -> None:
    '''печатает текущую позицию ладьи и возможные ходы'''
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['a1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == row.index(a) and i == 8 - int(b):
                    print('R', end=' ')
                elif (j == row.index(a) and (8 - int(b) > i or 8 - int(b) < i)) or (
                        8 - int(b) == i and (j > row.index(a) or j < row.index(a))):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    rock_move()

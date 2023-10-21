

def possible_move_rock(a_position='a1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_rock_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (j == start_row.index(a) and (8 - int(b) > i or 8 - int(b) < i)) or (
                    8 - int(b) == i and (j > start_row.index(a) or j < start_row.index(a))):
                position = start_row[j] + str(8 - i)
                possible_move_rock_list.append(position)
    return possible_move_rock_list


def rock_move() -> None:
    '''печатает текущую позицию ладьи и возможные ходы'''
    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['a1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_rock(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == start_row.index(a) and i == 8 - int(b):
                    print('R', end=' ')
                elif start_row[j] + str(8-i) in possible_move_rock(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    rock_move()

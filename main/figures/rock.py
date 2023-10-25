def possible_move_rock(a_position='a1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    possible_move_rock_list = []
    a, b = a_position
    for i in range(1, 9):
        for j in 'abcdefgh':
            if j == a or i == int(b):
                position = j + str(i)
                possible_move_rock_list.append(position)
    return possible_move_rock_list


def cur_move1(x='a1'):
    list_move = ['a1']
    cur_move = x
    while cur_move not in possible_move_rock(list_move[-1]):
        cur_move = input('Сделайте ход ладьёй:')
    list_move.append(cur_move)
    return cur_move


def rock_move() -> None:
    '''печатает текущую позицию ладьи и возможные ходы'''
    a, b = cur_move1()
    list_move = possible_move_rock(f'{a}{str(b)}')
    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == a and i == int(b):
                print('♖', end=' ')
            elif j + str(i) in list_move:
                print('*', end=' ')
            else:
                print('.', end=' ')
        print()
    print(end='\n \n \n')


if __name__ == '__main__':
    rock_move()

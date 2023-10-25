def possible_move_bishop(a_position='c1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    possible_move_bishop_list = []
    a, b = a_position
    for i in range(1,9):
        for j in 'abcdefgh':
            if abs(int(b) - i) == abs(ord(a) - ord(j)):
                position = j + str(i)
                possible_move_bishop_list.append(position)
    return possible_move_bishop_list


def cur_move1(x='c1'):
    list_move = ['c1']
    cur_move = x
    while cur_move not in possible_move_bishop(list_move[-1]):
        cur_move = input('Сделайте ход слоном:')
    list_move.append(cur_move)
    return cur_move


def bishop_move() -> None:
    a, b = cur_move1()
    list_move = possible_move_bishop(f'{a}{str(b)}')

    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == a and i == int(b):
                print('♗', end=' ')
            elif j + str(i) in list_move:
                print('*', end=' ')

            else:
                print('.', end=' ')
        print()
    print(end='\n \n \n')


if __name__ == '__main__':
    bishop_move()

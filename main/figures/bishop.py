def possible_move_bishop(a_position='c1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    possible_move_bishop_list = []
    a, b = a_position
    for i in range(9):
        for j in 'abcdefgh':
            if abs(int(b) - i) == abs(ord(a) - ord(j)):
                position = j + str(i)
                possible_move_bishop_list.append(position)
    return possible_move_bishop_list


def bishop_move() -> None:
    list_move = ['c1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_bishop(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8, 0, -1):
            for j in 'abcdefgh':
                if j == a and i == int(b):
                    print('♗', end=' ')
                elif j + str(i) in possible_move_bishop(cur_move):
                    print('*', end=' ')

                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    bishop_move()

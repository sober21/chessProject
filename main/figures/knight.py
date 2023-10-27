def possible_move_knight(cur_position, last_position) -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    possible_move_knight_list = []
    a, b = cur_position
    for i in range(9):
        for j in 'abcdefgh':
            if (j == chr(ord(a) + 1) or j == chr(ord(a) - 1)) and (i == int(b) + 2 or i == int(b) - 2) or \
                    (j == chr(ord(a) + 2) or j == chr(ord(a) - 2)) and (i == int(b) + 1 or i == int(b) - 1):
                position = j + str(i)
                if position == last_position:
                    return True
                possible_move_knight_list.append(position)

    return False


def knight_move() -> None:
    list_move = ['g1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_knight(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8, 0, -1):
            for j in 'abcdefgh':
                if j == a and i == int(b):
                    print('♘', end=' ')
                elif j + str(i) in possible_move_knight(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    knight_move()

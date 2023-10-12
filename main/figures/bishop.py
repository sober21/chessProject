def possible_move(a_position='c1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_bishop_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (8 - int(b) - i == row.index(a) - j) or (8 - int(b) == i + (8 - int(b) - i)
                and row.index(a) == j - (8 - int(b) - i)):
                position = row[j] + str(8 - i)
                possible_move_bishop_list.append(position)
    return possible_move_bishop_list

def bishop_move()->None:
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['c1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == row.index(a) and i == 8 - int(b):
                    print('B', end=' ')
                elif (
                        8 - int(b) - i == row.index(a) - j) or (
                        8 - int(b) == i + (8 - int(b) - i) and row.index(a) == j - (8 - int(b) - i)):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')


if __name__ == '__main__':
    bishop_move()

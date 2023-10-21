
def possible_move_knight(a_position='g1') -> list:
    '''возвращает список возможных ходов для конкретной позиции'''

    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_knight_list = []
    a, b = a_position
    for i in range(8):
        for j in range(8):
            if (8 - int(b) - 2 == i and j == start_row.index(a) - 1) or (8 - int(b) - 2 == i and j == start_row.index(a) + 1) \
                 or (8 - int(b) + 2 == i and j == start_row.index(a) - 1) or (8 - int(b) + 2 == i and j == start_row.index(a) + 1) \
                 or (8 - int(b) - 1 == i and j == start_row.index(a) - 2) or (8 - int(b) - 1 == i and j == start_row.index(a) + 2) \
                 or (8 - int(b) + 1 == i and j == start_row.index(a) - 2) or (8 - int(b) + 1 == i and j == start_row.index(a) + 2):
                position = start_row[j] + str(8 - i)
                possible_move_knight_list.append(position)
    return possible_move_knight_list

def knight_move() -> None:
    start_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    list_move = ['g1']
    while True:
        cur_move = input('Сделайте ход:')
        while cur_move not in possible_move_knight(list_move[-1]):
            cur_move = input('Сделайте ход:')
        list_move.append(cur_move)
        a, b = cur_move
        for i in range(8):
            for j in range(8):
                if j == start_row.index(a) and i == 8 - int(b):
                    print('♘', end=' ')
                elif start_row[j] + str(8 - i) in possible_move_knight(cur_move):
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(end='\n \n \n')

if __name__ == '__main__':
    knight_move()
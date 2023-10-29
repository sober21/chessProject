def possible_move_rock(cur_position, last_position, all_positions) -> bool:
    '''возвращает список возможных ходов для конкретной позиции'''

    possible_move_rock_list = []
    a, b = last_position
    if last_position[0] < cur_position[0] or last_position[1] < cur_position[1]:
        for i in range(1, 9):
            for j in 'abcdefgh':
                if (j == a or i == int(b)) and (j + str(i) != last_position):
                    position = j + str(i)
                    if position == cur_position and position not in all_positions.values():
                        return True
                    elif (position in all_positions.values() and position[0] == cur_position[0]) or \
                            (position in all_positions.values() and position[1] == cur_position[1]):
                        return False

    elif last_position[1] > cur_position[1]:
        for i in range(8, 0, -1):
            for j in 'abcdefgh':
                if (j == a or i == int(b)) and (j + str(i) != last_position):
                    position = j + str(i)
                    if (position in all_positions.values() and position[0] == cur_position[0]) or \
                            (position in all_positions.values() and position[1] == cur_position[1]):
                        return False
                    elif position == cur_position and position not in all_positions.values():
                        return True
    elif last_position[0] > cur_position[0]:
        for i in range(1, 9):
            for j in 'abcdefgh':
                if (j == a or i == int(b)) and (j + str(i) != last_position):
                    position = j + str(i)
                    if (position in all_positions.values() and position[0] == cur_position[0]) or \
                            (position in all_positions.values() and position[1] == cur_position[1]):
                        return False
                    elif position == cur_position and position not in all_positions.values():
                        return True

    return False


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

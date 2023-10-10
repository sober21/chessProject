def possible_move(start_position='a1') -> list:
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    possible_move_rock_list = []
    a, b = start_position
    for i in range(8):
        for j in range(8):
            if (j == row.index(a) and (8 - int(b) > i or 8 - int(b) < i)) or (
                    8 - int(b) == i and (j > row.index(a) or j < row.index(a))):
                position = row[j] + str(8 - i)
                possible_move_rock_list.append(position)
    return possible_move_rock_list


def valid_move(move='00') -> str:
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    while move[0] not in row or move[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
        move = input('Сделайте ход:').lower().strip()
        if move == 'стоп':
            return 'Пока!'
        elif move not in possible_move():
            print('Невозможный ход для ладьи.')
        elif len(move) == 0:
            print('Надо написать ход в шахматной аннотации')
            move = 'q0'
        elif len(move) != 2:
            print('Должно быть 2 символа без пробела: ряд и вертикаль.')

        elif not move.isalnum():
            print('Вводите только букву и цифру, как на шахматной доске.')

        else:
            print('Такой клетки нет на шахматной доске.')
    return move


def rock_move() -> None:
    row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    a, b = valid_move()
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

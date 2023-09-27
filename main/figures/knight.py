def knight_move(position: list) -> list:
    '''на вход позиция коня в шахматной аннотации, на выход: шахматная доска с конём в виде буквы "N",
    и возможные ходы коня в виде звёздочки("*")'''
    chess_board = [['.'] * 8 for _ in range(8)]
    letter = 'abcdefgh'
    for i in range(8):
        for j in range(len(letter)):
            if str(i + 1) == position[1] and 'abcdefgh'[j] == position[0]:
                chess_board[i][j] = 'N'  # добавил местонахождение коня на доску
                row, cols = i, j
    if row + 2 <= 7 and cols + 1 <= 7:  # проверки, чтобы возможный ход был в пределах доски
        chess_board[row + 2][cols + 1] = '*'
        print(letter[cols + 1], row + 3, sep='')
    if row + 2 <= 7 and cols - 1 >= 0:
        chess_board[row + 2][cols - 1] = '*'
        print(letter[cols - 1], row + 3, sep='')
    if row + 1 <= 7 and cols + 2 <= 7:
        chess_board[row + 1][cols + 2] = '*'
        print(letter[cols + 2], row + 2, sep='')
    if row + 1 <= 7 and cols - 2 >= 0:
        chess_board[row + 1][cols - 2] = '*'
        print(letter[cols - 2], row + 2, sep='')
    if row - 1 >= 0 and cols - 2 >= 0:
        chess_board[row - 1][cols - 2] = '*'
        print(letter[cols - 2], row, sep='')
    if row - 1 >= 0 and cols + 2 <= 7:
        chess_board[row - 1][cols + 2] = '*'
        print(letter[cols + 2], row, sep='')
    if row - 2 >= 0 and cols - 1 >= 0:
        chess_board[row - 2][cols - 1] = '*'
        print(letter[cols - 1], row - 1, sep='')
    if row - 2 >= 0 and cols + 1 <= 7:
        chess_board[row - 2][cols + 1] = '*'
        print(letter[cols + 1], row - 1, sep='')

    for i in range(4):  # переворот доски. Первая строка меняется с последней, вторая с предпоследней и т.д.
        for j in range(8):
            chess_board[i][j], chess_board[8 - 1 - i][j] = chess_board[8 - 1 - i][j], chess_board[i][j]

    for row in chess_board:
        print(*row)


if __name__ == '__main__':
    position = list(input())
    knight_move(position)
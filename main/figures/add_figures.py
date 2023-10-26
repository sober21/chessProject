import rock, bishop, king


def choise_figure() -> str:
    figure = input('Выберите фигуру:')
    return figure


def move() -> str:
    move1 = input('Сделайте ход:')
    return move1


def print_board(r1='a1', r2='h1', n1='b1', n2='g1', b1='c1', b2='f1', q='d1', k='e1'):

    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == r1[0] and i == int(r1[1]):
                print('♖', end='  ')
            elif j == r2[0] and i == int(r2[1]):
                print('♖', end='  ')
            elif j == n2[0] and i == int(n2[1]):
                print('♘', end='  ')
            elif j == n1[0] and i == int(n1[1]):
                print('♘', end='  ')
            elif j == b2[0] and i == int(b2[1]):
                print('♗', end='  ')
            elif j == b1[0] and i == int(b1[1]):
                print('♗ ', end='  ')
            elif j == q[0] and i == int(q[1]):
                print('♕', end='  ')
            elif j == k[0] and i == int(k[1]):
                print('♔ ', end='  ')
            # elif j + str(i) in list_move:
            #     print('*', end=' ')
            else:
                print('. ', end='  ')
        print()
    print(end='\n \n \n')




def add_figures_on_chess_board():
    print_board()
    f = choise_figure()
    m = move()

    print_board()




if __name__ == '__main__':
    print_board(r2='h3')

import rock, bishop, king


def choise_figure() -> str:
    figure = input('Выберите фигуру')
    return figure


def move() -> str:
    move1 = input('Сделайте ход:')
    return move1


def print_board():
    r = rock.cur_move1()
    b = bishop.cur_move1()
    k = king.cur_move1()
    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == r[0] and i == int(r[1]):
                print('♖', end=' ')
            elif j == b[0] and i == int(b[1]):
                print('♗', end=' ')
            elif j == k[0] and i == int(k[1]):
                print('♔', end=' ')
            # elif j + str(i) in list_move:
            #     print('*', end=' ')
            else:
                print('.', end=' ')
        print()
    print(end='\n \n \n')

    pass


def add_figures_on_chess_board():
    # position_figures = [rock.cur_move1(), bishop.cur_move1()]
    figure = ['q', 'r', 'p', 'k', 'n', 'b']
    fig = choise_figure()
    mo = move()
    r = rock.cur_move1()
    b = bishop.cur_move1()
    for i in figure:
        if fig == i:
            x1 = i.cur_move(mo)

    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == r[0] and i == int(r[1]):
                print('♖', end=' ')
            elif j == b[0] and i == int(b[1]):
                print('♗', end=' ')
            # elif j + str(i) in list_move:
            #     print('*', end=' ')
            else:
                print('.', end=' ')
        print()
    print(end='\n \n \n')


if __name__ == '__main__':
    print_board()

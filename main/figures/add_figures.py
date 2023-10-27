import rock, bishop, king


def choise_figure() -> str:
    figure = input('Выберите фигуру:')
    return figure


def move() -> str:
    move1 = input('Сделайте ход:')
    return move1

def possible_move(figure: str, position:str) -> bool:
    if figure == 'R1':
        if rock.possible_move_rock(position):
            return True
    return False




def print_board(**kwargs):
    d = kwargs
    for i in range(8, 0, -1):
        for j in 'abcdefgh':
            if j == d['R1'][0] and i == int(d['R1'][1]):
                print('♖', end='  ')
            elif j == d['R2'][0] and i == int(d['R2'][1]):
                print('♖', end='  ')
            elif j == d['N1'][0] and i == int(d['N1'][1]):
                print('♘', end='  ')
            elif j == d['N2'][0] and i == int(d['N2'][1]):
                print('♘', end='  ')
            elif j == d['B1'][0] and i == int(d['B1'][1]):
                print('♗', end='  ')
            elif j == d['B2'][0] and i == int(d['B2'][1]):
                print('♗ ', end='  ')
            elif j == d['Q'][0] and i == int(d['Q'][1]):
                print('♕', end='  ')
            elif j == d['K'][0] and i == int(d['K'][1]):
                print('♔ ', end='  ')
            # elif j + str(i) in list_move:
            #     print('*', end=' ')
            else:
                print('. ', end='  ')
        print()
    print(end='\n \n \n')




def add_figures_on_chess_board():
    d = {
        'R1': 'a1',
        'R2': 'h1',
        'N1': 'b1',
        'N2': 'g1',
        'B1': 'c1',
        'B2': 'f1',
        'Q': 'd1',
        'K': 'e1'
    }
    print_board(**d)
    f = ''
    while f != 'Стоп':
        f = choise_figure()
        m = move()
        if possible_move(f, m):
            d[f]=m
            print_board(**d)




if __name__ == '__main__':
    add_figures_on_chess_board()

class Board:
    def __init__(self):
        pass

    def print_board(self, **kwargs):
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
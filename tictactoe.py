import IPython.display
print('\t\tWELCOME TO TIC-TAC-TOE')

# def chose_symbol():
#     symbol_p1=1
#     while symbol_p1 not in (mark,'O'):
#         symbol_p1=input('Player One: select a symbol (X or O) ')

#     if symbol_p1==mark:
#         symbol_p2='O'
#     else:
#         symbol_p2=mark
#     return symbol_p1,symbol_p2

# symbol_p1,symbol_p2=chose_symbol()

# def box(gamelist):     #useless ho gya bhai
#     print('\t\t  | \t | \t ')
#     print('\t\t  | \t | \t ')
#     print('\t   --------------------')
#     print('\t\t  | \t | \t ')
#     print('\t\t  | \t | \t ')
#     print('\t   ---------------------')
#     print('\t\t  | \t | \t')
#     print('\t\t  | \t | \t ')
# image=box()
# print(image)

def board(row):
    print(row[7]+'\t|'+row[8]+'\t|'+row[9])
    print('--------------------------')
    print(row[4]+'\t|'+row[5]+'\t|'+row[6])
    print('----------------------------')
    print(row[1]+'\t|'+row[2]+'\t|'+row[3])


    
def replace():
    row=['',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    board(row)

    pos_x = []
    pos_o = []
    num=0
    while num < 9:
        pos = int(input('Which position (0 - 9) :'))
        if pos not in range(0,10):
            print('Please enter correct position : ')
            continue
        if pos not in pos_x and pos not in pos_o:
            if num % 2 == 0:
                symbol = 'X'
                pos_x.append(pos)
                num+=1
            else:
                symbol = 'O'
                pos_o.append(pos)
                num+=1
        else:
            print("Enter correct position : ")
        if pos == 1:
            row[1] = symbol
        elif pos == 2:
            row[2] = symbol
        elif pos == 3:
            row[3] = symbol
        elif pos == 4:
            row[4] = symbol
        elif pos == 5:
            row[5] = symbol
        elif pos == 6:
            row[6] = symbol
        elif pos == 7:
            row[7] = symbol
        elif pos == 8:
            row[8] = symbol
        elif pos == 9:
            row[9] = symbol
        board(row)
        if wincheck(row,symbol):
            print('{} is the winner'.format(symbol))
            break

        
        # print('\n'*100)
    
        
     # diagonal
    # return(num)

def wincheck(row,mark):
    
    return ((row[7] == mark and row[8] == mark and row[9] == mark) or # across the top
    (row[4] == mark and row[5] == mark and row[6] == mark) or # across the middle
    (row[1] == mark and row[2] == mark and row[3] == mark) or # across the bottom
    (row[7] == mark and row[4] == mark and row[1] == mark) or # down the middle
    (row[8] == mark and row[5] == mark and row[2] == mark) or # down the middle
    (row[9] == mark and row[6] == mark and row[3] == mark) or # down the right side
    (row[7] == mark and row[5] == mark and row[3] == mark) or # diagonal
    (row[9] == mark and row[5] == mark and row[1] == mark))
    
replace()
# print(r)
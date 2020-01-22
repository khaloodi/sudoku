board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

'''
algorithm steps:
1. pick an empty space
2. try all numbers
3. find one that works
'''

# print(len(game_board))

def print_board(gb):
    '''
    prints the game board
    '''
    for i in range(len(gb)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')

        for j in range(len(gb[0])): # for len of row 
            if j % 3 == 0 and j != 0:
                print (' | ', end='')

            if j == 8:
                print(gb[i][j])
            else:
                print(str(gb[i][j]) + ' ', end='')

def find_empty(gb):
    for i in range(len(gb)):
        for j in range(len(gb[0])):
            if gb[i][j] == 0:
                return (i, j) # row, col

print(print_board(board))
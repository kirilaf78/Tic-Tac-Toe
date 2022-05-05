enter = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def grid_print():
    print('-' * 9)
    print(f'| {enter[0]} {enter[1]} {enter[2]} |')
    print(f'| {enter[3]} {enter[4]} {enter[5]} |')
    print(f'| {enter[6]} {enter[7]} {enter[8]} |')
    print('-' * 9)


grid_print()

moves_count = 2
flag = 0
i = 0
a = 0
c = 0

while flag == 0:
    coordinates = input('Enter the coordinates: ')

    coordinates_list = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    for x in coordinates:
        if x in alphabet:
            print('You should enter numbers!')
            break
        if coordinates not in coordinates_list:
            print('Coordinates should be from 1 to 3!')
            break

    for x in coordinates_list:
        if coordinates in coordinates_list:
            if i < 9:
                if coordinates_list[i] == coordinates and enter[i] == ' ':
                    if not moves_count % 2:
                        enter[i] = 'X'
                        grid_print()
                        # flag = 1
                        moves_count += 1
                        break
                    else:
                        enter[i] = 'O'
                        grid_print()
                        # flag = 1
                        moves_count += 1
                        break

                i += 1
                if i >= 9:
                    i = c
                else:
                    if a < 9:
                        if coordinates_list[a] == coordinates and enter[a] != ' ':
                            print('This cell is occupied! Choose another one!')
                            a = c
                            break
                        a += 1
                        if a >= 9:
                            a = c


    def xwins(x):
        if enter[2] == enter[4] == enter[6] == "X" or enter[0] == enter[4] == enter[8] == "X" or \
                enter[0] == enter[1] == enter[2] == "X" or enter[3] == enter[4] == enter[5] == "X" or \
                enter[6] == enter[7] == enter[8] == "X" or enter[0] == enter[3] == enter[6] == "X" or \
                enter[1] == enter[4] == enter[7] == "X" or enter[2] == enter[5] == enter[8] == "X":
            return True


    def owins(x):
        if enter[2] == enter[4] == enter[6] == "O" or enter[0] == enter[4] == enter[8] == "O" or \
                enter[0] == enter[1] == enter[2] == "O" or enter[3] == enter[4] == enter[5] == "O" or \
                enter[6] == enter[7] == enter[8] == "O" or enter[0] == enter[3] == enter[6] == "O" or \
                enter[1] == enter[4] == enter[7] == "O" or enter[2] == enter[5] == enter[8] == "O":
            return True


    if owins(enter) is True:
        print("O wins")
        flag = 1
    elif xwins(enter) is True:
        print("X wins")
        flag = 1

    elif enter.count(" ") < 1:
        print("Draw")
        flag = 1


#building playground space
playground = [' ' for move in range(9)]        
# print(ground)

#building the ground & moves
def boundry():
    row1 = '| {} | {} | {} |'.format(playground[0], playground[1], playground[2])
    row2 = '| {} | {} | {} |'.format(playground[3], playground[4], playground[5])
    row3 = '| {} | {} | {} |'.format(playground[6], playground[7], playground[8])

    #designing the playground
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

#player's move function()
def move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print('Your turn player{}_'.format(number))

    #move
    user_input = int(input('Enter your move (1-9): ').strip())

    #move overwrite protection
    if playground[user_input - 1] == ' ':        #because, index starts from 0
        playground[user_input - 1] = icon 
    else:
        print()
        print('Oops! that move was taken_')

#check for victory
def victory(icon):
    if (playground[0] == icon and playground[1] == icon and playground[2] == icon) or\
       (playground[3] == icon and playground[4] == icon and playground[5] == icon) or\
       (playground[6] == icon and playground[7] == icon and playground[8] == icon) or\
       (playground[0] == icon and playground[3] == icon and playground[6] == icon) or\
       (playground[1] == icon and playground[4] == icon and playground[7] == icon) or\
       (playground[2] == icon and playground[5] == icon and playground[8] == icon) or\
       (playground[0] == icon and playground[4] == icon and playground[8] == icon) or\
       (playground[2] == icon and playground[4] == icon and playground[6] == icon):
       return True
    else:
        return False

#check for draw 
def draw():
    if ' ' not in playground:
        return True
    else:
        return False

#game loop
while True:
    boundry()

    move('X')
    boundry()
    if victory('X'):
        print('X Wins! Congratulations :) ')
        break
    elif draw():
        print('Yeah! It\'s a draw_')
        break

    move('O')
    boundry()
    if victory('O'):
        print('O Wins! Congratulations :) ')
        break
    elif draw():
        print('Yeah! It\'s a draw')
        break

 




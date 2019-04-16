def create_board():
        board_list=[]
        for i in range(11):
                board_list.append([])
                for j in range(11):
                        if i==0 :
                                board_list[i].append(j)
                        elif j==0:
                                board_list[i].append(i)
                        else:
                                board_list[i].append(' ')
        return board_list

def print_board(choose_board):
        for i in choose_board:
                for j in i:
                        if j!=10 : #ne csússzon el a tábla!
                                print(' '+str(j)+'|', end="")        
                        else:
                                print(str(j)+'|',end="")
                print()
        print("\n")            

#d=y+1
#u=y-1
#r=x+1
#l=x-1

def place_ship(ship_length,choose_board):  #paraméter, meghívásnál arg
        
        while True:
                try:
                        y=int(input("Row: "))
                        break
                except ValueError:
                        print("It's not a number!")
        while True:
                try:
                        x=int(input("Column: "))
                        break
                except ValueError:
                        print("It's not a number!")
        
        direction=input("Which direction?(r,l,d,u) ")
        good=[]
        if direction=="r":
                try:
                        for i in range(ship_length):
                                if choose_board[y][x+i]==" ": #változó is lehet, false után break
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        choose_board[y][x+i]='*'
                        else:
                                print("You can/'t place your ship there!")
                                place_ship(ship_length,choose_board) #recursive helyett loop, több függvény
                except IndexError:
                        print("Out of range! Try again!")
                        place_ship(ship_length,choose_board)
        if direction=="l":
                try:
                        for i in range(ship_length):
                                if choose_board[y][x-i]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        choose_board[y][x-i]='*'
                        else:
                                print("You can't place your ship here!")
                                place_ship(ship_length,choose_board)
                except IndexError:
                        print("Out of range! Try again!")
                        place_ship(ship_length,choose_board)        
        if direction=="d": #down
                try:
                        for i in range(ship_length):
                                if choose_board[y+i][x]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        choose_board[y+i][x]='*'
                        else:
                                print("You can't place your ship here!")
                                place_ship(ship_length,choose_board)
                except IndexError:
                        print("Out of range! Try again!")
                        place_ship(ship_length,choose_board)
        if direction=="u":
                try:
                        for i in range(ship_length):
                                if choose_board[y-i][x]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        choose_board[y-i][x]='*'
                        else:
                                print("You can't place your ship here!")
                                place_ship(ship_length,choose_board)
                except IndexError:
                        print("Out of range! Try again!")
                        place_ship
                (ship_length,choose_board)

board1=create_board()
board2=create_board()

# > 1 és <= len(lista)
print_board(board1)
print("Player 1, this is your board! Place your ship.")
ship_length=int(input("Press 2 to place your first ship! "))
place_ship(ship_length,board1)
print_board(board1)
ship_length=int(input("Press 3 to place your second ship! "))
place_ship(ship_length,board1)
print_board(board1)
ship_length=int(input("Press 4 to place your third ship! "))
place_ship(ship_length,board1)
print_board(board1)
ship_length=int(input("Press 5 to place your fourth ship! "))
place_ship(ship_length,board1)
print_board(board1)
print("Player 1 - your board with ships:")
print_board(board1)
print("\n"*21)

print_board(board2)
print("Player 2, this is your board! Place your ship.")
ship_length=int(input("Press 2 to place your first ship! "))
place_ship(ship_length,board2)
print_board(board2)
ship_length=int(input("Press 3 to place your second ship! "))
place_ship(ship_length,board2)
print_board(board2)
ship_length=int(input("Press 4 to place your third ship! "))
place_ship(ship_length,board2)
print_board(board2)
ship_length=int(input("Press 5 to place your fourth ship! "))
place_ship(ship_length,board2)
print_board(board2)
print("Player 2 - your board with ships:")
print_board(board2)
print("\n"*21)

guessboard1=create_board()
guessboard2=create_board()

def guess_place(c,d):
    while True:
            try:
                    x=int(input("Row: "))
                    if  x>= 11:
                        print("Error, out of range!")
                    elif x == 0:
                        print("Error, not an empty place!")
                    else:
                        break
            except ValueError:
                    print("It's not a number!")
    while True:
            try:
                    y=int(input("Column: "))
                    if y >= 11:
                        print("Error, out of range!")
                    elif y == 0:
                        print("Error, not an empty place!")
                    else:
                        break
            except ValueError:
                    print("It's not a number!")
    if c[x][y]!=" ":
        print("Error, not an empty place!")
        guess_place(c,d)
    else:   
        if d[x][y]=="*":
            d[x][y]="x"
            c[x][y]="x"
        else:
            c[x][y]="o"
def winner(b):
        there_is_no_star=[]
        for sublist in b:
                if "*" not in sublist:
                        there_is_no_star.append(True)
                else:
                        there_is_no_star.append(False)
        return False not in there_is_no_star

while True:
#       print_board(guessboard1)
        print("Player 1: Place your guess!")
        guess_place(guessboard1,board2)
        print("Player1 Guess board")
        print_board(guessboard1)

        print("\n" *4)
        if winner(board2):
                print("Player 1 wins")
                print("Player1 Ship board")
                print_board(board1)
                print("Player2 Ship board")
                print_board(board2)
                break
        #print("Player2 Guess board")
        #print_board(guessboard2)
        print("Player 2: Place your guess!")
        guess_place(guessboard2,board1)
        print("Player2 Guess board")
        print_board(guessboard2)

        print("\n" *4)
        #print(board1)
        if winner(board1):
                print("Player 2 wins")
                print("Player1 Ship board")
                print_board(board1)
                print("Player2 Ship board")
                print_board(board2)
                break
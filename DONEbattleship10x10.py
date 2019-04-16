def create_board():
        l=[]
        for i in range(11):
                l.append([])
                for j in range(11):
                        if i==0 :
                                l[i].append(j)
                        elif j==0:
                                l[i].append(i)
                        else:
                                l[i].append(' ')
        return l

def printboard(b):
        for i in b:
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

def ship_place(ship_length,b):  #paraméter, meghívásnál arg
        
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
        
        direction=input("Which direction? ")
        good=[]
        if direction=="r":
                try:
                        for i in range(ship_length):
                                if b[y][x+i]==" ": #változó is lehet, false után break
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        b[y][x+i]='*'
                        else:
                                print("You can/'t place your ship there!")
                                ship_place(ship_length,b) #recursive helyett loop, több függvény
                except IndexError:
                        print("Out of range! Try again!")
                        ship_place(ship_length,b)
        if direction=="l":
                try:
                        for i in range(ship_length):
                                if b[y][x-i]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        b[y][x-i]='*'
                        else:
                                print("You can\'t place your ship there!")
                                ship_place(ship_length,b)
                except IndexError:
                        print("Out of range! Try again!")
                        ship_place(ship_length)
        if direction=="d":
                try:
                        for i in range(ship_length):
                                if b[y+i][x]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        b[y+i][x]='*'
                        else:
                                print("You can\'t place your ship there!")
                                ship_place(ship_length,b)
                except IndexError:
                        print("Out of range! Try again!")
                        ship_place(ship_length),b
        if direction=="u":
                try:
                        for i in range(ship_length):
                                if b[y-i][x]==" ":
                                        good.append(True)
                                else:
                                        good.append(False)
                        if good.count(True)==len(good):
                                for i in range(ship_length):
                                        b[y-i][x]='*'
                        else:
                                print("You can\'t place your ship there!")
                                ship_place(ship_length,b)
                except IndexError:
                        print("Out of range! Try again!")
                        ship_place(ship_length,b)

board1=create_board()
board2=create_board()

# > 1 és <= len(lista)
printboard(board1)
print("Player 1, this is your board! Place your ship.")
ship_length=int(input("Press 2 to place your first ship! "))
ship_place(ship_length,board1)
printboard(board1)
ship_length=int(input("Press 3 to place your second ship! "))
ship_place(ship_length,board1)
printboard(board1)
ship_length=int(input("Press 4 to place your third ship! "))
ship_place(ship_length,board1)
printboard(board1)
ship_length=int(input("Press 5 to place your fourth ship! "))
ship_place(ship_length,board1)
printboard(board1)
print("Player 1 - your board with ships:")
printboard(board1)
print("\n"*21)

printboard(board2)
print("Player 2, this is your board! Place your ship.")
ship_length=int(input("Press 2 to place your first ship! "))
ship_place(ship_length,board2)
printboard(board2)
ship_length=int(input("Press 3 to place your second ship! "))
ship_place(ship_length,board2)
printboard(board2)
ship_length=int(input("Press 4 to place your third ship! "))
ship_place(ship_length,board2)
printboard(board2)
ship_length=int(input("Press 5 to place your fourth ship! "))
ship_place(ship_length,board2)
printboard(board2)
print("Player 2 - your board with ships:")
printboard(board2)
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
#        printboard(guessboard1)
        print("Player 1: Place your guess!")
        guess_place(guessboard1,board2)
        print("Player1 Guess board")
        printboard(guessboard1)

        print("\n" *4)
        if winner(board2):
                print("Player 1 wins")
                print("Player1 Ship board")
                printboard(board1)
                print("Player2 Ship board")
                printboard(board2)
                break
        #print("Player2 Guess board")
        #printboard(guessboard2)
        print("Player 2: Place your guess!")
        guess_place(guessboard2,board1)
        print("Player2 Guess board")
        printboard(guessboard2)

        print("\n" *4)
        #print(board1)
        if winner(board1):
                print("Player 2 wins")
                print("Player1 Ship board")
                printboard(board1)
                print("Player2 Ship board")
                printboard(board2)
                break
import random as ran

ans = [1, 2, 3, 4, 'O', 6, 7, 8, 9]

print(ans[0], ans[1], ans[2])  # game
print(ans[3], ans[4], ans[5])  # focus
print(ans[6], ans[7], ans[8])  # focus

def humanMove(value): #focus

    if value == "1":
        ans[0] = "X"  # focus
    elif value == "2":
        ans[1] = "X"  # focus
    elif value == "3":
        ans[2] = "X"  # focus
    elif value == "4":
        ans[3] = "X"  # focus
    elif value == "5":
        ans[4] = "X"  # focus
    elif value == "6":
        ans[5] = "X"  # focus
    elif value == "7":
        ans[6] = "X"  # focus
    elif value == "8":
        ans[7] = "X"  # focus
    elif value == "9":
        ans[8] = "X"  # focus

    print(ans[0], ans[1], ans[2])  # game
    print(ans[3], ans[4], ans[5])  # focus
    print(ans[6], ans[7], ans[8])  # focus

    return ans

def botMove():  # FOCUS ,game

    Vs = 1000
    Vb = 0
    value = 0

    if ans[0]== 1:
        A = 0
        B = 0
        if ans[1]==2 :
            A=A+1
        if ans[3]==4 :
            A=A+1
        if ans[1]!='X' :
            B=B+1
        if ans[3]!='X' :
            B=B+1
        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb1 : ', Vb)

        if Vb < Vs:
            Vs = Vb
            value = 1

    if ans[1] == 2:
        A = 0
        B = 0
        if ans[0] == 1:
            A = A + 1
        if ans[4] == 5:
            A = A + 1
        if ans[2] == 3:
            A = A + 1
        if ans[0] != 'X':
            B = B + 1
        if ans[4] != 'X':
            B = B + 1
        if ans[2] != 'X':
            B = B + 1
        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb2 : ', Vb)

        if Vb < Vs :
            Vs=Vb
            value = 2

    if ans[2] == 3:
        A = 0
        B = 0
        if ans[1] == 2:
            A = A + 1
        if ans[5] == 6:
            A = A + 1

        if ans[1] != 'X':
            B = B + 1
        if ans[5] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb3 : ', Vb)

        if Vb < Vs :
            Vs=Vb
            value = 3

    if ans[3] == 4:
        A = 0
        B = 0
        if ans[0] == 1:
            A = A + 1
        if ans[4] == 5:
            A = A + 1
        if ans[6] == 7:
            A = A + 1

        if ans[0] != 'X':
            B = B + 1
        if ans[4] != 'X':
            B = B + 1
        if ans[6] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb4 : ', Vb)

        if Vb < Vs :
            Vs=Vb
            value = 4

    if ans[5] == 6:
        A = 0
        B = 0
        if ans[2] == 3:
            A = A + 1
        if ans[4] == 5:
            A = A + 1
        if ans[8] == 9:
            A = A + 1

        if ans[2] != 'X':
            B = B + 1
        if ans[4] != 'X':
            B = B + 1
        if ans[8] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb6 : ', Vb)

        if Vb < Vs:
            Vs = Vb
            value = 6

    if ans[6] == 7:
        A = 0
        B = 0
        if ans[3] == 4:
            A = A + 1
        if ans[7] == 8:
            A = A + 1

        if ans[3] != 'X':
            B = B + 1
        if ans[7] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb7 : ', Vb)

        if Vb < Vs:
            Vs = Vb
            value = 7

    if ans[7] == 8:
        A = 0
        B = 0
        if ans[4] == 5:
            A = A + 1
        if ans[6] == 7:
            A = A + 1
        if ans[8] == 9:
            A = A + 1

        if ans[4] != 'X':
            B = B + 1
        if ans[6] != 'X':
            B = B + 1
        if ans[8] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb8 : ', Vb)

        if Vb < Vs:
            Vs = Vb
            value = 8

    if ans[8] == 9:
        A = 0
        B = 0
        if ans[5] == 6:
            A = A + 1
        if ans[7] == 8:
            A = A + 1

        if ans[5] != 'X':
            B = B + 1
        if ans[7] != 'X':
            B = B + 1

        # print('A : ', A)
        # print('B : ', B)
        Vb = A + B
        print('Vb9 : ', Vb)

        if Vb < Vs:
            Vs = Vb
            value = 9

    print('Vs : ', Vs)
    print('Value : ', value)

    if value == 1:
        ans[0] = "O"  # focus
    elif value == 2:
        ans[1] = "O"  # focus
    elif value == 3:
        ans[2] = "O"  # focus
    elif value == 4:
        ans[3] = "O"  # focus
    elif value == 5:
        ans[4] = "O"  # focus
    elif value == 6:
        ans[5] = "O"  # focus
    elif value == 7:
        ans[6] = "O"  # focus
    elif value == 8:
        ans[7] = "O"  # focus
    elif value == 9:
        ans[8] = "O"  # focus

    print(ans[0], ans[1], ans[2])  # focus
    print(ans[3], ans[4], ans[5])  # focus
    print(ans[6], ans[7], ans[8])  # focus


def win():
    won = False  # O

    if 'X' == ans[0] == ans[1] == ans[2]:  # focus # bun
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[3] == ans[4] == ans[5]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[6] == ans[7] == ans[8]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[0] == ans[3] == ans[6]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[1] == ans[4] == ans[7]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[2] == ans[5] == ans[8]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[0] == ans[4] == ans[8]:  # focus
        print('Player Win')# focus
        won = True  # O
    elif 'X' == ans[2] == ans[4] == ans[6]:  # focus
        print('Player Win')# focus
        won = True  # O

    elif 'O' == ans[0] == ans[1] == ans[2]:  # Liw , focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[3] == ans[4] == ans[5]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[6] == ans[7] == ans[8]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[0] == ans[3] == ans[6]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[1] == ans[4] == ans[7]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[2] == ans[5] == ans[8]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[0] == ans[4] == ans[8]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O
    elif 'O' == ans[2] == ans[4] == ans[6]:  # Liw, focus
        print('Bot Win')# Liw , focus
        won = True  # O

    elif ans[0] != 1 and ans[1] != 2 and ans[2] != 3 and ans[3] != 4 and ans[4] != 5 and ans[5] != 6 and ans[6] != 7 and ans[7] != 8 and ans[8] != 9:  # focus
        print('Game Draw') # focus
        won = True

    return won  # O

def space_exist():
    return ans.count('X') != 9  # O

i = 1
while space_exist():

    print('round : ',i) # focus
    value = input("Please enter a number : ")  # bun
    if int(value) >=10:# bun
        print('------Try again------')# bun
        continue# bun
    elif int(value) == 0:# bun
        print('------Try again------')# bun
        continue# bun

    value = humanMove(value)  # O
    botMove() # focus
    i = i+1
    won = win()  # O

    if won == True:  # O
        break  # O

# print(f'You entered {value}')


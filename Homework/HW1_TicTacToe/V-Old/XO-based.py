import random
# W0 = random.randint(-100,100)
# W1 = random.randint(-100,100)
ans = [1, 2, 3, 4, 'O', 6, 7, 8, 9]
print(' **************************** GAME START ****************************')  # game
def table(): # game focus
    print('                          [',ans[0],']','[',ans[1],']','[',ans[2],']',)  # game
    print('                          [',ans[3],']','[',ans[4],']','[',ans[5],']',)  # focus
    print('                          [',ans[6],']','[',ans[7],']','[',ans[8],']',)   # focus

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

    return ans

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

    return ans

def botMove():  # FOCUS ,game

    Vs = -1000
    Vb = 0
    value = 0

    if ans[0]== 1:
        A = 0
        B = 0
        C = 0
        #cheak A
        if ans[1] == 'X':
            A=A+1
        if ans[3] == 'X':
            A=A+1
        if ans[4] == 'X' :
            A=A+1
        #cheak B
        if ans[1] == 'O':
            B = B + 1
        if ans[2]== 'O':
            B = B + 1
        if ans[3]== 'O':
            B = B + 1
        if ans[6]== 'O':
            B = B + 1
        if ans[4]== 'O':
            B = B + 1
        if ans[8]== 'O':
            B = B + 1
        # cheak C
        C = C+1

        Vb = A+2*B+C
        print('ans[0] Vb =',Vb)
        if Vb > Vs:
            Vs = Vb
            value = 1


    if ans[1] == 2:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[0] == 'X':
            A = A + 1
        if ans[2] == 'X':
            A = A + 1
        if ans[3] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[5] == 'X':
            A = A + 1
        # cheak B
        if ans[0]== 'O':
            B = B + 1
        if ans[2]== 'O':
            B = B + 1
        if ans[4]== 'O':
            B = B + 1
        if ans[7]== 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[1] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 2

    if ans[2] == 3:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[1] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[5] == 'X':
            A = A + 1

        # cheak B
        if ans[0] == 'O':
            B = B + 1
        if ans[1] == 'O':
            B = B + 1
        if ans[5] == 'O':
            B = B + 1
        if ans[8] == 'O':
            B = B + 1
        if ans[4]== 'O':
            B = B + 1
        if ans[6]== 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[2] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 3

    if ans[3] == 4:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[0] == 'X':
            A = A + 1
        if ans[1] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[6] == 'X':
            A = A + 1
        if ans[7] == 'X':
            A = A + 1

        # cheak B
        if ans[0] == 'O':
            B = B + 1
        if ans[4] == 'O':
            B = B + 1
        if ans[5] == 'O':
            B = B + 1
        if ans[6] == 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[3] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 4

    if ans[4] == 5:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[0] == 'X':
            A = A + 1
        if ans[1] == 'X':
            A = A + 1
        if ans[2] == 'X':
            A = A + 1
        if ans[3] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[5] == 'X':
            A = A + 1
        if ans[6] == 'X':
            A = A + 1
        if ans[7] == 'X':
            A = A + 1
        if ans[8] == 'X':
            A = A + 1

        # cheak B
        if ans[1] == 'O':
            B = B + 1
        if ans[3] == 'O':
            B = B + 1
        if ans[5] == 'O':
            B = B + 1
        if ans[7] == 'O':
            B = B + 1
        # cheak C
        C = C + 2

        Vb = A + 2*B + C
        print('ans[4] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 5

    if ans[5] == 6:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[1] == 'X':
            A = A + 1
        if ans[2] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[7] == 'X':
            A = A + 1
        if ans[8] == 'X':
            A = A + 1

        # cheak B
        if ans[2] == 'O':
            B = B + 1
        if ans[3] == 'O':
            B = B + 1
        if ans[4] == 'O':
            B = B + 1
        if ans[8] == 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[5] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 6

    if ans[6] == 7:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[3] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[7] == 'X':
            A = A + 1

        # cheak B
        if ans[0] == 'O':
            B = B + 1
        if ans[3] == 'O':
            B = B + 1
        if ans[7] == 'O':
            B = B + 1
        if ans[8] == 'O':
            B = B + 1
        if ans[2]== 'O':
            B = B + 1
        if ans[4]== 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[6] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 7

    if ans[7] == 8:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[3] == 'X':
            A = A + 1
        if ans[4] == 'X':
            A = A + 1
        if ans[5] == 'X':
            A = A + 1
        if ans[6] == 'X':
            A = A + 1
        if ans[8] == 'X':
            A = A + 1

        # cheak B
        if ans[1] == 'O':
            B = B + 1
        if ans[4] == 'O':
            B = B + 1
        if ans[6] == 'O':
            B = B + 1
        if ans[8] == 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[7] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 8

    if ans[8] == 9:
        A = 0
        B = 0
        C = 0
        # cheak A
        if ans[4] == 'X':
            A = A + 1
        if ans[5] == 'X':
            A = A + 1
        if ans[7] == 'X':
            A = A + 1

        # cheak B
        if ans[2] == 'O':
            B = B + 1
        if ans[5] == 'O':
            B = B + 1
        if ans[6] == 'O':
            B = B + 1
        if ans[7] == 'O':
            B = B + 1
        if ans[0]== 'O':
            B = B + 1
        if ans[4]== 'O':
            B = B + 1
        # cheak C
        C = C + 1

        Vb = A + 2*B + C
        print('ans[8] Vb =', Vb)
        if Vb > Vs:
            Vs = Vb
            value = 9



    if value == 1:
        ans[0] = "O"  # focus
        print('choose ans[0]')
    elif value == 2:
        ans[1] = "O"  # focus
        print('choose ans[1]')
    elif value == 3:
        ans[2] = "O"  # focus
        print('choose ans[2]')
    elif value == 4:
        ans[3] = "O"  # focus
        print('choose ans[3]')
    elif value == 5:
        ans[4] = "O"  # focus
        print('choose ans[4]')
    elif value == 6:
        ans[5] = "O"  # focus
        print('choose ans[5]')
    elif value == 7:
        ans[6] = "O"  # focus
        print('choose ans[6]')
    elif value == 8:
        ans[7] = "O"  # focus
        print('choose ans[7]')
    elif value == 9:
        ans[8] = "O"  # focus
        print('choose ans[8]')


def win():
    won = False  # O

    if 'X' == ans[0] == ans[1] == ans[2] or 'X' == ans[3] == ans[4] == ans[5] or 'X' == ans[6] == ans[7] == ans[8] or 'X' == ans[0] == ans[3] == ans[6] or 'X' ==  ans[1] == ans[4] == ans[7] or 'X' == ans[2] == ans[5] == ans[8] or 'X' == ans[0] == ans[4] == ans[8] or 'X' == ans[2] == ans[4] == ans[6]  : # focus # bun
        print('****************************Player Win****************************')# focus
        won = True  # O
    
    elif 'O' == ans[0] == ans[1] == ans[2] or 'O' ==  ans[3] == ans[4] == ans[5] or 'O' ==  ans[6] == ans[7] == ans[8] or  'O' ==  ans[0] == ans[3] == ans[6] or 'O' ==  ans[1] == ans[4] == ans[7] or  'O' == ans[2] == ans[5] == ans[8] or 'O' == ans[0] == ans[4] == ans[8] or'O' ==  ans[2] == ans[4] == ans[6]  : # focus # bun
       
        print('****************************Bot Win****************************')# Liw , focus
        won = True  # O

    elif ans[0] != 1 and ans[1] != 2 and ans[2] != 3 and ans[3] != 4 and ans[4] != 5 and ans[5] != 6 and ans[6] != 7 and ans[7] != 8 and ans[8] != 9:  # focus
        print('****************************Game Draw****************************') # focus
        won = True
    if won == True :
        table()

    return won  # O

def space_exist():
    return ans.count('X') != 5  # O

i = 1
while space_exist():

    print('round :',i) # focus
    table()
    value = input("Please enter a number : ")  # bun

    if int(value) >=10:# bun
        print('------Try again------')# bun
        continue# bun
    elif int(value) == 0:# bun
        print('------Try again------')# bun
        continue# bun
    elif int(value) == 5:# bun , focus
        print('------Try again------')# bun
        continue# bun
    else: #focus
        value = humanMove(value)  # O
        won = win()  # O
        botMove()  # focus
        won = win()
        i = i+1

    if won == True:  # O
        break  # O

# print(f'You entered {value}')


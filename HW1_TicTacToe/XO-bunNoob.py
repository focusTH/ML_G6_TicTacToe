import random
from matplotlib.pyplot import table
import numpy as np

W0 = random.randint(-100, 100)
W1 = random.randint(-100, 100)
W2 = random.randint(-100, 100)
W3 = random.randint(-100, 100)



   
def table(): # game focus
    print('                          [',ans[0],']','[',ans[1],']','[',ans[2],']',)  # game
    print('                          [',ans[3],']','[',ans[4],']','[',ans[5],']',)  # focus
    print('                          [',ans[6],']','[',ans[7],']','[',ans[8],']',)   # focus

def humanMove(): #focus
    value = input("Please enter a number : ")  # bun
    if int(value) >=10:# bun
        print('------Try again------')# bun
        # continue# bun
    elif int(value) == 0:# bun
        print('------Try again------')# bun
        # continue# bun 
    elif value == "1":
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

def win():
    won = False  # O

    if 'X'  == ans[0] == ans[1] == ans[2] or 'X' == ans[3] == ans[4] == ans[5] or 'X' == ans[6] == ans[7] == ans[
        8] or 'X' == ans[0] == ans[3] == ans[6] or 'X' == ans[1] == ans[4] == ans[7] or 'X' == ans[2] == ans[5] == ans[
        8] or 'X' == ans[0] == ans[4] == ans[8] or 'X' == ans[2] == ans[4] == ans[6]:  # focus # bun
        print('****************************Player Win****************************')  # focus
        won = True  # O

    elif 'O' == ans[0] == ans[1] == ans[2] or 'O' == ans[3] == ans[4] == ans[5] or 'O' == ans[6] == ans[7] == ans[
        8] or 'O' == ans[0] == ans[3] == ans[6] or 'O' == ans[1] == ans[4] == ans[7] or 'O' == ans[2] == ans[5] == ans[
        8] or 'O' == ans[0] == ans[4] == ans[8] or 'O' == ans[2] == ans[4] == ans[6]:  # focus # bun

        print('****************************Bot Win****************************')  # Liw , focus
        won = True  # O

    elif ans[0] != 1 and ans[1] != 2 and ans[2] != 3 and ans[3] != 4 and ans[4] != 5 and ans[5] != 6 and ans[6] != 7 and \
            ans[7] != 8 and ans[8] != 9:  # focus
        print('****************************Game Draw****************************')  # focus
        won = True
    if won == True:
        table()

    return won  # O

def space_exist():
    return ans.count('X') != 5  # O

   

        
while True:
    
    answer = input('Do you want to play ? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        
        i = 1
        ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(' **************************** GAME START ****************************')  # game

        while space_exist():

            print('round :',i) # focus
            #********************************
            Vb = 0
            Vb1 = []
            value = 0

            value1 = []
            if i == 1:
                # W0 = random.randint(-100, 100)
                # W1 = random.randint(-100, 100)
                # W2 = random.randint(-100, 100)
                # W3 = random.randint(-100, 100)
                Vs = -1000
            else:
                Vt = Vs
                Vs = -1000
                # print(Vt)

            print('W0 =', W0, ',W1 =', W1, ',W2 =', W2, ',W3 =', W3)
            if ans[0] == 1:
                A = 0
                B = 0
                C = 0
                # cheak A
                if ans[1] == 'X':
                    A = A + 1
                if ans[3] == 'X':
                    A = A + 1
                if ans[4] == 'X':
                    A = A + 1
                # cheak B
                if ans[1] == 'O':
                    B = B + 1
                if ans[2] == 'O':
                    B = B + 1
                if ans[3] == 'O':
                    B = B + 1
                if ans[6] == 'O':
                    B = B + 1
                if ans[4] == 'O':
                    B = B + 1
                if ans[8] == 'O':
                    B = B + 1
                # cheak C
                C = C + 1

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[0] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 1
                    f1 = A
                    f2 = 2 * B
                    f3 = C

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
                if ans[0] == 'O':
                    B = B + 1
                if ans[2] == 'O':
                    B = B + 1
                if ans[4] == 'O':
                    B = B + 1
                if ans[7] == 'O':
                    B = B + 1
                # cheak C
                C = C + 1

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[1] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 2
                    f1 = A
                    f2 = 2 * B
                    f3 = C
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
                if ans[4] == 'O':
                    B = B + 1
                if ans[6] == 'O':
                    B = B + 1
                # cheak C
                C = C + 1

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[2] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 3
                    f1 = A
                    f2 = 2 * B
                    f3 = C
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

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[3] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 4
                    f1 = A
                    f2 = 2 * B
                    f3 = C

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

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[4] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 5
                    f1 = A
                    f2 = 2 * B
                    f3 = C

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

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[5] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 6
                    f1 = A
                    f2 = 2 * B
                    f3 = C
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
                if ans[2] == 'O':
                    B = B + 1
                if ans[4] == 'O':
                    B = B + 1
                # cheak C
                C = C + 1

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[6] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 7
                    f1 = A
                    f2 = 2 * B
                    f3 = C
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

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[7] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 8
                    f1 = A
                    f2 = 2 * B
                    f3 = C
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
                if ans[0] == 'O':
                    B = B + 1
                if ans[4] == 'O':
                    B = B + 1
                # cheak C
                C = C + 1

                Vb = W0+W1*A + W2*2*B + W3*C
                print('ans[8] Vb =', Vb)
                Vb1.append(Vb)
                if Vb > Vs:
                    Vs = Vb
                    value = 9
                    f1 = A
                    f2 = 2 * B
                    f3 = C

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



            # print('Max Vb1', max(Vb1))
            # print('np.argmax Vb1',np.argmax(Vb1))
            if i != 1:
                print('Vt', Vt)
                print('Vs', Vs)
                error = Vt - Vs
                print('error',error)
                W0 = W0 + 0.1 * 1 * error
                W1 = W1 + 0.1 * f1 * error
                W2 = W2 + 0.1 * f2 * error
                W3 = W3 + 0.1 * f3 * error
                print('weight : f1,f2,f3 :',W0,W1,W2,W3,f1,f2,f3)
                

            # *******************************
            table()
            won = win()
            if won == True:  # O
                break  # O
            value = input("Please enter a number : ")  # bun
            if int(value) >=10:# bun
                print('------Try again------')# bun
                continue# bun
            elif int(value) == 0:# bun
                print('------Try again------')# bun
                continue# bun
            value = humanMove(value)  # O
            i = i+1
            print('W0-3',W0,W1,W2,W3)
    else:
        break


# print(f'You entered {value}')


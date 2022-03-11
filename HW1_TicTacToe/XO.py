import random as ran
ans = ['1', '2', '3', '4', 'O', '6', '7', '8', '9']
A=0
B=0
Vs=0
Vb=100
print(ans[0], ans[1], ans[2])  # game
print(ans[3], ans[4], ans[5])  # focus
print(ans[6], ans[7], ans[8])  # focus


def move(value,i,A,B,Vs,Vb):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 9 :
        # if ans[0]==1 :
        #     if ans[1]==2 :
        #         A=A+1
        #     if ans[3]==4 :
        #         A=A+1
        #     if ans[1]!='X' :
        #         B=B+1
        #     if ans[3]!='X' :
        #         B=B+1
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs :
        #     Vs=Vb
        #
        # if ans[1] == 2:
        #     if ans[0] == 1:
        #         A = A + 1
        #     if ans[4] == 5:
        #         A = A + 1
        #     if ans[2] == 3:
        #         A = A + 1
        #     if ans[0] != 'X':
        #         B = B + 1
        #     if ans[4] != 'X':
        #         B = B + 1
        #     if ans[2] != 'X':
        #         B = B + 1
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs :
        #     Vs=Vb
        #
        # if ans[2] == 3:
        #     if ans[1] == 2:
        #         A = A + 1
        #     if ans[5] == 6:
        #         A = A + 1
        #
        #     if ans[1] != 'X':
        #         B = B + 1
        #     if ans[5] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs :
        #     Vs=Vb
        #
        # if ans[3] == 4:
        #     if ans[0] == 1:
        #         A = A + 1
        #     if ans[4] == 5:
        #         A = A + 1
        #     if ans[6] == 7:
        #         A = A + 1
        #
        #     if ans[0] != 'X':
        #         B = B + 1
        #     if ans[4] != 'X':
        #         B = B + 1
        #     if ans[6] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs :
        #     Vs=Vb
        #
        # if ans[5] == 6:
        #     if ans[2] == 3:
        #         A = A + 1
        #     if ans[4] == 5:
        #         A = A + 1
        #     if ans[8] == 9:
        #         A = A + 1
        #
        #     if ans[2] != 'X':
        #         B = B + 1
        #     if ans[4] != 'X':
        #         B = B + 1
        #     if ans[8] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs:
        #     Vs = Vb
        #
        # if ans[6] == 7:
        #     if ans[3] == 4:
        #         A = A + 1
        #     if ans[7] == 8:
        #         A = A + 1
        #
        #
        #     if ans[3] != 'X':
        #         B = B + 1
        #     if ans[7] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs:
        #     Vs = Vb
        #
        # if ans[7] == 8:
        #     if ans[4] == 5:
        #         A = A + 1
        #     if ans[6] == 7:
        #         A = A + 1
        #     if ans[8] == 9:
        #         A = A + 1
        #
        #     if ans[4] != 'X':
        #         B = B + 1
        #     if ans[6] != 'X':
        #         B = B + 1
        #     if ans[8] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
        #
        # if Vb < Vs:
        #     Vs = Vb
        #
        # if ans[8] == 9:
        #     if ans[5] == 5:
        #         A = A + 1
        #     if ans[7] == 7:
        #         A = A + 1
        #
        #     if ans[5] != 'X':
        #         B = B + 1
        #     if ans[7] != 'X':
        #         B = B + 1
        #
        #     print('A : ', A)
        #     print('B : ', B)
        #     Vb = A + B
        #     print('Vb : ', Vb)
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
    else :
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


def win():
    won = False  # O
    if ans[0] == ans[1] == ans[2]:  # Liw
        print('win')
        won = True  # O
    elif ans[3] == ans[4] == ans[5]:  # Liw
        print('win')
        won = True  # O
    elif ans[6] == ans[7] == ans[8]:  # Liw
        print('win')
        won = True  # O
    elif ans[0] == ans[3] == ans[6]:  # Liw
        print('win')
        won = True  # O
    elif ans[1] == ans[4] == ans[7]:  # Liw
        print('win')
        won = True  # O
    elif ans[2] == ans[5] == ans[8]:  # Liw
        print('win')
        won = True  # O
    elif ans[0] == ans[4] == ans[8]:  # Liw
        print('win')
        won = True  # O
    elif ans[2] == ans[4] == ans[6]:  # Liw
        print('win')
        won = True  # O
    elif i == 10:  # Liw
        print('draw')
        won = True
    return won  # O


def space_exist():
    return ans.count('X') != 9  # O

i = 1
while space_exist():

    print('round ',i)
    value = input("Please enter a number : ")  # bun
    value = move(value,i,A,B,Vs,Vb)  # O
    i=i+1
    won = win()  # O

    if won == True:  # O
        break  # O

# print(f'You entered {value}')


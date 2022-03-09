import random as ran
ans=['1','2','3','4','5','6','7','8','9']

print(ans[0],ans[1],ans[2]) #game
print(ans[3],ans[4],ans[5]) #focus
print(ans[6],ans[7],ans[8]) #focus

value = input("Please enter a number : ") #bun
# print(f'You entered {value}')

if value == "1":
    ans[0] = "X" #focus
elif value == "2":
    ans[1] = "X" #focus
elif value == "3":
    ans[2] = "X" #focus
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


print(ans[0],ans[1],ans[2]) #game
print(ans[3],ans[4],ans[5]) #focus
print(ans[6],ans[7],ans[8]) #focus

if ans[0]==ans[1]==ans[2]:
    print('win')
elif ans[3] == ans[4] == ans[5]:
    print('win')
elif ans[6] == ans[7] == ans[8]:
    print('win')
elif ans[0] == ans[3] == ans[6]:
    print('win')
elif ans[1] == ans[4] == ans[7]:
    print('win')
elif ans[2] == ans[5] == ans[8]:
    print('win')
elif ans[0] == ans[4] == ans[8]:
    print('win')
elif ans[2] == ans[4] == ans[6]:
    print('win')
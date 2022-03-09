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



print(ans[0],ans[1],ans[2]) #game
print(ans[3],ans[4],ans[5]) #focus
print(ans[6],ans[7],ans[8]) #focus
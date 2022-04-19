from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

x = loadmat('HR1.mat')
# print(x)
xLen = len(x)

sex = x['sex'];
sexLen = len(sex)
dep = x['dep'];
depLen = len(dep)

arrAll = []  #นำข้อมูลมาใส่ขั้นแรก
arrRep = []  #แยกตัวซ้ำ
numRep = 0    #จำนวนสายงาน
arrNum = [] #จำนวนคนตามแต่ละสายงาน


#
# choice = input("\nโปรดเลือก set ของข้อมูลที่ต้องการ\n[1]เฉพาะเพศ [2]เฉพาะสายงาน [3]รวมทั้ง 2 อย่าง : ")
#
#
# if choice == '1':
#   print("เฉพาะเพศ")
#   sex = x['sex']
#   arr_sex = []
#   for i in range(sex.size):
#
#     arr_sex.append(sex[i, 0][0])
#     # print(i)
#   # print(sex.size)
#   # print(sex[0,0])
#   print(arr_sex)
#   print("ช :", arr_sex.count('ช'))
#   print("ญ :", arr_sex.count('ญ'))
#   print("ช+ญ :", arr_sex.count('ญ') + arr_sex.count('ช'))
#
#
# elif choice == '2':
#   print("เฉพาะสายงาน")
#
#   for x in range(depLen):
#     c = dep[x,0][0]
#     arrAll.append(c)
#
#   for x in range(depLen):
#     if arrAll[x] not in arrRep:
#       arrRep.append(arrAll[x])
#       numRep = numRep + 1
#   print(arrAll)
#
#   for x in range(numRep):
#     arrNum.append(arrAll.count(arrRep[x]))
#
#   print("\nมีทั้งหมด ", numRep, " ตำแหน่ง\n")
#
#   for x in range(numRep):
#     print(arrRep[x], ' = ', arrNum[x], ' คน')
#
#   print('\nรวมทั้งหมด = ', len(arrAll), ' คน')


# elif choice == '3':
print("รวมทั้ง 2 อย่าง")
for x in range(depLen):
  c = dep[x,0][0],sex[x,0][0]
  arrAll.append(c)
print(arrAll)
for x in range(depLen):
  if arrAll[x] not in arrRep:
    arrRep.append(arrAll[x])
    numRep = numRep+1
arrNumb = []
arrRepb = []
numRepb=0
arrNumg = []
arrRepg = []
numRepg = 0
for x in range(depLen):
  if arrAll[x] not in arrRepb and arrAll[x][1]!= 'ญ':
    arrRepb.append(arrAll[x])
    numRepb = numRepb+1
for x in range(depLen):
  if arrAll[x] not in arrRepg and arrAll[x][1]!= 'ช':
    arrRepg.append(arrAll[x])
    numRepg = numRepg+1
for x in range(numRep):
  arrNum.append(arrAll.count(arrRep[x]))
for x in range(numRepb):
  arrNumb.append(arrAll.count(arrRepb[x]))
for x in range(numRepg):
  arrNumg.append(arrAll.count(arrRepg[x]))
# print("\nมีทั้งหมด ",numRep," ตำแหน่ง(แยกช./ญ.)\n")
# for x in range(numRep):
#   print(arrRep[x],' = ',arrNum[x],' คน')
# for x in range(numRepb):
#   print(arrRepb[x],' = ',arrNumb[x],' คน')
# for x in range(numRepg):
#   print(arrRepg[x],' = ',arrNumg[x],' คน')
print('\nรวมทั้งหมด = ',len(arrAll),' คน')
x = int(arrNumb[0]/2)
x_ = int(arrNumb[0]/2)
y = int(arrNumg[0]/2)
y_ = int(arrNumg[0]/2)
# print("boy:",x,x_," girl:",y,y_)

# [1, 2, -3, 0, 1, 1]
# plt.plot(x, y, '.')
# plt.plot(x_, y_, 'r')
# plt.show()

def fitness(P, x, y):
    e = []
    for p in P:
        z = np.polyval(p, x)
        e.append(np.sum((z-y) ** 2))
    return e

def xover(p1, p2):
    xp = np.random.randint(len(p1))
    c1 = np.concatenate((p1[:xp], p2[xp:]))
    c2 = np.concatenate((p2[:xp], p1[xp:]))
    return c1, c2

def mutate(p1):
    xp = np.random.randint(len(p1))
    c1 = p1.copy()
    c1[xp] += np.random.randn()
    return c1
color1sex = []
color2sex = []
arrPerson =[]
degree = 5
n_pop = 100
n_sel = 50
P = np.random.randn(n_pop, degree)
n_gen = 1e4
i_gen = 0
for p in range(19) :
    print(p)
    while i_gen < n_gen:

        if p>16 :
            r = p-2
        else : r = p

        x = int(arrNumb[r] / 2)
        x_ = int(arrNumb[r] / 2)
        y = int(arrNumg[p] / 2)
        y_ = int(arrNumg[p] / 2)
        i_gen += 1
        # Selection
        F = fitness(P, x, y)
        i = np.argsort(F)
        P = P[i]
        print(f'fitness = {F[i[0]]}')
        plt.clf()
        plt.plot(x, y, '.')  # problem
        plt.plot(x_, y_, 'r')  # solution
        z = np.polyval(P[0], x_)
        plt.plot(x_, z, 'g')  # GA
        plt.show(block=False)
        plt.pause(0.1)
        # Reproduction
        # Sexual
        for j in range(n_sel, n_pop, 2):
            p1p2 = np.random.permutation(n_sel)[:2]
            P[j], P[j+1] = xover(P[p1p2[0]], P[p1p2[1]])
        # Asexual
        for j in range(n_sel, n_pop):
            if np.random.rand() > 0.8:
                P[j] = mutate(P[np.random.randint(n_sel)])


        if F[i[0]]<=1:
            x1 = arrNumb[r]-x
            y1 = arrNumg[p]-y
            for x in range(x1):
                color1sex.append('ชาย')
            for x in range(y1):
                color1sex.append('หญิง')
            for x in range(x):
                color2sex.append('ชาย')
            for x in range(y):
                color2sex.append('หญิง')

            print('color1 : ',color1sex,'\ncolor2 : ',color2sex)


            print("boy:", x1, x_, " girl:", y1, y_)
            break


# else:
#   print("End Program")
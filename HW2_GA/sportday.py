from scipy.io import loadmat

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

# for x in range(xLen):
#   c = dep[x,0][0]
#   arrAll.append(c)

for x in range(depLen):
  c = dep[x,0][0],sex[x,0][0]
  arrAll.append(c)
# print(arrAll)

for x in range(depLen):
  if arrAll[x] not in arrRep:
    arrRep.append(arrAll[x])
    numRep = numRep+1

for x in range(numRep):
  arrNum.append(arrAll.count(arrRep[x]))

print("\nมีทั้งหมด ",numRep," ตำแหน่ง(แยกช./ญ.)\n")

for x in range(numRep):
  print(arrRep[x],' = ',arrNum[x],' คน')

print('\nรวมทั้งหมด = ',len(arrAll),' คน')



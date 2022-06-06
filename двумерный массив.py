#rf-read file
#rfn-read the file name

def rf(rfn=""):
    with open(rfn, 'r') as file:
        massive = []
        for s in file:
            c=s.split('\n')[0]
            c=c.split( )
            massive=[]
            for k in c:
                k=int(k)
                massive.append(k)
            massive_1.append(massive)
    return massive_1

def rec(i, j, massive_1, mas):
    tekelement = massive_1[i][j]
    massive_1[i][j]=0
    mas.append(tekelement)
    try:
        if massive_1[i-1][j]==tekelement:
            if not massive_1[i-1][j]==massive_1[-1][j]:
                x = rec(i-1, j, massive_1, mas)
    except IndexError:
       x=0
    try:
        if massive_1[i][j + 1] == tekelement:
            if not massive_1[i][j+1]==massive_1[i][0]:
                x=rec(i, j+1, massive_1, mas)
    except IndexError:
        x=0
    try:
        if massive_1[i + 1][j] == tekelement:
            if not massive_1[i+1][j]==massive_1[0][j]:
                x = rec(i+1, j, massive_1, mas)
    except IndexError:
        x=0
    try:
        if massive_1[i][j - 1] == tekelement:
            if not massive_1[i][j-1]==massive_1[i][-1]:
                x = rec(i, j - 1, massive_1, mas)
    except IndexError:
        x=0
    return mas

massive_1=[]
rfn = input("Введите название файла, содержащий массив: ")
massive_1=rf(rfn)
k=0

#если нужно вывести сам массив (из файла)
#for i in range(len(massive_1)):
#     for j in range(len(massive_1[i])):
#         print(massive_1[i][j], end=' ')
#     print()

#если нужно вывести только кол-во получившихся пар
for i in range(len(massive_1)):
     for j in range(len(massive_1[i])):
         if massive_1[i][j] == 0:
             continue
         else:
             mas=[]
             function=rec(i, j, massive_1, mas)
             k+=1
print("Количество получившихся из массива пар: ", k)
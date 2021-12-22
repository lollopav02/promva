#sommatoria righe e colonna matrice 3x3

mytab=[
    [1,2,3],
    [2,3,2],
    [3,4,1]
]

s_r=[]
s_c=[]

for i in range(len(mytab)):
    s=0
    for j in range(len(mytab[i])):
       s += mytab[i][j]
    s_r.append(s)
print(s_r)

for j in range(len(mytab[0])):
    s=0
    for i in range(len(mytab)):
        s+=mytab[i][j]
    s_c.append(s)
print(s_c)

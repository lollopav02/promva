cost=int(input("inserire costante: "))
mappa=[[0]*cost]
print(mappa)
for i in range(cost-1):
    mappa.append([0]*cost)
print(mappa)

print("*******************")

mappa2=[[0]*cost for i in range(cost)]
print(mappa2)
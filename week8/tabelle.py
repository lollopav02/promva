myreg=[]

myreg=[
    [22,23,24],
    [25,26,27],
    [28,29,19],
]

print(myreg)
print(myreg[1])
print(myreg[2][2])
stud=2
exam=2
print(myreg[stud-1][exam])
#stampa tabella colonna per colonna
print("####################")

for i in range(len(myreg)):
    for j in range(len(myreg[0])):
        print(myreg[i][j], " ",end=" ")
    print()


print("prodotto per scalare: ")
k=2
for i in range(len(myreg)):
    for j in range(len(myreg[0])):
        myreg[i][j]=myreg[i][j]*k
print(myreg)


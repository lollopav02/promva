#lettura da file di una matrice di interi di dimensioni non note a priori

#filename="matrice.txt"
fp_in=open("matrice.txt", "r", encoding="utf-8")

m=[]

for line in fp_in:
    row=[]
    for word in line.split():
        row.append(int(word))
    m.append(row)


print(m)

fp_in.close()
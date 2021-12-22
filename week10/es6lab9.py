"""
 Scrivere un programma che generi una “spirale” di numeri interi inserita in una
matrice di NxN elementi, con N inserito dall’utente. I numeri saranno i valori
compresi tra 1 e N2
.
Suggerimento: costruire prima la spirale numerica in una tabella NxN, e solo
successivamente stamparla.
Ad esempio, se N=4, il programma dovrà stampare:

1 2 3 4       ⨀ → → ↴
12 13 14 5    ↱ → ↴ ↓
11 16 15 6    ↑ ⨂ ↵ ↓
10 9 8 7      ↑ ← ← ↵
"""

n_matrix=input("inserire dimensione matrice: ")
while n_matrix !="" or n_matrix=="":
    n_matrix=int(n_matrix)
    matrix=[]
    for i in range(n_matrix):
        for j in range(n_matrix):
            matrix.append([0]*n_matrix)
    #ciclo fino a mezza diagonale della matrice
    val=1
    for strato in range(0,n_matrix):
        row=strato
        col=strato
    #mi sposto a destra
        for j in range(col,n_matrix-strato):
            matrix[row][j]=val
            val +=1
        col=j
    #mi sposto in basso:
        for i in range(row+1,n_matrix-strato):
            matrix[i][col]=val
            val +=1
        row=i
    #mi sposto a sinistra
        for j in range(col-1,strato-1,-1):
            matrix[row][j]=val
            val+=1
        col=j
    #mi sposto in alto
        for i in range(row-1,strato,-1):
            matrix[i][col]=val
            val+=1
    for i in range(n_matrix):
        print(matrix[i])
    n_matrix=int(input("inserire dimensione matrice: "))




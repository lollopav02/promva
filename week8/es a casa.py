#letta una matrice di dimensioni non note a priori,cercare il centro
#della sottomatrice 3x3 di somma Massima

def sumsubmatrix3x3(f_matrix,ix,jx):
    s=0
    for i in range(ix-1,ix+1+1):
        for j in range(jx-1,jx+1):
            s+= f_matrix[i][j]
    return s

def main():

    mytab=[ #M=5 -> len(mytab[0]) == 5->range(1,len(mytab[0])==(1,5)====(1,4)
        [1, 2, 3, 4, 5],#0
        [1, 2, 9, 8, 7],#1
        [1, 2, 1, 2, 1],#2<- N=4-> len(mytab)== 4 -> range(1,len(mytab))==(1,3-1]
        [2, 1, 2, 1, 5] #3
    ]
    r_max=1
    c_max=1
    s_max=sumsubmatrix3x3(mytab,1,1)
    for r in range(1,len(mytab)-1 ):
        for c in range(1,len(mytab[0])-1):
            s=sumsubmatrix3x3(mytab,r,c)
            if s>s_max:
                s_max=s
                r_max=r
                c_max=c
    print("row",r_max)
    print("col:",c_max)
    return

main()
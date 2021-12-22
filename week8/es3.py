#funzione che legge una matrica di interi

def printtab(f_matrix):
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[i])):
            print(f_matrix[i][j],end=" ")
        print()
    return

def readTab_nXm(r,c):
    f_matrix=[]
    for i in range(r):
        f_list= []
        for j in range(c):
            print("valore[%d][&d]: " %(i,j),end=" ")
            val=int(input())
            f_list.append(val)
    return f_matrix



def main():
    row=2
    col=2
    mytab=readTab_nXm(row,col)
    printtab(mytab)

    return


main()
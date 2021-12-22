#ricerca del massimo in una matrice

def searchMax(f_matrix):
    i_max=0
    j_max=0
    v_max=f_matrix[0][0]
    for i in range(len(f_matrix)):
        for j in range(len(f_matrix[i])):
            if f_matrix[i][j]>max:
                v_max=f_matrix[i][j]
                i_max=i
                j_max=j

    return i_max,j_max


def main():
    mytab=[
        [13,2,3,],
        [1,22,3,],
        [3,23,3,],
    ]
    (r_max,c_max)=searchMax(mytab)
    print("valore massimo",mytab[r_max][c_max])
    return

main()
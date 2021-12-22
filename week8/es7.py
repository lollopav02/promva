#aggiunta colonna a matrice

def add_c(f_matrix,f_list):
    for i in range(len(f_list)):
        f_matrix[i].append(f_list[i])

return f_matrix



def main():

    myTab=[
        [1,2,3],
        [4,5,6]
        ]
    mylist=[11,12]
    mytab=add_c(myTab,mylist)
    print(myTab)
return

main()
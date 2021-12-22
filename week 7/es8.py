
#ricerca minimo in lista di valori numerici; ritorna posizione minimo

def searchmin(f_list):
    min= f_list[0]
    pos=0
    for i in range(1,len(f_list)):
        if f_list[i]<min:
            min=f_list[i]
            pos=i


    return pos


def main():
    mylist=[1,2,5,0,11]
    pos_min=searchmin(mylist)
    print("volore minimo: ",mylist[pos_min],"in posizione: ", pos_min)
    return

main()
#elimina elementi minori di una soglia

def delLwrTh(f_list,f_th):
    i=0
    while i<len(f_list):
        if f_list[i]<f_th:
            f_list.pop(i)
        else:
            i+=1
            return f_list

def main():
    mylist=[1,3,5,7,9,11,2,3]
    th=9
    milist2=[]
    mylist2=delLwrTh(mylist,th)
    print(mylist)
    return

main()
def mergeord(f_list1,f_list2):
    f_t_list1=list(f_list1)
    f_t_list2=list(f_list2)
    f_t_list1.sort()
    f_t_list2.sort()
    f_list=[]
    finito1=False
    finito2=False
while not (finito1 and finito2):
    if not finito1 and not finito2:
        if f_t_list1[0] < f_t_list2[0]:
            f_list.append(f_list2[0])
            f_t_list1.pop(0)
            if len(f_t_list1) == 0:
                finito1 = True
        else:
            f_list.append(f_list2[0])
            f_t_list2.pop(0)
            if len(f_t_list2) == 0:
                finito2 = True
    elif finito1 and not finito2:
        for item in f_t_list2:
            f_list.append(item)
            finito2 = True
    elif not finito1 and finito2:
        for item in f_t_list1:
            f_list.append(item)
        finito1 = True

    return f_list


def main():
    mylist1=[1,5,7,11,4]
    mylist2=[2,2,9,11]
    mylist=mergeord(mylist1,mylist2 )
    return

main()



#print contenuto lista


def printlist(f_list):
    for (i,item) in enumerate(f_list):
        print("pos",i,"valore",item)
    return

def readist():
    f_list=[]
    finito = False
    while not finito:
        val=input("valore:")
        if val== "":
            finito=True
        else:
            val=int(val)
            f_list.append(val)
    return f_list

def readlist(flist):
    finito=False
    while not finito:
        val= input("valore: ")
        if val == "":
            finito=True
        else:
            val=int(val)
            f_list.append(val)


def main():
    mylist=[1,2,3]
    mylist=readlist(mylist)
    printlist(mylist)
    readlist(mylist)

    return

main()
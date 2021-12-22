#scrivere e testare una funzione che cerca il primo elemento
#in una lista maggiore di una certa soglia th

def searchgrt(f_list,th):

   # for (i,item) in enumerate(f_list):
   #     if item > th:
   #         pos=i
   trovato=False
   i=0
   pos=-1
   while (not trovato) and i<len(f_list):
       if f_list[i] > th:
           pos=i
           trovato= True
       else:
           i=i+1
           if not trovato:
               print("no values grater than",th)
    return pos

def main():
    th=9
    mylist=[2,2,2,2,2,7,2]
    p=searchgrt(mylist,th)
    print("primo elemento magigore di:" th,"=",searchgrt(p))
    #print("primo elemento magigore di:" th,"=",mylist(searchgrt(mylist,th))
    return

main()
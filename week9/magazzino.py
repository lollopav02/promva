def drop(f_shelf,f_n_obj,f_max_obj):
    finito=False
    i=len(f_shelf)-1
    j=0
    while f_n_obj>0 and not finito:
        #deposito oggetti
        slots_available=f_max_obj-f_shelf[i][j]
        obj_dropped=min(slots_available,f_n_obj)
        f_shelf[i][j]+=obj_dropped
        f_n_obj-=obj_dropped
        #aggiornamento i,j
        j+=1
        if j>len(f_shelf[0])-1:
            j=0
            i-=1
            if i<0:
                finito=True
    return f_n_obj

def take(f_shelf,f_n_obj):
    i=0
    j=0
    finito=False
    while f_n_obj>0 and not finito:
        obj_available=f_shelf[i][j]
        obj_taken=min(obj_available,f_n_obj)
        f_shelf[i][j]-=obj_taken
        f_n_obj -= obj_taken
        i+=1
        if i>len(f_shelf)-1:
            i=0
            j+=1
            if j>len(f_shelf[0])-1:
                finito=True

    return f_n_obj

def main():
    shelf=[
        [0, 0, 0],
        [3, 7, 9],
        [9, 9, 9]
    ]
    max_obj=9
    termina=False
    avanzo=0
    while not termina:
        action=input("Dx per depositare x obj,Px per prelevare x obj,x intero, nl= end:  ")
        if action.upper()=="":
            termina=True
        elif action[0].upper()=="D":
            n_obj=int(action[1:])
            avanzo=drop(shelf,n_obj,max_obj)
        elif action[0].upper()=="P":
            n_obj= int(action[1:])
            avanzo=take(shelf,n_obj)
            #take(shelf,n_obj)

        else:
            print("azione non riconosciuta")
        #stampa shelf
        for i in range(len(shelf)):
            print(shelf[i])
        print("oggetti in avanzo:",avanzo)




    return


main()
"""
Spesso i valori raccolti durante un esperimento vanno corretti, per togliere parte del
rumore di misura. Un approccio semplice a questo problema prevede di sostituire, in
una lista, ciascun valore con la media tra il valore stesso e i due valori adiacenti (o un
unico adiacente se il valore in esame si trova a una delle due estremità della lista).
Realizzate un programma che svolga tale operazione, senza creare un’altra lista.

"""
#lista viene acquisita da tastiera finchè l'utente non inserisce la stringa vuota

def buildlist(lista):
    full=1 #0 se la lista è vuota
    var=input("inserire misura: ")
    #todo handle empty list
    while(var !=""):
        lista.append(float(var))
        var=input("inserire misura: ")

    if len(lista)<2:
        print("errore:lista vuota")
        full=0
    return full

def computeaverages(lista):
    left=lista[0]
    #calcolo primo elemento
    lista[0]=(lista[0]+len(lista)-1)/2
    lista[-1] = lista[0]
    #calcolo elementi centrali
    for i in range(1,len(lista)-1):
        cur=lista[i]#salvo valore corrente
        #modifico elemento
        lista[i]=(left+lista[i]+lista[i+1])/3
        left=cur
    #modifico ultimo elemento
    lista[-1]=(lista[-1]+left)/2

    return

def main():
    misure=[]
    full=0 #inizialmente lista vuota

    while full== 0:
        full=buildlist(misure)

    print("lista misure: ")
    print(misure)
    computeaverages(misure)
    print("lista aggiornata: ")
    print(misure)

#run
main()
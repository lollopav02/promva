"""
Scrivete un programma che gestisca un menù che chieda all’utente di scegliere un
posto, un prezzo o l’uscita dal programma. Contrassegnate con un prezzo uguale a 0 i
posti già venduti. Quando l’utente specifica un posto, accertatevi che sia libero e che
le coordinate siano all’interno della tabella. Quando, invece, specifica un prezzo,
assegnategli un posto qualsiasi tra quelli disponibili a quel prezzo.
"""


teatro=[
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,10,10,10,10,10,10,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [10,10,20,20,20,20,20,20,10,10],
    [20,20,30,30,40,40,30,30,20,20],
    [20,30,30,40,50,50,40,30,30,20],
    [30,40,50,50,50,50,50,50,40,30],
]

def display_map(teatro):
    #visualizza la mappa dei posti
    for i in range(len(teatro)):
        for j in range(len(teatro[i])):
            print(f"{teatro[i][j]:3}", end="")
        print()

def main():
    #leggi la scelta dell'utente
    display_map(teatro)
    print("********************************")
    scelta = input("MENU'= (s)=prendi un posto;(p)=scegli un prezzo;(x)=esci  :").lower()
    while scelta != "x":
    #Gestire una selezione del posto in base alla posizione del sedile.
        if scelta=="s":
            riga=int(input("scegli la riga: "))
            colonna=int(input("scegli la colonna: "))
            #verifica che il posto è ancora disponibile
            if 0<=riga<=len(teatro) and 0<=colonna<=len(teatro) and teatro[riga][colonna]!=0:
                print("venduto, per %d dollari%",teatro[riga][colonna])
                teatro[riga][colonna]=0
            else:
                print("spiacenti, ma il posto non è disponibile")
        elif scelta== "p":
            prezzo=float(input("quanto vuoi spendere? "))
            trovato=False
            #ricerca per un posto con il prezzo desiderato
            for riga in range(len(teatro)):
                for colonna in range(len(teatro[riga])):
                    if teatro[riga][colonna]==prezzo and not trovato:
                        print("hai il posto in (%d,%d)."%(riga,colonna))
                        teatro[riga][colonna]=0
                        trovato=True
            if not trovato:
                print("spiacenti,nessun ticket disponibile a quel prezzo ")
        else:
            print("non è un opzione valida ")

        #leggi la prossima scelta
        display_map(teatro)
        scelta = input("MENU'= (s)=prendi un posto;(p)=scegli un prezzo;(x)=esci  :").lower()

main()
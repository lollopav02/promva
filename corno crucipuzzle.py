#risoluzone esercizio crucipuzzle

def main():
    griglia=leggi_griglia() #inserimento dati da parte dell'utente
   # print(griglia)
    stampa_griglia(griglia)
    parola=input("parola: ")
    parola=parola.upper()
    while parola != " ":
        trovata=cerca_parola(parola,griglia)
        if trovata:
            print("trovata")
        else:
            print("parola non esistente")

        parola = input("parola: ")
        parola=parola.upper()


def leggi_griglia():
    """
    chiede all' utente di inserier una gliglia di lettere una riga per volta
    terminando con una riga vuota.
    una tabella (lista di liste) le cui celle contengono le singole lettere inserite
    :return:
    """
 #griglia:[
   # ["X","Y","Z"],
   # ["A","B","C"]
   # ]
    #"stub"
    return [['E', 'B', 'C', 'D', 'E'], ['F', 'D', 'R', 'I', 'J'], ['K', 'O', 'O', 'N', 'O'], ['T', 'Q', 'R', 'L', 'T']]

    griglia=[]

    lettere=input("inserisci riga: ")  #"XYZ"
    lettere=lettere.upper()

    while lettere !="":
        #riga=lista fatta dai singoli caratteri di "lettere",es:["X","Y","Z"]
       # riga=[]
       # for ch in lettere:            # metodo 1
       #     riga.append(ch)
        #riga=[ch for ch in lettere]   #metodo 2
        riga=list(lettere)             #spacchettare una stringa in una lista

        griglia.append(riga) #[ ], appendo ["X","Y","Z"]-> [ ["X","Y","Z"] ]
        lettere = input("inserisci riga: ")  # "XYZ"
        lettere = lettere.upper()

    #TODO:CONTROLLA CHE LE COLONNE ABBIANO TUTTE LA STESSA LUNGHEZZA
    return griglia


def cerca_parola(parola,griglia):
    """
    analiiza la griglia e stabilisce se la parola ricevuta nella griglia,
    muovendosi nelle 8 direzioni possibili.

    :param parola: parola da ricercare
    :param griglia: tabella contenente le lettere del crucipuzzle
    :return: True se la parola è stata trovata,False se non è presente
    """
    #cerca tutte le caselle in cui c'è la lettera iniziale

    for r in range(len(griglia)):
        for c in range(len(griglia[0])):
            if griglia[r][c]== parola[0]:
                #ho trovato una lettera iniziale...verifico se la parola prosegue
                print(f"ho trovato una {parola[0]} nella posizione {r},{c}")
                if parola_prosegue(parola,griglia,r,c):
                    return True

    return False

def parola_prosegue(parola,griglia,r,c):
    n_righe=len(griglia)
    n_colonne=len(griglia[0])
#cerca verso *destra*
    i=0 # indice parola
    r1,c1=r,c #posizione di partenza della griglia
    #r1=r
    #c1=c
    while i<len(parola) and c1<n_colonne and parola[i]==griglia[r1][c1]:
        i=i+1
        c1=c1+1 #sposta a destra
    if i==len(parola):
        return True
#cerco verso *sinistra*
    i=0
    r1,c1 = r,c
    while i<len(parola) and c1>=0 and parola[i]==griglia[r1][c1]:
        i=i+1
        c1=c1-1 #sposta a sinistra
    if i==len(parola):
        return True
# cerco verso *alto*
    i=0
    r1, c1 = r, c
    while i < len(parola) and r1 >= 0 and parola[i] == griglia[r1][c1]:
        i = i + 1
        r1 = r1 - 1  # sposta in alto
    if i == len(parola):
        return True
# cerco verso *basso*
    i=0
    r1, c1 = r, c
    while i < len(parola) and r1<n_righe and parola[i] == griglia[r1][c1]:
        i = i + 1
        r1 = r1 +1  # sposta in basso
    if i == len(parola):
        return True
# cerco verso *alto+destra*
    i=0
    r1, c1 = r, c
    while i < len(parola) and r1>=0 and c1<n_colonne and parola[i] == griglia[r1][c1]:
        i = i + 1
        r1 = r1 - 1  # sposta in basso
        c1=c1+1
    if i == len(parola):
        return True
# cerco verso *alto+sinistra*
    i=0
    r1=r
    c1=c
    while i<len(parola) and r1>=0 and c1>=0 and parola[i]==griglia[r1][c1]:
        i = i + 1
        r1 = r1 - 1  # sposta in basso
        c1=c1 - 1
        if i==len(parola):
            return True
# cerco verso *basso-destra*
        i=0
        r1, c1 = r, c
        while i < len(parola) and r1<n_righe and c1 < n_colonne and parola[i] == griglia[r1][c1]:
            i = i + 1
            r1 = r1 + 1  # sposta in basso
            c1 = c1 + 1
        if i == len(parola):
            return True
# cerco verso *basso-sinistra*
        i=0
        r1, c1 = r, c
        while i < len(parola) and r1<n_righe and c1>=0 and parola[i] == griglia[r1][c1]:
            i = i + 1
            r1 = r1 + 1  # sposta in basso
            c1 = c1 - 1
        if i == len(parola):
            return True
    return False

def stampa_griglia(griglia):
   # for r in range(len(griglia)): #numero di righe
   #     for c in range(len(griglia[0])): #numero di colonne
   #         print(griglia[r][c],end=" ")
   #     print()

    for riga in griglia: #a ciascuna iterazione "riga" è la ista che corrisponde agli elementi:
        for ch in riga:  #ch sono gli elementi della lista interna(cioè le colonne)
            print(ch,end="")
        print()

    pass

main()
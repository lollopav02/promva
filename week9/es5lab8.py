"""
Scrivete un programma che giochi a tic-tac-toe (in italiano, tris o schiera). Il tic-tactoe si gioca su una scacchiera 3 × 3, come quella qui raffigurata, da due giocatori
che, a turno, posizionano in una casella libera il proprio simbolo (una croce per il
primo giocatore e un cerchio per il secondo). Il giocatore che compone una schiera di
tre propri simboli su una riga, una colonna o una diagonale, vince la partita. Il
programma deve disegnare la scacchiera, chiedere all’utente le coordinate del suo
prossimo simbolo, cambiare il giocatore di turno dopo ogni mossa e decretare il
vincitore
"""

def main():
    griglia=crea_griglia()
    print(griglia)
    finito=False
    giocatore1=False
    turni=0
    while not finito and turni<9:
        if giocatore1:
            print("giocatore 1(X)")
            simbolo="X"
        else:
            print("Giocatore 2 (O)")
            simbolo="O"
        stampa_griglia(griglia)

 # formato di ingresso: 23  (riga e colonna senza separatori, valori 1, 2, 3)
        #  11 12 13
        #  21 22 23
        #  31 32 33

        mossa=input("inserisci la tua mossa(rc): ")
        r=int(mossa[0])-1
        c=int(mossa[1])-1

        if griglia[r][c]==" ":
            #mossa lecita,eseguila
            griglia[r][c]=simbolo
            if vittoria2(griglia,simbolo):
                print("hai vinto!")
                finito=True
        else:
            print("Mossa non permessa-partita interrotta")
            finito=True

        turni=turni+1
        giocatore1=not giocatore1

    if turni==9 and finito==False:
        print("pareggio")



def crea_griglia():
    g=[]
    for riga in range(3):
        g.append([" "]*3)

    return g

def stampa_griglia(griglia):
    for riga in griglia:
        print(" | ".join(riga))
        print("-"*9)


def vittoria(griglia, simbolo):
    if griglia[0][0] == simbolo and griglia[0][1] == simbolo and griglia[0][2] == simbolo:
        return True
    elif griglia[1][0] == simbolo and griglia[1][1] == simbolo and griglia[1][2] == simbolo:
        return True
    elif griglia[2][0] == simbolo and griglia[2][1] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][0] == simbolo and griglia[1][0] == simbolo and griglia[2][0] == simbolo:
        return True
    elif griglia[0][1] == simbolo and griglia[1][1] == simbolo and griglia[2][1] == simbolo:
        return True
    elif griglia[0][2] == simbolo and griglia[1][2] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][0] == simbolo and griglia[1][1] == simbolo and griglia[2][2] == simbolo:
        return True
    elif griglia[0][2] == simbolo and griglia[1][1] == simbolo and griglia[2][0] == simbolo:
        return True
    else:
        return False

def vittoria2(griglia, simbolo,):
    trovato=False
#cerca per righe
    for riga in range(3):
        ok=True
        for col in range(3):
            if griglia[riga][col] != simbolo:
                ok=False
        if ok:
            trovato=False
#cerca per colonne
    for col in range(3):
        if griglia[riga][col]!= simbolo:
            ok=False
        if ok:
            trovato=True
#cerca diagonale principale

    diag_ok=True
    for r in range(3):
        if griglia[r][r] != simbolo:
            diag_ok=False
    if diag_ok:
        trovato=True
#cerca diagonale inversa
    diag_ok=True
    for r in range(3):
        if griglia[r][2-r] != simbolo:
            diag_ok=False

    if diag_ok:
        trovato=False

    return trovato


main()
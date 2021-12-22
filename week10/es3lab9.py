"""
Nei lunghi viaggi in auto, per ingannare il tempo, si può fare il gioco delle “parole
concatenate”. Il primo giocatore dice una parola iniziale, poi a turno ciascun
giocatore dovrà dire una nuova parola (ossia mai detta prima) la cui sillaba iniziale
sia uguale alla sillaba finale della parola precedente. (NOTA: Per semplicità,
ipotizziamo che tutte le sillabe siano lunghe esattamente 2 caratteri, quindi per “figli”
la ‘sillaba’ finale sarà “li” e non “gli”).
Ad esempio: gatto - torino - notte - tela - lana …
Scrivere un programma per permettere di gestire una o più partite del gioco.
Ciascuna partita termina quando un giocatore inserisce una parola già detta nella
stessa partita, quando inserisce una parola non correttamente concatenata, oppure
quando non riesce a proseguire (per abbandonare, inserisce *).
"""

def partita():
    words=[]
    ultima=input("inserire la parola iniziale: ").strip().lower()
    gioco_valido=True
    while gioco_valido:
        nuova=input("inserisci la parola: ").strip().lower()
        if nuova=="*":
            print("hai abbandonato")
            gioco_valido=False
        elif len(nuova)<2 or ultima[-2:] != nuova[0:2]:
            print("gioco non valido")
            gioco_valido=False
        elif nuova in words:
            print('Repeated word!')
            gioco_valido = False
        else:
            ultima=nuova
            words.append(nuova)



def main():
    stop=False
    while not stop:
        partita()
        yn=input("continuare? (y/n): ")
        if yn.strip().lower().startswith("n"):
            stop=True

main()
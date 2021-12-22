"""
Cifrario di Playfair. Un diverso modo per impedire la decifrazione di un testo
mediante la semplice analisi delle frequenze delle singole lettere consiste nel cifrare
insieme coppie di lettere e un semplice schema per farlo è il cifrario di Playfair. Si
sceglie una parola chiave e vi si eliminano le lettere duplicate, poi la si inserisce,
seguita ordinatamente dalle altre lettere dell’alfabeto inglese (non presenti dunque
nella parola chiave), in una scacchiera 5 × 5 (dato che ci sono soltanto 25 caselle e
l’alfabeto inglese ha 26 lettere, la I e la J sono considerate indistinguibili. Verificare
che nel testo sorgente le lettere siano pari, sennò aggiungere una “Z”).
Ecco lo schema che si ottiene usando PLAYFAIR come parola chiave:
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
Per cifrare una coppia di lettere, ad esempio AM, si cerca il rettangolo che ha A e M
negli angoli.
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
La codifica di questa coppia si ottiene prendendo gli altri due angoli del rettangolo,
in questo caso FH. Se le due lettere della coppia si trovano sulla stessa riga o sulla
stessa colonna, come GO, vengono semplicemente scambiate tra loro. La
decifrazione avviene nello stesso modo. Scrivete un programma che cifri o decifri un
file di testo secondo lo schema qui presentato.
"""

def genera_scacchiera():
    tastieraNoDupl=rimuovi_duplicati(tastiera)
    alpfabeto="abcdefghiklmnopqrstuvwxyz"
    #inserimento della scacchiera
    listalettere=tastieraNoDupl
    for c in alphabeto:
        listalettere.append(c)
    listalettere=rimuovi_duplicati(listalettere)
    #print(letterlist)
    scacchiera=[]
    for i in range(5):
        riga=[]
        for j in range(5):




def main():
    scacchiera=genera_scacchiera("lorenzo")
    print_scacchiera(scacchiera)
    ciphertext="questaeunaprovaz"
    testo_cifrato=cipher(scacchiera,ciphertext)
    print(testo_cifrato)
    testo_decifrato=cipher(scacchiera,testo_cifrato)
    print(testo_decifrato)

main()
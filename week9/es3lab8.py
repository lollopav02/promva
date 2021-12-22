"""
Quadrati magici. Una matrice n × n contenente i numeri interi 1, 2, 3, ..., n
2
è un
quadrato magico se la somma dei suoi elementi in ciascuna riga, in ciascuna colonna
e nelle due diagonali ha lo stesso valore. Ad esempio, questo è un quadrato magico di
dimensione 4:
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Scrivete un programma che acquisisca in ingresso 16 valori e verifichi se, dopo
averli disposti in una tabella 4 × 4 ordinatamente per righe, da sinistra a destra e
dall’alto in basso, formano un quadrato magico. Dovete verificare due proprietà:
1. Nei dati acquisiti sono presenti tutti e soli i numeri 1, 2, ..., 16?
2. Quando i numeri vengono disposti nella tabella, le somme delle righe, delle
colonne e delle diagonali sono tutte uguali l’una all’altra?
"""

quadrato=[
        [16,3,2,13],
        [5,10,11,8],
        [9,6,7,12],
        [4,15,14,1]
    ]

magico=True
# Verifica che ci siano tutti e soli i numeri tra 1 e 16
for num in range(1,17):
    numero_ok=False
# c'è il numero 'num' nella matrice?
# deve essere in almeno una riga
    for riga in quadrato:
        if num in riga:
            numero_ok=True
    if not numero_ok:
        magico=False

# Verifica la somma delle righe
somma=sum(quadrato[0]) # uso la prima riga come riferimento

for riga in quadrato:
    if sum(riga) != somma:
        magico=False

#verifica la somma delle colonne
for c in range(4): #c indice di colonna
    s=0            #somma elementi colonna c
    for r in range(4):
        s=s+quadrato[r][c]
    if s != somma:
        magico=False
#verifica diagonale discendente
s=0
for r in range(4):
    s=s+quadrato[r][r]
if s != somma:
    magico=False
#verifica diagonale ascendente
s=0
for r in range(4):
    s=s+quadrato[r][3-r]
if s != somma:
    magico= False

print(f"Quadrato magico {magico}")
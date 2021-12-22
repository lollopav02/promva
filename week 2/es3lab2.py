"""
Scrivere un programma che memorizzi una stringa in una variabile e, a partire da
quella variabile, visualizzi i primi tre caratteri della stringa, seguiti da tre punti,
ancora seguiti dagli ultimi tre caratteri.
Ad esempio, se la stringa viene inizializzata al valore “Mississippi”, il programma
deve visualizzare “Mis...ppi”
"""
#inizializzazione della stringa
stringa="Mississippii"
#visualizza
print(stringa[0:3],"...",stringa[9:12])#12+1
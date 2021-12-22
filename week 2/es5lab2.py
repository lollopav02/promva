"""
Scrivere un programma che memorizzi in due variabili costanti le lunghezze dei lati
di un rettangolo e visualizzi:
• L’area e il perimetro del rettangolo
• La lunghezza della sua diagonale
"""
from math import sqrt
#costanti lunghezza e larghezza
lunghezza=float(input("inserire lunghezza: "))
larghezza=float(input("inserire larghezza: "))
#calcoli
area=lunghezza*larghezza
perimetro=(lunghezza+larghezza)*2
diagonale=sqrt(lunghezza**2+larghezza**2)
print("l'area è: ",area)
print("il perimetro è:",perimetro)
print("la diagonale è: ",diagonale)

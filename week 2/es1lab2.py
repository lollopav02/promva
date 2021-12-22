"""
Scrivere un programma che memorizzi due numeri interi in due costanti definite nel
codice, e poi ne visualizzi:
• La somma
• La differenza
• Il prodotto
• Il valore medio
• La distanza (cioè il valore assoluto della differenza)
• Il valore massimo (cioè il maggiore tra i due)
• Il valore minimo (cioè il minore tra i due)
Suggerimento: utilizzare le funzioni max e min definite in Python. Esse accettano
una sequenza di valori separati da virgola in input e restituiscono rispettivamente il
valore massimo e minimo della sequenza. (Es: max(10, 5) restituisce 10)
"""
A=345
B=23

#calcoli
print("somma",A+B)
print("differenza",A-B)
print("prodotto",A*B)
print("valore medio",(A*B)/2)
print("distanza",abs(A-B))
print("massimo",max(A,B))
print("minimo",min(A,B))

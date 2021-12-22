"""
Lo pseudocodice seguente descrive come, in una libreria, viene calcolato l’importo di
un ordine a partire dal costo totale dei libri ordinati e dal loro numero.
• Leggere il costo totale dei libri e il numero di libri.
• Calcolare le tasse (il 7.5 per cento del costo totale dei libri).
• Calcolare i costi di spedizione ($2 per ogni libro).
• Il prezzo totale dell’ordine è la somma del costo totale dei libri, delle tasse e
dei costi di spedizione.
• Visualizzare l’importo dell’ordine.
Scrivere un programma in Python che implementi questo pseudocodice. Il costo
totale dei libri e il numero di libri devono essere memorizzati in due variabili
costanti.
"""
#definire le costanti
TASSE=0.075
COSTI_SPEDIZIONE=2
#input
costo_libri=float(input("inserire costo totale dei libri: "))
numero_libri=int(input("inserire il numero libri: "))
#calcoli
tassetot=costo_libri*TASSE
spedizionetot=numero_libri*COSTI_SPEDIZIONE
costotot=costo_libri+tassetot+spedizionetot
#visualizza l'importo totale
print("il costo totale dell'ordine è:$%.2f"%costotot)

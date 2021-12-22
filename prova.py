#leggere dei valore ed inserirli nella lista (interi)

valori=[]


dato=input("dato: ")
while dato !="":
    try:
        d=int(dato)
        valori.append(d)
        dato = input("dato: ")
    except ValueError as errore:
    #arriva qui se una delle istruzioni del blocco precedente ha generato
    #un eccezione del tipo ValueError
        print(f"il valore {dato} non è un numero correttamente formattato, riprova")
        print("messaggio errore: ",errore)

    dato = input("re-inserisci il dato: ")



print(valori)


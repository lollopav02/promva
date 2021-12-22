prezzoArticolo=float(input("inserire prezzo:"))
sconto=(prezzoArticolo/100)*8
prezzoScontato=prezzoArticolo-sconto

if prezzoArticolo>128:
    print(prezzoScontato)
else:
    print("fa schifo")


    #se pari e maggiore di 10:stampa categoria A
    #se dispari e minore di 10:stampa categoria B
    #altrimenti categoria C
    x=12
    if x%2==0:
        if x>10:
            print("categoria a")
            #cateogria c:
        else:
            print("cateogira c")
    else:
        if x<10:
            print("categoria b")
        else:
            print("categoria c")


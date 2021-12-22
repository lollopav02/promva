"""
Un supermercato vuole ricompensare il proprio miglior cliente del giorno,
mostrandone il nome su uno schermo all’interno del negozio. A questo scopo,
vengono memorizzati in una lista (customers) i nomi di tutti i clienti del giorno e, in
un’altra lista (sales), il corrispondente importo della spesa effettuata.
Scrivete la funzione nameOfBestCustomer(sales, customers) che restituisca il
nome del cliente che ha speso la cifra più alta.
Poi, scrivete un programma che chieda al cassiere di digitare tutti gli importi spesi e i
nomi dei relativi clienti, aggiungendoli via via a due liste distinte, per poi invocare la
funzione che avete progettato e visualizzare il risultato. Usate il prezzo 0 come
sentinella
"""
#TODO: Note: nella consegna, la frase “Usate il prezzo 0 come sentinella”,
# vuol dire che il ciclo che si occupa dell’input dei nomi dei clienti
# e del prezzo della spesa continuerà a richiedere nome e prezzo finchè
# non verrà inserito il prezzo = a 0. Per questo motivo il nome e il prezzo
# vengono “appesi” alle due liste se, e solo se, il prezzo è != (diverso) da 0.

def main():
    customers = []
    sale=[]
    prezzo=1
    while prezzo != 0:
        nome=input("Nomi clienti del giorno: ")
        while nome == "" or nome== " ":
            nome =input("Nomi clienti del giorno: ")
        prezzo=int(input("inserire prezzo: "))
        while prezzo <=0:
            prezzo=int(input("inserire prezzo: "))
        if prezzo !=0:
            customers.append(nome)
            sale.append(prezzo)
    prezzoMassimo = nameOfBestCustomer(customers, sale)
    for i in range(len(sale)):
        if sale[i]==prezzoMassimo:
            print("prezzo massimo :",sale[i],"cliente:",customers[i])

def nameOfBestCustomer(clienti,prezzo):
    limite=len(clienti)
    massimo=prezzo[0]
    i=1
    while i<limite:
        if prezzo[i]>massimo:
            massimo=prezzo[i]
        i +=1

    return massimo


main()


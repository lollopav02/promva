"""
Il responsabile amministrativo di un albergo registra le vendite in un file di testo.
Ogni riga contiene le seguenti 4 informazioni, separate da caratteri “punto e virgola”:
il nome del cliente, il servizio venduto (ad esempio, cena, conferenza, alloggio, e
così via), l’importo pagato e la data dell’evento. Scrivete un programma che legga un
tale file di testo e visualizzi l’importo totale relativo a ciascun tipo di servizio,
segnalando un errore se il file non esiste oppure se il suo formato non è corretto
(verificando cioè che ci siano 4 campi per riga e che il prezzo sia float).

"""
filename=input("inserire nome file da visualizzare: ")
#apri il file
try:
    vendite=open(filename,"r",encoding="utf-8")
except IOError:
    exit("il file non puà essere aperto")
#leggi le righe,aggiungendo nuove categorie come sono state trovate e
#mantenere il totale
categorie=[]
totale=[]
for line in vendite:
#verifica che la linea ha i numeri richiesti di item
    parti=line.strip(",")
    if len(parti) !=4:
         exit("c'e una linea invalida nel file")
    #verifica che il costo è un numero valido
    try:
        costo=float(parti[2])
    except ValueError:
        exit("c'e una linea invalida nel file")
    #se esiste la categoria allora aggiungere il totale,altrimenti
    #aggiungi un altra categoria
    if parti[1] in categorie:
        indice=categorie.index([parti[1]])
        totale[indice]=totale[indice]+costo
    else:
        categorie.append(parti[1])
        totale.append(costo)

filename.close()
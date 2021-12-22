"""
Scrivete un programma che chieda all’utente di fornire due stringhe, per poi
visualizzare (evitando ripetizioni di caratteri nella stampa):
• i caratteri che compaiono in entrambe le stringhe;
• i caratteri che compaiono in una stringa ma non nell’altra;
• le lettere che non compaiono in nessuna delle due stringhe.
Suggerimento: trasformare una stringa in un insieme di caratteri.

"""
stringa1=input("inserire prima stringa: ").lower()
stringa2=input("inserire seconda stringa: ").lower()
insieme1=set(stringa1)
insieme2=set(stringa2)
print("INSIEME 1:",insieme1)
print("INSIEME 2:",insieme2)

print("****CARATTERI COMUNI****")
caratteri_comuni=insieme1.intersection(insieme2)
print(caratteri_comuni)

print("***CARATTERI NON COMUNI****")
caratteri_non_comuni=insieme1.symmetric_difference(insieme2)
if caratteri_non_comuni==insieme2 or insieme1:
    print("insiemi uguali")
else:
    print(caratteri_non_comuni)

alfabeto="acdefghilmnopqrstujkyz"
ins_alf=set(alfabeto)

print("****LETTERE NON PRESENTI IN NESSUNA DELLE DUE LISTE****")
caratteri_mancanti=ins_alf.difference(caratteri_comuni)
print(caratteri_mancanti)
#operazione su insiemi

col_set1={"red","green","blue"}
col_set2={"red","green"}
col_set3={"red","orange","yellow"}

#ricerca
col=input("colore: ")
if col in col_set1:
    print(col,"in set 1")
else:
    print("colore non presente in set 1")
    col_set1.add(col)
print(col_set1)

col_set1.add(col)
print(col_set1)

#eliminare un elemento
col_set1.discard(col)
print(col_set1)
col_set1.discard(col)
print(col_set1)
#col_set1.remove(col) remove dà errore se l'elemento non è presente nell'insieme
print(col_set1)
if col in col_set1:
    col_set1.remove(col)
else:
    print(col,"not in set")

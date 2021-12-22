#operazioni tra insiemi
col_set1={"red","green","blue"}
col_set2={"red","green"}
col_set3={"red","orange","yellow"}

#unione
print("*UNIONE*")
print(col_set1.union(col_set2))
print(col_set1.union(col_set3))
col_set4=col_set1.union(col_set3)
print(col_set4)
col_set4=col_set3.union(col_set1)


#intersezione
print("*INTERSEZIONE*")
col_set5=col_set1.intersection(col_set3)
print(col_set5)
col_set5=col_set3.intersection(col_set1)
print(col_set5)

#differenza
col_set6=col_set1.difference(col_set3)
print(col_set6)
col_set6=col_set1.difference(col_set1)
print(col_set6)

#contenimento
if col_set2.issubset(col_set1):
    print("set2 contenuto in set1")
else:
    print("set2 non contenuto in set2")

if col_set2.issubset(col_set2):
    print("set1 contenuto in set2")
else:
    print("set1 non contenuto in set2")

#conteggio elementi
num_item_set1=len(col_set1)
num_item_set2=len(col_set2)
print(num_item_set2)

#comparazione
if col_set1==col_set3:
    print("set1==set3")
else:
    print("set1 != set3 ")

if col_set2==col_set2.intersection(col_set2):
    print("set2 contenuto in set1")
else:
    print("set2 non contenuto in set1 ")
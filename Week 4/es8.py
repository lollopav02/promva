#ricerca del minimo(o massimo) tra un serie di valori introdotti  da tastiera(NL per terminare)
val=int(input("inserire valore: "))
max=val
finito= False
while not finito:
if val=="":
    finito=True
else:
    val=int(val)
    if val> max:
        max=int(val)

print("valore massimo:",max)


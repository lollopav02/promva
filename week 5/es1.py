#sequenza di interi (nl per terminare) e stampare a video la massima differnza tra due interi adiacenti
delta_max=-1
delta=0

if prev=="":
    finito=True
else:
    finito=False
    prev=int(prev)

while not finito:
    current=input("valore: ")
    if current=="":
        finito=True
    else:
        current=int(current)
        delta=abs(current-prev)
    if delta>delta_max:
       delta_max=delta
       prev=current
print("delta max: ",delta_max)

DISCOUNTRATE_LOW = 0.08
DISCOUNTRATE_HIGH = 0.16
DISCOUNTRATE_THR = 128

prezzo = float(input("prezzo: "))
if prezzo >= DISCOUNTRATE_THR:
    prezzo = prezzo * (1 - DISCOUNTRATE_HIGH)
else:
    prezzo = prezzo * (1 - DISCOUNTRATE_LOW)
print(prezzo)

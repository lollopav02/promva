#letta sequenza di numeri interi verifcare che che la seq sia monotona
#mono strettamente crescente
mono=True
prev=int(input("valore: "))
finito=False

while (not finito) and mono:
  current=int(input("valore: "))
  if current== "":
      finito=True
  else:

      current=int(current)
      if current<=prev:
          mono= False
          finito=False
      prev=current
if mono:
    print("mono")
else:
    print("no mono")

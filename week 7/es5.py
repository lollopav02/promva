#lettura di una lista di interi, nl per terminare

mylist=[]

finito=False
while not finito:
  val=input("valore: ")
  if val== " ":
      finito=True
  else:
      mylist[i]=int(val)
      i += 1

print(mylist)

#inserimento valore
mylist.insert(1,-2)
print(mylist)

#estrazione valore
mylist.pop(1)
print(mylist)

pos=mylist.index(8)
val=8
pos=-1
if val in mylist:
    pos=mylist.index(val)
else:
    print("not trovato ")

#rimuovi per valore

val=9

if val in mylist:
    mylist.remove(val)
    print(mylist)



"""
Scrivete un programma che inizializzi una lista con dieci numeri interi casuali tra 1 e
100 e, poi, visualizzi quattro righe di informazioni, contenenti:
a. Tutti gli elementi di indice pari.
b. Tutti gli elementi di valore pari.
c. Tutti gli elementi in ordine inverso.
d. Il primo e l’ultimo elemento.
"""
from random import randint

#stampa numeri casuali
num_max=100
max=10
list=[]
for i in range(0,max):
    list.append(randint(1,num_max))
print("lista random:",list)

#stampa numeri indice pari
print("numeri con indice pari presenti in lista:",end=" ")
print()
for i in range(0,len(list),2):
    print(list[i],end=" ")
print()

#stampa numeri pari
print("lista numeri pari:",end="")
print()
for i in range(0,len(list)):
    if list[i]%2==0:
        print(list[i],end="")
print()
#stampa lista in ordine inverso
print("lista in reverse",end="")
print()
for i in range(len(list)-1,-1,-1):
    print(list[i],end=" ")
print()
#for i in range(len(list)):
#    reversed(list)

#il primo ed ultimo elemento
print("primo e ultimo elemento della della lista: ",end="")
print()
print(list[0],list[9])

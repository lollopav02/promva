"""
Scrivere un programma che memorizzi in una costante un numero intero positivo di
cinque cifre (quindi compreso tra 10000 e 99999), e visualizzi le singole cifre di cui
è composto.
Ad esempio, avendo il numero 16384, il programma deve visualizzare, su righe
separate: 1 6 3 8 4.
"""
#num=16384
num=input("inserire un numero intero di cinque cifre: ")
cost=str(num)

print(cost[0])
print(cost[1])
print(cost[2])
print(cost[3])
print(cost[4])


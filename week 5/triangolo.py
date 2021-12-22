h=int(input("altezza: "))

for i in range(0,h):
    #stampa i-th row
    for j in range(0,h-1-i):
        print(" ",end="")
    for j in range(0,2*i+1):
        print("*",end="")


print()

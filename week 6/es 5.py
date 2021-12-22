# leggere intero fino a che positivo

def readTillpos():

    while negativo:
        n=int(input("valore: "))
        if n>0:
            negativo= False
            return n

def main():
    print("Introduci intero positivo: ")
    val= readTillpos()
    print(val)


    return

main()
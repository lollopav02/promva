# leggere intero fino a che positivo

def readTillPos():
    negativo = True
    while negativo:
        n = int(input("valore: "))
        if n >= 0:
            negativo = False
    return n

def main():
    print("Introduci intero positivo: ")
    val = readTillPos()
    print(val)
    return

main()

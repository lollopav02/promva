frase=input("inserire frase""\n")
if frase.isalpha():
    print("contiene soltanto lettere")
elif frase.isdigit():
    print("contiene solo lettere maiuscole")
elif frase.isalpha() and frase.isupper():
    print("contiene solo lettere minuscole")
elif frase.isalnum() and frase.islower():
    print("contiene soltanto cifre")
elif frase.isalnum():
    print("contiene soltanto lettere o cifre")
elif frase[0].isupper():
    print("inizia con lettera maiuscola")
    if frase[0].isupper():
        print("inizia con una lettera maiuscola")
else:
    print("errore")
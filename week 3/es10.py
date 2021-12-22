coordinata = input('inserisci coordinata LetteraNumero: ')
#print(coordinata)

lettera = coordinata[0]
pos_lettera = ord(lettera) - ord('a')
#print(pos_lettera)
numero = int(coordinata[1])

#if numero%2 == 0:
#    print('PARI')
#else:
#    print('DISPARI')

if lettera %2 == 0:
    if numero %2 == 0:
        print('W')
    else:
        print('B')
else:
    if numero % 2 == 0:
        print('B')
    else:
        print('W')
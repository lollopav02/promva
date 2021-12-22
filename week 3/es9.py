#se pari e maggiore di 10: stampa categoria A
#se dispari e minore di 10: stampa categoria B
#altrimenti categoria C

x = 12

if x%2 == 0:
    if x > 10:
        print('CATEGORIA A')
    else:
        print('CATEGORIA C')
else:
    if x < 10:
        print('CATEGORIA B')
    else:
        print('CATEGORIA C')
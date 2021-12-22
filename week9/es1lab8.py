"""
Scrivete la funzione merge(a, b) che “fonde” due liste, alternando un elemento
della prima e un elemento della seconda. Se una lista è più corta dell’altra, gli
elementi vengono alternati fin quando è possibile, poi gli elementi rimasti nella lista
più lunga vengono aggiunti ordinatamente in fondo. Le liste di partenza non devono
essere modificate. Se, ad esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è
9 7 4 9 11, l’invocazione di merge(a, b) restituisce una nuova lista contenente i
valori 1 9 4 7 9 4 16 9 11.
"""
"""
table=[[0]*4]*5
for r in table:
    print(r)
for r in  range(len(table)):
    for c in range(len(table[0])):
        print(table[r][c])
"""

def merge(a,b):
    """
    :param a: la prima lista da cui prendere gli elementi
    :param b: la seconda lista da cui prendere gli elementi
    :return: la lista mischiata
    """
    s=[]
    #unire gli elementi da entrambe le liste fin quando ci sono elementi in entrambe

    lista_piu_corta=min(len(a),len(b))
    for i in range(lista_piu_corta):
        s.append(a[i])
        s.append(b[i])
#itera fin quando una delle due stringhe finisce gli elementi
#aggiungere gli elementi rimanenti
    for i in range(lista_piu_corta,len(a)):
        s.append(a[i])
    for i in range(lista_piu_corta,len(b)):
        s.append(b[i])
    return s


def main():
    a=[1,4,9,16]
    b=[9,7,4,9,11,8]
    ris=merge(a,b)
    print("risultato: ",ris)
    return

main()
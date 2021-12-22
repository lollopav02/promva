"""
Scrivete funzioni che risolvano i problemi seguenti per liste di numeri interi,
fornendo un programma di collaudo per ciascuna funzione.
a. Scambiare tra loro il primo e l’ultimo elemento della lista.
b. Far scorrere tutti gli elementi di una posizione “verso destra”, spostando
l’ultimo elemento nella prima posizione. Ad esempio, la lista 1 4 9 16 25
deve diventare 25 1 4 9 16.
c. Sostituire con 0 tutti gli elementi di valore pari.
d. Sostituire ciascun elemento, tranne il primo e l’ultimo, con il più grande dei
due elementi ad esso adiacenti. È possibile usare liste di appoggio.
e. Eliminare l’elemento centrale della lista se questa ha dimensione dispari,
altrimenti eliminare i due elementi centrali.
f. Spostare tutti gli elementi pari all’inizio della lista (lasciando quelli dispari in
coda), preservando però l’ordinamento relativo tra gli elementi.
g. Restituire il secondo valore maggiore della lista (senza pari meriti).
h. Restituire True se e solo se la lista è ordinata in senso crescente.
i. Restituire True se e solo se la lista contiene due elementi adiacenti duplicati.
j. Restituire True se e solo se la lista contiene elementi duplicati (non
necessariamente adiacenti).
"""
from random import randint

def main():
    random_list=[randint(1,20) for i in range(10)] #genera una lista di 10 numeri random
    print("lista: ",random_list)
#punto a
    data=list(random_list)
    swap_primo_ultimo(data)
    print("dopo aver scambiato il primo e l'ultimo numero: ",data)
#punto b
    data=list(random_list)
    sposta_destra(data)
    print("dopo aver fatto scorrere i numeri verso destra: ",data)
#punto c
    data=list(random_list)
    zero_pari(data)
    print("dopo aver sostituito i numeri pari con zero: ",data)
#punto d
    data=list(random_list)
    grandi_vicini(data)
    print("dopo aver sostituito i vicini,eccetto il primo numero e l'ultimo della lista: ",data)
#punto e
    data = list(random_list)
    centro_lista(data)
    print("dopo aver eliminato l'elemento centrale: ",data)
#punto f
    data = list(random_list)
    pari_inizio_lista(data)
    print("dopo aver messo gli elementi pari all'inizio preservando il loro ordine: ",data)
#punto g
    print("secondo elemento maggiore della lista: ",secondo_maggiore(random_list))
#punto h
    print("la lista è ordinata in senso crescente:",lista_crescente(random_list))
#punto i
    print("la lista contiene elementi adiacenti duplicati",duplicati_adiacenti(random_list))
#punto j
    print("la lista contiene elementi duplicativi: ",duplicati(random_list))

#a
def swap_primo_ultimo(random_list):
    """
    scambia il primo numero con l'ultimo della lista
    :param data(ho provato in questo caso con random_list: la lista da processare
    :return:
    """
    if len(random_list)<2:
        return
    else:
        (random_list[0],random_list[-1])=(random_list[-1],random_list[0])
    #data[0]=data[-1]
    #data[-1]=data[0]  ha usato una tupla
#b
def sposta_destra(data):
    """
    sposta gli elementi verso destra
    :param data:
    :return:
    """
    if len(data)==0:
        return
    ultimo=data[len(data)-1]
    #iterazione iniziando dall'ultimo elemento della lista e finendo al secondo
    for i in range(len(data)-1,0,-1):
        data[i]=data[i-1]
    data[0]=ultimo
#c
def zero_pari(data):
    """
    sostituisce 0 ad ogni numero pari
    :param data:
    :return:
    """
    for i in range(0,len(data)):
        if data[i]%2==0:
            data[i]=0
#d
def grandi_vicini(data):
    """
    rimpiazza ogni valore con il piu' grande dei suoi vicini
    :param data:
    :return:
    """
    vecchi_valori=data
    for i in range(1,len(data)-1):
        data[i]=max(vecchi_valori[i-1],vecchi_valori[i+1])

        #todo SOSTITUIRE CON DATA[DONE(NON CAMBIA UN CAZZO)]
#e
def centro_lista(data):
    """
    Eliminare l’elemento centrale della lista se questa ha dimensione dispari,
    altrimenti eliminare i due elementi centrali.
    :param data:
    :return:
    """
    if len(data)==0:
        return
    if len(data)%2==1:
        data.pop(len(data)//2)
    else:
        data.pop(len(data)//2)
        data.pop(len(data)//2)
#f
def pari_inizio_lista(data):
    """
    Spostare tutti gli elementi pari all’inizio della lista (lasciando quelli dispari in
    coda), preservando però l’ordinamento relativo tra gli elementi.
    :param data:
    :return:
    """
    pari_pos=0
    pos=0
    while pos<len(data):
        if data[pos]%2==0:
            temp=data.pop(pos)
            data.insert(pari_pos,temp)
            pari_pos += 1
        pos += 1
#g
def secondo_maggiore(data):
    """
     Restituire il secondo valore maggiore della lista (senza pari meriti).
    :param data:
    :return:
    """
    pari=[]
    dispari=[]
    for n in data:
        if n%2==0:
            pari.append(n)
        else:
            dispari.append(n)
    n=pari+dispari
#h
def lista_crescente(data):
    """
    Restituire True se e solo se la lista è ordinata in senso crescente.
    :param data:
    :return: True se è in ordine crescente, altrimenti falso
    """
    crescente=True
    for i in range(0,len(data)-1):
        if data[i]>data[i+1]:
            crescente=False
    return crescente
#i
def duplicati_adiacenti(data):
    """
    Restituire True se e solo se la lista contiene due elementi adiacenti duplicati.
    :param data:
    :return: True se la lista contiene duplicati adiacenti altrimenti falso
    """
    ha_duplicati=False
    for i in range(0,len(data)-1):
        if data[i]==data[i+1]:
            ha_duplicati=True

    return ha_duplicati

def duplicati(data):
    """
    Restituire True se e solo se la lista contiene elementi duplicati (non
    necessariamente adiacenti).
    :param data:
    :return: True se la lista ha duplicati,altrimenti False
    """
    ha_duplicati=False
    for i in range(0,len(data)-1):
        for j in range(i+1,len(data)):  #evita di comparare data[i] con se stesso
            if data[i]==data[j]:
                ha_duplicati=True
    return ha_duplicati



main()
#scrivere e testare una funzione che concatena gli elementi di
#una lista di stringhe, così da ottenere un unico testo_da_controllare.txt

def textconcat(f_list):
    t_string= ""
    for word in f_list:
        t_string += word
        #t_string=t_string+word+""
    return t_string

def main():
    text=""
    mylist=["Ciao","Franco","Ciao"]
    text=textconcat(mylist)
    print(text)
    return

main()

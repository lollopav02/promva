filename= "testo.txt"

fp_in=open(filename,"r",encoding="utf-8") #filename perche il file di testo_da_controllare.txt è dato a filename ed "r" per indicare solo la lettura
                                        #quel tipo di encoding perchè la "è" veniva convertita in una A
print(fp_in)
# lettura un carattere
car=fp_in.read(1)#il primo carattere letto viene dato a car
print(car)
car=fp_in.read(1)
print(car)
car=fp_in.read(3)
print(car)


#lettura di un intera riga
line=fp_in.readline().rstrip()
print(line)
line=fp_in.readline().strip()
print(line)


#lettura di tutte le righe
text_list=fp_in.readlines()
print(text_list)
print(text_list[2])
#lettura du tutti i caratteri
text=fp_in.read()
print(text)

fp_in.close()

fp_in=open(filename,"r",encoding="utf-8")
text=fp_in.read()
print(text)
fp_in.close()
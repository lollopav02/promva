#letto un testo_da_controllare.txt (termina con riga vuota,nl) stampare a video
#a video la frequenza delle parole inserite

import matplotlib.pyplot as plt

wordlist=[]
counterlist=[]
finito=False
while not finito:
    line=input()
    if line == "":
        finito= True
    else:
        line=line.split()
        for word in line:
            if word not in wordlist:
                wordlist.append(word)
                counterlist.append(1)
            else:
                pos=wordlist.index(word)
                counterlist[pos] +=1
print(wordlist)
print(counterlist)
plt.bar(wordlist,counterlist)
plt.show()
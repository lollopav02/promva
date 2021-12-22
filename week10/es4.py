#lettura di un file di testo_da_controllare.txt e stampa a video tutte le parole (by-row)

filename= "testo2.txt"
fp_in=open(filename,"r",encoding="utf-8")
line="start" # quello che vuoi
#metodo migliore
for line in fp_in:
    for word in line.split():
        print(word.strip(",;:.!?"))



#metodo peggiore
"""
while line != "":
    line=fp_in.readline().strip()
    wordlist=line.split()
    for word in wordlist:
        print(word.strip(",;:.!?"))
"""

fp_in.close()
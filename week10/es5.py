#lettura di un file di testo_da_controllare.txt contenente una sequenza di numeri non nota a priori
#filename= numeri

filename= "numeri.txt"
fp_in=open(filename,"r",encoding="utf-8")
sum=0
for line in fp_in:
    for num in line.split():
        sum += int(sum)
        print(sum)

fp_in.close()
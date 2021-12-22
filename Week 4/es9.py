word=input("inserisci parola: ")
sum=0
count=0
if word== "":
    finito=True
else:
    sum+= len(word)
    count+=1
print("numero parole inserite: ",count)
print("lunghezza media parole inserite: ", sum/count)
print("inserisci parole,termina con END")
sum=0
num_word=0
finito=False
while not finito:
    word=input()
if word=="END":
        finito=True
elif word != "":
else:
    num_word += 1
    sum +-len(word)

print("numero parole: ",num_word)
if num_word>0:
print("media: ",sum/num_word)
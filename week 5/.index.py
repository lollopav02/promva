word="franco"
car="a"
#for i in range(0;len(word)):
trovata=False
i=0
while i<len(word) and not trovata:
    if car==word[i]:
        trovata=True
 else:
     i+=1

if trovata:
     print(i)
else:
    print("non trovato")
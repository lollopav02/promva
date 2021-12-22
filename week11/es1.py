#spell check

#lettura vocabolario
voc_list=[]
fp_voc=open("voc.txt", "r")
for line in fp_voc:
    voc_list.append(line.strip())
fp_voc.close()

#lettura di un file di testo_da_controllare.txt
fp_text=open("testo.txt", "r")
for line in fp_text:
    for word in line.split():
        word=word.strip(",;.:?!").lower()
        if word not in voc_list:
            print("typo: ",word)

fp_text.close()
#dizionari dic()

student1=()
student2={# matricola -> nome STR-STR
    "29718":"franco",
    "29719":"Licia",
}

#stampa valore corrispondente ad una key
print(student2["29719"])
matricola="29718"
if "30128" in student2:
    print(student2[matricola])
else:
    print("no key")

shelf1={#merce ->conteggio STR-INT
    "banana":129,
    "pesca":0
}
key="banana"
print(shelf1[key])
shelf2={#barcode ->merce INT-STR
    10001:"banana",
    10100:"pesca",
 }

key=10001
print(shelf2[key])
print(shelf2[10100])

freq={#barcode -> merce INT-STR
    12:27,
    27:39,
}
print(freq[12])

dic1={
    "franco":"29789",
    27:"INFORMATICA",
    "franco":"12121"
}
print(dic1["franco"])
print(dic1[27])

dic2=dic1.copy() #copia di dic1 in dic2
dic2=dict(dic1) #copia di dic1 in dic2
#dic2=dic1 #no copia,solo alias
#rubrica
#dict nome->numCell

book={}
for i in range(2):
    name=input("nome: ")
    num=input("telefono: ")
    book[name]=num

print(book)

#scansione del dizionario per key
for key in book.keys():
    print(key,book[key])

print(book.keys())

listkeys=list(book.keys())#crea lista di keys
#for key in listkeys:
print(book.keys())

for value in book.values():
    print(value)

listValues=list(book.values()):

for key, val in book.items():
    print(key,val)
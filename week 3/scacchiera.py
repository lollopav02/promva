###inserire coordinate e leggere se la pos
# si trova in una casella nera o bianca
coordinata=(input("inserisci letteraNumero:"))
print(coordinata)
lettera=coordinata[0]
pos_lettera=ord(lettera)-ord("a")
print(pos_lettera)
numero=int(coordinata[1])
if numero%2==0:
    print("pari")
else:
    print("dispari")

if lettera%2==0:
    if numero%2==0:
        print("bianca")
    else:
        print("nera")
else:
    if numero%2==0:
        print("nera")
    else:
        print("bianca")
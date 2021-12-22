mese=int(input("inserire mese: "))
giorno=int(input("inserire giorno: "))
if mese==1 or mese==2 or mese==3:
   stagione=("inverno")
elif mese==4 or mese==5 or mese==6:
    stagione=("primavera")
elif mese== 7 or mese==8 or mese==9:
   stagione=("estate")
elif mese==10 or mese==11 or mese==12:
   stagione=("autunno")
else:
    print("errore")
if mese%3==0 and giorno>=21:
    if stagione=="inverno":
        stagione="primavera"
    if stagione=="primavera":
        stagione="estate"
    if stagione=="estate":
        stagione="autunno"
    else:
        print("inverno")
print(f"quel giorno è:",stagione)



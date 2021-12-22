voto=input("inserire un voto:")
if voto[0]=="A":
    ris=4.0
elif voto[0]=="B":
    ris=3.0
elif voto[0]=="C":
    ris=2.0
elif voto[0]=="D":
    ris=1.0
else:
    ris=0.

if len(voto)>1 and voto[0] !=" F":
    if voto[1]=="+" and voto[0] !="A":
        ris=ris+0.3
    elif voto[1]=="-":
            ris=ris-0.3

print(f"il voto corrispondente è {ris}")



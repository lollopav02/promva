#leggere due file con sequenza di interi per ciascuna riga
#creare un terzo file con la somma di ogni riga
#i due file hanno stesso #righe

fpin1=open("numeri1.txt", "r", encoding="utf-8")
fpin2=open("numeri2.txt", "r", encoding="utf-8")
fpsum=open("somma.txt", "w", encoding="utf-8")


for line1 in fpin1:
    num_list1=line1.split()
    line2=fpin1.readline()
    num_list2=line2.split()
    sum=0
    lineout=""
    for i, num1 in enumerate(num_list1):
        num2=num_list2[i]
        sum += int(num1)+int(num2)
        lineout +="+"+ num1+"+"+num2
    lineout= lineout.lstrip("+")
    print(lineout,"=",sum)
    fpsum.write(lineout+str(sum)+"\n")

fpin1.close()
fpin2.close()
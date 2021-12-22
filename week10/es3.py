#leggere il nome file e numero-> salvare numero+1 in nome file

file_name=input("nome file: ")
fp_out=open(file_name,"w",encoding="utf-8")
val=int(input("numero: "))
val += 1
fp_out.write(str(val))


fp_out.close()

#leggere dal file appena creato il numero e stampare a video il numero +1

fp_in=open(file_name,"r",encoding="utf-8")
line=fp_in.readline()

val=int(line)
val=+1
print(val)


fp_out.close()
# copia criptata di qun file di testo_da_controllare.txt

filename=input("inserire nome file: ")
fp_in=open(filename,"r",encoding="utf-8")
filename=filename.rstrip(".txt")
fp_out=open(filename+"_copy_enc.txt","w",encoding="utf-8")

for line in fp_in:
    for car in line:
        fp_out.write(str(ord(car)))




fp_in.close()
fp_out.close()

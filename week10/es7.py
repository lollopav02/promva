#copia incolla di un file di testo_da_controllare.txt il cui nome è fornito da tastiera

filename=input("inserire nome file: ")
fp_in=open(filename,"r",encoding="utf-8")

filename=filename.rstrip(".txt")

fp_out=open(filename+"_copy.txt","w",encoding="utf-8")

for line in fp_in:
    fp_out.write(line)



fp_in.close()
fp_out.close()
"""
Scrivete un programma che legga il file di testo_da_controllare.txt input.txt. Ogni riga letta va scritta nel
file output.txt preceduta dal numero di riga, inserita come commento tra caratteri /* e
*/. Se, ad esempio, il file input.txt fosse il seguente:
Enola Gay
è il bombardiere che il 6 agosto 1945,
sganciò su Hiroshima la prima bomba atomica
soprannominata Little Boy.
Il file output.txt generato sarebbe:
/*1*/Enola Gay
/*2*/è il bombardiere che il 6 agosto 1945,
/*3*/sganciò su Hiroshima la prima bomba atomica
/*4*/soprannominata Little Boy.
"""


fp_in=open("input.txt", "r", encoding="utf-8")
fp_out=open("output.txt", "w", encoding="utf-8")

i=1
for line in fp_in:
    fp_out.write(f"/*{i}*/{line}")
    i +=1

fp_in.close()
fp_out.close()

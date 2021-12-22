"""
Scrivete un programma che legga tutte le righe di un file di testo_da_controllare.txt (input.txt), ne
inverta l’ordine e le scriva in un altro file (output.txt). Ad esempio, se il file input.txt
contiene queste righe:
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.

allora il file output.txt conterrà:

The lamb was sure to go.
And everywhere that Mary went
Its fleece was white as snow
Mary had a little lamb
"""
#leggi il file di input


file_input=open("inputes2.txt", "r", encoding="utf-8")
#reggi le righe
righe=file_input.readlines()
file_output=open("outputes2.txt", "w", encoding="utf-8")

for i in range(len(righe)-1,-1,-1):
    file_output.write(righe[i])

#chiudi
file_input.close()
file_output.close()
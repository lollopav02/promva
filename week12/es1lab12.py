"""
A) Scrivete un programma che conti le occorrenze di ciascuna parola presente in un
file di testo_da_controllare.txt, il cui nome è inserito da tastiera. Si assuma che il file contenga solo
caratteri alfabetici o di spaziatura.
B) Successivamente, migliorate il programma in modo che visualizzi le 100 parole più comuni
(in caso di parità alla posizione 100, è indifferente quali parole si stampino).
"""

file_testo=input("Inserire il file.txt da controllare: ")
fp_in=open("{file_testo}","r",encoding="utf-8")



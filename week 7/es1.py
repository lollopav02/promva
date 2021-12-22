#letta una serie di matricole id( nl per terminare), si leggano i voti di ogni singolo alunno
#e si stampi la media dello studente id

finito=False
finito2=False
while not finito:
    id=input("matricola: ")

    if id == "":
        finito=True
else:
    finito2=False
    tot_score=0
    n_score=0
    while not  finito2:
        score=input("voto: ")
        if score == "":
            finito2=True
        else:
            tot_score += int(score)
            n_score += 1

print("media",id,":",tot_score/n_score)

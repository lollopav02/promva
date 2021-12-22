#suggerimento usr minima distanza di preferenze

from csv import reader
from math import sqrt
fp=open("movies.csv", "r")
csvR=reader(fp)
next(csvR)
DBmovie={}
for row in csvR:

    if row[1] not in DBmovie:
        DBmovie[row[1]]=set()

    DBmovie[row[1]].add(row[0])

fp.close()

#lettura DBuser
fp=open("users.csv", "r")
csvR=reader(fp)
next(csvR)
DBusr={}
for row in csvR:
    DBusr[row[0]]=set()
    for title in row[1:]:
        DBusr[row[0]].add(title)
fp.close()

#calcola score per genere di ciascun usr

DBusrScore={}

for usr in DBusr:
    UsrScore={}
    for genre in DBmovie:
        UsrScore[genre]=len(DBmovie[genre].intersection(DBusr[usr]))
    DBusrScore[usr]=UsrScore
print(DBusrScore)

id=input("login: ")
for usr in DBusr:
    if usr != id:
        distance=0
        for genre in DBmovie:
            distance+=(DBusrScore[id][genre]-DBusrScore[usr][genre])**2
        distance=sqrt(distance)
        print(usr,distance)
        if distance< distance_min:
            distance_min=distance
            id_match=usr
print(id,"<-->",id_match)

#impostare le info del movie.csv
#lista di movie,dove movie è un record(dict) con tante key quante sono le colonne del csv
#titolo,studio,genere,anno

from csv import reader
fp=open("movies.csv", "r")
csvR=reader(fp)
next(csvR)


movieList=[]
for row in csvR:
    movie = {}
    movie["title"]=row[0]
    movie["gen"]=row[1]
    movie["studio"]=row[2]
    movie["yr"]=row[7]
    movieList.append(movie)
    print(movie)
fp.close()
#stampa lista di movie
#for item in movieList:
#    print(item)

#ricerca per genere
genere="action"
for item in movieList:
    if item["gen"].lower()==genere:
        print(item["title"])
#vetrina per studio
print("----Universal---")
genere="romance"
studio="universal"
for item in movieList:
    if item["gen"].lower()==genere and item["studio"].lower()==studio:
        print(item["title"])
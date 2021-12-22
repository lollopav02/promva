#vetrina movie-by-studio
from csv import reader
ListGen=["romance","action","comendy","drama"]
ListStud=["universal","fox","disney"]
ListGenSet=[]
ListStudSet=[]
for i in range(len(ListGen)):
    ListGenSet.append(set())
for i in range(len(ListStud)):
    ListStud.append(set())
fp_csv=open("movies.csv", "r")
csvReader=reader(fp_csv)
next(csvReader)
for row in csvReader:
    gen=row[1]
    pos=ListGen.index(gen)
    ListGenSet[pos].add(row[0])
    stud=row[2].lower()
    pos=ListStud.index(stud)
    ListStudSet[pos].add(row[0])

fp_csv.close()


gen=input("genere [romance,action,comedy]: ")

for i,stud in enumerate(ListStud):
    print("-",stud,"-")
    if gen in ListGen:
        for movie in ListStudSet[i].intersection(ListStudSet[ListGen.index(gen)):
        print(movie)
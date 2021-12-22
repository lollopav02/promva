#vetrina movie-by-studio

from csv import reader

set_romance=set()
set_action=set()
set_comedy=set()

set_uni=set()
set_fox=set()
set_dis=set()


fp_csv=open("movies.csv", "r")
csvReader=reader(fp_csv)
next(csvReader)
for row in csvReader:
    if row[1].lower()=="romance":
        set_romance.add(row[0])
    if row[1].lower()=="action":
        set_action.add(row[0])
    if row[1].lower() == "comedy":
        set_comedy.add(row[0])
    if row[2].lower() == "universal":
        set_uni.add(row[0])
    if row[2].lower() == "fox":
        set_fox.add(row[0])
    if row[2].lower() == "disney":
        set_dis.add(row[0])


fp_csv.close()

gen=input("genere[romance,action,comedy]: ")
print("=universal= ")
if gen=="romance":
    set_tmp=set_uni.intersection(set_romance)
if gen=="action":
    set_tmp=set_uni.intersection(set_action)
if gen=="comedy":
    set_tmp=set_uni.intersection(set_comedy)
for item in set_tmp:
    print(item)


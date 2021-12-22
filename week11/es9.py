#operazione con e tra dizionari

fav_col={
    "franco":"red",
    "licia":"yellow",
}
#aggiungere una coppia key:val
fav_col["lauro"]="black"
print(fav_col)
fav_col["franco"]= "pink"
print(fav_col)
#eliminare una coppia key: val
fav_col.pop("lauro")
print(fav_col)
key="lauro"
if key in fav_col:
    fav_col.pop("lauro")
else:
    print("no key")
print(fav_col)
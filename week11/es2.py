#SETs/insiemi

col_set1={"red","green","blue"}
col_set2=set()#insieme vuoto
col_set2={"red","green"}
col_set3={"orange","red","blue"}
print(col_set1)
print(col_set2)
print(col_set3)#ordine "sparso" "casuale"
print("*********")
#col_set4=col_set1#alias
#col_set4=col_set1.copy()#copia
col_set4=set(col_set1)#copia

col_set4.add("black")
print(col_set4)
print(col_set1)
#trasforma lista in set
tmp_list=["yellow","orange","red"]
col_set5=set(tmp_list)
col_set5.add("black")
print(col_set5)
#"scansione" set
for item in col_set5:
    print(item)
print("---ordered")
for item in sorted(col_set5):
    print(item)

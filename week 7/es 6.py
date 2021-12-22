mylist=[1,3,5]
mylist2=[7,9,11]
print(mylist + mylist2)
mylist3=mylist+mylist2
print(mylist3)

mylist=mylist+mylist2
print(mylist)

mylist.extend(mylist2)
print(mylist)

mylist.append(mylist2)
print(mylist)
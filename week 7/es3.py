mylist=[1,2,3,4]
mylist2=mylist

mylist2[1]=-2
print(mylist)

mylist2=list(mylist)
mylist2[2]=-3
print(mylist)
print(mylist2)
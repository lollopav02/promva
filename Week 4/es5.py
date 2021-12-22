data=int(input("digitare anno:"))
if data%4! 0 or (data%100==0 and data>1582 and data%400 !=0):
    print(data, "non è bisestile")
else:
    print(data, "è bisestile")

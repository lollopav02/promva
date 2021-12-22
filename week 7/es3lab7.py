list1 = [1,4,9,16,9,7,4,9,11]
list2 = [11,11,7,9,16,4,1]

def sameset(list,list2):
    for i in list1:
        if i not in list2:
            return False
    for i in list2:
        if i not in list1:
            return False
    return True

print(sameset(list1,list2))


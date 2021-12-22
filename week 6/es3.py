# media tra due interi letti da tastiera

def avg2(a, b):
    avg = (a+b)/2
    return avg
    #return (a+b)/2

#chiamante
val_a = int(input("valore 1: "))
val_b = int(input("valore 2: "))
val_m = avg2(val_a, val_b)
print("media: ", val_m)
# print("media: ", avg2(val_a, val_b))
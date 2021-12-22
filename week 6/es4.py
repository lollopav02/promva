# swap di due variabili

def swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

def main():
    # chiamante
    val_a = 3
    val_b = 4
    print("prima: ", val_a, val_b)
    val_a, val_b = swap(val_a, val_b)
    print("dopo: ", val_a, val_b)
    return

val_a = 13
main()
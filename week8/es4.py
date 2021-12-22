#lettura matrice di dimensioni non note a priori

def readtab():
    f_matrix=[]
    finito=False
    while not finito:
        line=input()
        if line == "":
            finito=True
        else:
            f_list=[]
            line=line.split()
      #fmatrix.append(line)
            for item in line:
                f_list.append(int(item))
                f_matrix.append(f_list)
    return f_matrix

def main():
    mytab=[]
    mytab=readtab()
    print(mytab)
    return

main()
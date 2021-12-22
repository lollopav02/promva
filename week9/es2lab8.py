"""
Scrivete la funzione neighbor_average(values, row, column) che, in una
tabella values, calcoli il valore medio dei vicini di un elemento nelle otto direzioni,
come si può vedere nella figura sotto. Se, però, l’elemento si trova su un bordo della
tabella, la media va calcolata considerando soltanto i vicini che appartengono
effettivamente alla tabella. Ad esempio, se row e column valgono entrambe 0, ci
sono soltanto tre vicini.
"""

def averageValues(matrix,row,column):
    somma=0
    count=0

    for i in range(row-1,row+2):
        for j in range(column-1,column+2):
            if i>=0 and i<len(matrix) and j>=0 and j<len(matrix[i]) and (i,j) != (row,column):
                somma += matrix[i][j]
                count += 1
    return somma/count #media

def main():
#matrix
    matrix=[[1,8,7,0],[3,4,5,6],[0,0,0,0],[10,11,12,13]]
    for i in range(len(matrix)):
        print(matrix[i])

    row=int(input("inserire riga: "))
    column=int(input("inserire colonna: "))
    avg=averageValues(matrix,row,column)

    print("media vicini: "+str(avg))


main()
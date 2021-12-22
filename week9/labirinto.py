#labirinto

def findNext(map,r,c):
    r_next=-1
    c_next=-1

    if r>0 and map[r-1][c]==1:
        r_next=(r-1)
        c_next=c
    if c<len(map[0])-1 and map[r][c+1]==1:
        c_next=c+1
        r_next = r
    if c>0 and map[r][c-1]==1:
        c_next=c-1
        r_next=r
    if r<len(map) and map[r+1][c]==1:
        c_next=c
        r_next = r + 1
    return r_next,c_next

def isExit(map,r,c):

    if r==len(map)-1 or r==0 or c==0 or c==len(map[0])-1:
        exit=True
    else:
        exit=False

    return exit

def main():

    map=[
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    r=0
    c=2
    finito=False
    while not finito:
        (r_next,c_next) =findNext(map,r,c)
        if not r_next!=-1 and not c_next!=-1:
            map[r][c]= 0
            r= r_next
            c= c_next
            print(r,c)
            if isExit(map,r,c):
                finito = True
                print("OUT")
        else:
            finito =True
            print("NO WAY")
    return

main()
#---I-------I---
#x:    ^
#sx      dx

sx=2
dx=8
x=int(input("x: "))
#inclusione
if x>sx and x<dx:
    print("incluso")
#esclusione
    if x<sx or x>dx:
        print("escluso")

# not !
piove=False
if not piove:
    print("esco")

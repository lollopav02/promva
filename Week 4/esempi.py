"""rate=5.0
initial_balance=5
target=2*initial_balance

balance=initial_balance
year=0
while balance< target:
    year= year+1
    interest=balance*rate/100
    balance=balance+interest

    print("the investment double after",year,"years")"""

"""i= 0
total= 0
while total<10:
    i=i+1
    total=total+1

    print(i,total)"""

"""""=0
total=0
while total<10:
    i=i+1
    total=total+1

    print(i,total)"""

"""count=0
ok=True
while(count<10) and ok :
    a=int(input("number: "))
    if a==0:
        ok=False
        print(f"number {count+1}={a}")
        count= count+1"""

n=1729
total=0
while n>0:
    digit= n%10
    total=total+digit
    n=n//10
    print(total)
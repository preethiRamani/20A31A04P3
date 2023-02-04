term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))

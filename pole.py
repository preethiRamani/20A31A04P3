def felicia(n,a,b,c):
    if n>0:
        felicia(n-1,a,c,b)
        if a:
            c.append(a.pop())
            felicia(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
felicia(len(a),a,b,c)
print("after the puzzle")
print(a,b,c)

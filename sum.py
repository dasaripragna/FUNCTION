def fun(a):
    sum=1
    i=0
    while i<len(a):
        sum=sum+a[i]
        i=i+1
    return sum
a=[8,2,3,0,7]
print(fun(a))
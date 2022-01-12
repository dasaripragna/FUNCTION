def sum(n):
    sum=0
    i = 0
    while i<len(n):
        sum=sum+n[i]
        i=i+1
    return sum
print(sum([8, 2, 3, 0, 7]))

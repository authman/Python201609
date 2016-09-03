a=[2,4,10,16]
def multiply(lst,n):
    out = []
    for i in lst:
        out.append(i * n)
    return out

b = multiply(a,5)
print b

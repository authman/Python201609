a=[2,4,10,16]

def mult(alist,multiple):
    for i in range(0,len(alist)):
        alist[i]=alist[i]*multiple
    return alist
        
b = mult(a,5)
print b


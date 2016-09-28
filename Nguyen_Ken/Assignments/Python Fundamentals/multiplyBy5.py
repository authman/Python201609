#multiply by 5
def multiply(a,b):
    for i in range(len(a)):
        a[i] *= b
    return a

ken=[1,2,3,15,14,13,7,7,14,500]
k2 = [2,4,10,16]

koolio = multiply(ken,5)
print koolio


def insertionSort(lst):
    temp = lst[0]
    for n in range(1,len(lst)):
        temp = lst[n]
        if lst[n] < lst[n-1]:
            i = n-1
            while lst[i] > temp and i >= 0:
                lst[i+1] = lst[i]
                i -= 1
            lst[i+1] = temp
    return a


a = [8,3,7,12,0,54,2,6]

print insertionSort(a)

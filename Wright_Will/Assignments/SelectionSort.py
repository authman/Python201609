
def selectionSort(lst):
    for n in range(len(lst)):
        minimum = lst[n]
        index = n
        for i in range(n,len(lst)):
            if lst[i] < minimum:
                minimum = lst[i]
                index = i
        lst[index] = lst[n]
        lst[n]=minimum
    return lst

a = [1,4,7,3,12,6,3,33,6]

print selectionSort(a)


def bubbleSort(lst):
    for n in range(len(lst)):
        for i in range(1,len(lst)):
            if lst[i-1] > lst[i]:
               temp = lst[i-1]
               lst[i-1] = lst[i]
               lst[i] = temp
    return lst
a = [2,6,4,9,12,5,3,7]

print(bubbleSort(a))

#bubble sort assignment

list = [8,9,17,5,3,2,6,1,17,18,20,24,14,12,10,9]


i = 0

while i < (len(list)-1):
    if (list[i+1]<list[i]):

        temp = list[i]
        list[i]=list[i+1]
        list[i+1]=temp

        i = 0

    else:
        i+=1
        continue


print list

#selection sort assignment

list = [2,4,8,9,55,61,22,8,80,91,100,-100,79,14,31,13,3,7]

for i in range(len(list)):
    for j in range(i,len(list)):

        min = list[i]

        if list[j]<min:
            min=list[j]
            temp=list[i]
            list[i]=min
            list[j]=temp

print list

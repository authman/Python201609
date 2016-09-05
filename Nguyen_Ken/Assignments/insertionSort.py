#insertion sort assignment

list = [2,4,8,9,55,61,22,8,80,91,100,-100,79,14,31,13,3,7]

for i in range(len(list)):
    count = 0
    while count < i:
        if list[i]<list[count]:
            temp=list[i]
            for j in range(i,count,-1):
                list[j]=list[j-1]
            list[count]=temp

        else:
            count += 1


print list

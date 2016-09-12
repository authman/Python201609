#insertion sort assignment

list = [2,4,8,9,55,61,22,8,80,91,100,-100,79,14,31,13,3,7]

for i in range(len(list)):
    pointer = 0
    while pointer < i:
        if list[i]<list[pointer]:
            temp=list[i]
            for j in range(i,pointer,-1):
                list[j]=list[j-1]
            list[pointer]=temp

        else:
            pointer += 1


print list

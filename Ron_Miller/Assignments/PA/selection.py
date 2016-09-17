def genList():
    import random
    sList =[]
    for i in range(0,100):
        temp= random.randint(1,1000)
        sList.append(temp)
    print sList
    return sList

def selectSort(aList):
    for i in range(0,len(aList)):
        index=i
        m=aList[i]
        for j in range(i,len(aList)):
            if m>aList[j]:
                index=j
                m=aList[j]
                ##aList[i],aList[j]=aList[j],aList[i]
        aList[i],aList[index]=aList[index],aList[i]    
    return aList

 
    
       

print selectSort(genList())


def genList():
    import random
    sList =[]
    for i in range(0,100):
        temp= random.randint(1,1000)
        sList.append(temp)
    print sList
    return sList

def bubSort(aList):
    for i in range(0,len(aList)):
        for j in range(0,len(aList)-(i+1)):
            if(aList[j]>aList[j+1]):
                aList[j],aList[j+1]=aList[j+1],aList[j]
                
       
                
    return aList
test1=[1,2,8,4,5,6,7,3]
print bubSort(genList())
print bubSort(test1)

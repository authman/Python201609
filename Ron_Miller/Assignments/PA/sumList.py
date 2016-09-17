list=[1,2,5,10,255,3]

def avgNum(n):
    sum=0
    avg=0
    for i in range(0,len(list)):
        sum += list[i]
    avg=sum/len(list)    
    print avg

avgNum(list)
        
    

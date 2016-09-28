x=[4,6,1,3,5,7,25]
def draw_stars(numList):
    for i in range(0,len(numList)):
        
        for j in range(0,numList[i]):
            print "* ",
        print ""
draw_stars(x)

y=[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def draw_stuff(numList):
    for i in range(0,len(numList)):
        if type (numList[i])== int:        
            for j in range(0,numList[i]):
                print "* ",
            print ""
        else:
            for k in range(0,len(numList[i])):
                print numList[i][0].lower(),
            print""
                           
draw_stuff(y)

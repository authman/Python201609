def scores(students):
    studentList=[]
    for i in range(0,students):
        studentList+= [input("What is your grade?")]
    print "Scores and Grades "
    for j in range(0,len(studentList)):
        if studentList[j] >= 60 and studentList[j]<=69:
            print "Score: " +str(studentList[j])+"; Your Grade is a D dummy."
        elif studentList[j] >= 70 and studentList[j]<=79: 
            print "Score: " +str(studentList[j])+"; Your Grade is a C."                  
        elif studentList[j] >= 80 and studentList[j]<=89: 
            print "Score: " +str(studentList[j])+"; Your Grade is a B."                      
        elif studentList[j] >= 90 and studentList[j]<=100: 
            print "Score: " +str(studentList[j])+"; Your Grade is a A like a Boss."                     
        else:
            print"That is a crappy grade."                  
    print "End of Program.Bye!"
scores(10)

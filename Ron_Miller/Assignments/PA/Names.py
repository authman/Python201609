students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def studentNames(inList):
    for i in range(0,len(inList)):
        print students[i]['first_name']+" "+ students[i]['last_name']
studentNames(students)


users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def studInst(inDict):
    
        if inDict['Students']:
            print "Students"
            for j in range(0,len(inDict['Students'])):
                print str(j+1)+" - " + inDict['Students'][j]['first_name']+" "+ inDict['Students'][j]['last_name']+" - "+ str(len(inDict['Students'][j]['first_name'])+len(inDict['Students'][j]['last_name']))

        if inDict['Instructors']:
            print "Instructors"
            for k in range(0,len(inDict['Instructors'])):
                print str(k+1)+" - " + inDict['Instructors'][k]['first_name']+" "+ inDict['Instructors'][k]['last_name']+" - "+ str(len(inDict['Instructors'][k]['first_name'])+len(inDict['Instructors'][k]['last_name']))           
                   
        
studInst(users)

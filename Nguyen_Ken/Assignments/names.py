#names

########################### part 1 ###########################
students = [
    {'first_name': 'Michael', 'last_name': 'Jordon'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def outputStudents():
    for i in students:
        print i['first_name'], i['last_name']

print "Part I: "
outputStudents()



########################### part 2 ###########################
users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordon'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}



#append names in a list
names = []

def outputNames():
    for key,data in users.items():
        for d in data:
            names.append(d['first_name'] + ' ' + d['last_name'])

outputNames()

#capitalize names in list
def capitalize():
    for i in range(len(names)):
        names[i] = names[i].upper()

capitalize()

#count characters in each list
def countCharacters(a):
    return len(names[a])

def outputInstructors():
    for i in users:
        print i
        for k in range(len(users[i])):
            if (i=='Students'):
                print str(k+1) + ' - ' + names[k] + ' - ' + str(countCharacters(k)-1)

            elif (i=='Instructors'):
                print str(k+1) + ' - ' + names[k+4] + ' - ' + str(countCharacters(k+4)-1)


print ' '
print 'Part II:'
outputInstructors()

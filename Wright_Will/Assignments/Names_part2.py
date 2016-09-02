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

for key in users.iterkeys():
    print key
    i = 1
    for  n in users[key]:
        fName = n["first_name"]
        lName = n["last_name"]
        print str(i) +" - "+fName.upper() + " " + lName.upper() +" - "+ str(len(fName)+len(lName))
        

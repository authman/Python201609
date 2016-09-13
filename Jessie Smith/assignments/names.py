


students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for value in students:
	print value["first_name"], value["last_name"]

# 1)print ordinal number
# 2)print names
# 3)print number of characters

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


for key in users:
	print key
	
	alist=users[key]
	count=0
	for value in alist:#can use users[key] here
		count +=1
		print count,"-", value["first_name"], value["last_name"],"-", str(len(value["first_name"])+(len(value["last_name"])))

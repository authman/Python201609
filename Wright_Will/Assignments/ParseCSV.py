## parse csv

import csv
import pprint
import re
with open("us-500.csv","rU") as csvfile:
    read = csv.reader(csvfile)
    heading = read.next()
    print heading         #get key names
    data = {}                       #initialize big dictionary

    #parse into dictionary
    for row in read:
        fname = row[0]+ " "+row[1]              # get persons fullname
        data[fname] = {}                        #initialize person with key = persons fullname
        for i in range(len(heading)):
            data[fname][heading[i]] = row[i]    # add each piece of data with the correct key taken from the heading

#note these are not in order
#because I chose to parse int a dictionary
#instead of a list
#print
def printPerson(person,data):
    print person
    for each in data[person]:
        print each + ": " +data[person][each]
    print "-"*12



def lookup(key,regex,data):
    for person in data:
        if re.search(regex,data[person][key]):
            printPerson(person,data)

#print people whos first name starts with A

# lookup("first_name",r"\bA",data)

#or print everybody
lookup("first_name",r"",data)

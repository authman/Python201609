class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next


class Singly(object):
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

## add new value to back
    def addBack(self,data):
        temp=self.tail
        newNode = Node(data)
        
        if self.tail==None:
            self.head=newNode
            self.tail=newNode
            return self
        
        temp.next=newNode
        self.tail=newNode
## add new value to front
    def addFront(self,data):
        temp=self.head
        newNode = Node(data)
        
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            return self
        
        newNode.next=temp
        self.head=newNode
## insertBefore
    def insertBefore(self,nVal,val):
        if self.isEmpty():
            self.addFront(val)
        elif self.head.data==nVal:
            temp=self.head
            while temp:
                if temp.data==nVal:
                    run=temp.next
                    newNode=Node(val,temp.next)
                    temp.next=newNode
                temp=temp.next 
        else:
            temp=self.head.next
            while temp:
                if temp.data==nVal:
                    run=temp.next
                    newNode=Node(val,temp.next)
                    temp.next=newNode
                temp=temp.next            

## insert after
    def insertAfter(self,pVal,val):
        if self.isEmpty():
            self.addFront(val)
            print "fail"
        else:
            temp=self.head
            print "Closer"
            while temp:
                if temp.data==pVal:
                    print "got here"
                    newNode=Node(val,temp.next)
                    temp.next=newNode
                temp=temp.next    

    def printVal(self):
        temp=self.head
        while temp:
            print  temp.data
            temp=temp.next

    def ReverseList(self):
        temp=self.tail
        while temp:
            print  temp.data
            temp=temp.nex
        
## check if list is empty
    def isEmpty(self):
        if self.head ==None:
            return True
    
    def removeNode(self,val):
        temp=self.head.next
        if self.isEmpty():
            print " This list is empty!"
        else:
            while temp:
                if temp.data==val:
                    run=temp.next
                    newNode=Node(val,temp.next)
                    temp.next=newNode
                temp=temp.next     



A=Singly()

A.addBack(9)
A.addBack(8)
A.addBack(7)
A.addBack(6)
A.addFront(5)
A.addFront(4)                     
A.addFront(3)
A.addFront(2) 
A.printVal()
A.insertBefore(5,10)
A.printVal()
A.insertAfter(2,11)
A.printVal()
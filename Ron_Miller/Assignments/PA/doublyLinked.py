class Node(object):

    def __init__(self,d,n=None, p=None):
        self.data =d
        self.next =n
        self.prev=p

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next=n

    def getPrev(self):
        return self.prev
    
    def setPrev(self,p):
        self.prev =p

    def getData(self):
        return self.data

    def setData(self,d):
        self.data=d


class DList(object):
    def __init__(self,head=None, tail=None):
        self.head =head
        self.tail= tail
        self.size=0

    def getSize(self):
        return self.size

    def addH(self,d):
        newNode=Node(d)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.setNext(None)
            newNode.setPrev(self.tail)
            self.tail.next =newNode
            self.tail=newNode
    
            

    def remove(self,d):
        temp=self.head
        while temp:
            if temp.getData()==d:
                next=temp.getNext()
                prev=temp.getPrev()

                if next:
                    next.setPrev(prev)

                if prev:
                    prev=temp.getPrev()

                else:
                    self.head =temp
                self.size -=1
                return true
        return false


    def find(self,d):
        temp=self.head
        while temp:
            if temp.getData()==d:
                return temp.getData()
        return None
    def printData(self):
        temp=self.tail
        while temp:
            print temp.getData()
            temp=temp.getPrev()

    def printRev(self):
        temp=self.head
        while temp:
            print temp.getData()
            temp=temp.getNext()

myList=DList()
myList.addH(3)
myList.addH(6)
myList.addH(9)
myList.addH(4)
myList.addH(2)
myList.printData()
myList.printRev()




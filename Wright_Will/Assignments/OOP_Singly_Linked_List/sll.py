import pprint
pp = pprint.PrettyPrinter(indent=4)
class Node(object):
    def __init__(self,val,nextN=None):
        self.val = val
        self.next = nextN

class SLL(object):
    def __init__(self):
        self.head = None

    def add_To_Front(self,val):
        self.head = Node(val,self.head)
        return self
    def add_To_Back(self,val):
        N = self.head
        while N.next != None:
            print N.val
            N = N.next
        N.next = Node(val)
        return self
    def forEach(self,fn):
        N = self.head
        while N != None:
            fn(N)
            N = N.next
        return self

    def print_all(self):
        self.forEach(self.__print_val)
        return self
    def __print_val(self,N):
        print N.val

    def get_last(self):
        N = self.head
        while N.next != None:
            N = N.next
        return N
    def __id(self):
        return self

    def get_last_R(self,N=None):
        if not N :
            N = self.head
        if N.next == None:
            return N
        return self.get_last_R(N.next)

    #
    # def find_by_index(self,index):
    #     N = self.head
    #     while N.next != None:
    # def insert_in_order(val):
    #     N=self.head
    #     while N.next != None and N.next.val >




sll = SLL()
sll.add_To_Front("a")
# print mylist.head.val
# print "_________"
sll.add_To_Front("b")
# print mylist.head.val, mylist.head.next.val, mylist.head.next.next
# print "_________"
sll.add_To_Back("c")
# print mylist.head.val, mylist.head.next.val, mylist.head.next.next.val
# print "_________"
# sll.print_all()
print


# print sll.get_last_R().val

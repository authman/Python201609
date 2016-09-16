class Dbl_Linked_List(object):
    def __init__(self):
        self.head = Node(None,None,None)
        self.tail = Node(None,self.head,None)
        self.head.next = self.tail
    def delete(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
        return self
    def insert_at_start(self,value):
        self.insert_after(value,self.head)
        return self
    def insert_at_end(self,value):
        self.insert_before(value,self.tail)
        return self
    def insert_after(self,value,nodeBefore):
        nodeBefore.next.prev = Node(value,nodeBefore,nodeBefore.next)
        nodeBefore.next = nodeBefore.next.prev
        return self
    def insert_before(self,value,nodeAfter):
        nodeAfter.prev.next = Node(value,nodeAfter.prev,nodeAfter)
        nodeAfter.prev = nodeAfter.prev.next
        return self
    def loop_from_node(self,start,fn):
        if start.next.val == None:
            return
        fn(start.next)
        self.loop_from_node(start.next,fn)
    def loop_forwards(self,fn):
        self.loop_from_node(self.head,fn)
        return self
    def print_all(self):
        self.loop_forwards(self.print_val)
    def print_val(self,x):
        print x.val
    #*****these dont work yet****
    # def loop_till(self,start,fn):
    #     if fn(start.next):
    #         return start.next
    #     elif start.next == self.tail:
    #         return False
    #     return self.loop_till(start.next,fn)
    # def find_val(self,val):
    #     return self.loop_till(self.head,lambda x: True if x == val else False)
    #** still want to add get_val_by_index(), add_after_index() splice()
class Node(object):
    def __init__(self,val,prevN,nextN):
        self.val = val
        self.prev = prevN
        self.next = nextN

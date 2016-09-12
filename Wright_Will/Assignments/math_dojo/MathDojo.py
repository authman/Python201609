#
class MathDojo(object):
    """docstring for MathDojo."""
    def __init__(self):
        super(MathDojo, self).__init__()
        self.result = 0

    #**** I hope to come back and make a _each method that will consolidate the recursive for each from the add and subtract functions
    # def _each(self,x,fn):
    #     if type(x) is int or type(x) is float:
    #          fn(x)
    #     elif type(x) is list or type(x) is tuple:
    #         for each in x:
    #             self[fn](each)
    #     else: print "unsupported type"
    #     return self
    def _add(self,x):
        if type(x) is int or type(x) is float:
             self.result += x
        elif type(x) is list or type(x) is tuple:
            for each in x:
                self._add(each)
        else: print "unsupported type"
        return self
    def add(self,n,*rest):
        self._add(n)
        self._add(rest)
        return self

    def _sub(self,x):
        if type(x) is int or type(x) is float:
             self.result -= x
        elif type(x) is list or type(x) is tuple:
            for each in x:
                self._sub(each)
        else: print "unsupported type"
        return self

    def sub(self,n,*rest):
        self._sub(n)
        self._sub(rest)
        return self


a = (1,2,3)
b = [1,2,3]
c = 1.1


md = MathDojo()
md2 = MathDojo()
# print md2._each([5,5],"_add")
print md.add([5,5],5).add([5],[5,5],5).sub(5,(5,5)).result

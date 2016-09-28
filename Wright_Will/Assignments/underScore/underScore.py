class underScore(object):
    def __init__(self):
        super(underScore, self).__init__()
        self.pi = 3.14159
    #maps an iterble in place
    def map(self,iterbl,fn):
        for i in range(len(iterbl)):
            iterbl[i] = fn(iterbl[i])
        return iterbl
    def reduce(self,iterbl,fn,out):
        for each in iterbl:
            out = fn(each,out,iterbl)
        return out
    def find(self,iterbl,findme):
        for i in range(len(iterbl)):
            if iterbl[i] == findme:
                return i
        return -1
    def filter(self,iterbl,fn):
        if type(iterbl) is tuple:
            out = ()
        else:
            out = []
        for each in iterbl:
            if fn(each):
                out.append(each)
        return out
    def reject(self,iterbl,fn):
        if type(iterbl) is tuple:
            out = ()
        else:
            out = []
        for each in iterbl:
            if not fn(each):
                out.append(each)
        return out


_ = underScore()


a = [1,2,3]
#print _.map(a,lambda x: x*x)
# print _.reduce(a,lambda each,out,iterbl: each + out, 0)
# print _.find(a,1)
#print _.filter(a,lambda x: x < 2)
print _.reject(a,lambda x: x < 2)

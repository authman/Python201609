class MathDojo(object):
    def __init__(self):
        self.number=0

    def add(self,*args):
        input=args
        for i in range(len(input)):
            if type(input[i])==list:
                self.number+=sum(input[i])

            elif type(input[i])==int:
                      self.number+=input[i]

            else:
                self.add(*input[i])

        return self

    def subtract(self,*args):
        input=args
        for i in range(len(input)):
            if type(input[i])==list:
                self.number-=sum(input[i])

            elif type(input[i])==int:
                      self.number-=input[i]

            else:
                self.subtract(*input[i])

        return self
    def getResult(self):
        return self.number

md = MathDojo().add(1,3,4,[1,3,4],(3,4,5,[2,3,4,5],[2],2)).number
print md
sb=MathDojo().subtract(1,3,4,[1,3,4],(3,4,5,[2,3,4,5],[2],2)).number
print sb



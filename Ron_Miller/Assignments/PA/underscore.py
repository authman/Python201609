class Underscore(object):
    def map(self, arr, func):
        result = []
        for x in arr:
            result.append(func(x))
        return result

    def reduce(self, arr,func,memo=0):
        x=0
        for y in range(len(arr)):
            x+=func(arr[y],memo)
        return x
            
    def find(self,arr,func):
        for x in arr:
            if arr[x] == func(x):
                return x
            else:
                print "No such condition exists"
                return self
    def filter(self,arr,func):
        result=[]
        for i in range(len(arr)):
            if func(arr[i]):
                result.append(arr[i])
        return result     

    def reject(self,arr,func):
        result=[]
        for i in range(len(arr)):
             if not(func(arr[i])):
                result.append(arr[i])
        return result   
        # your code
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
print(evens)
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(odds)
T = _.reduce([1, 2, 3, 4, 5, 6], lambda num,memo: num + memo)
print(T)

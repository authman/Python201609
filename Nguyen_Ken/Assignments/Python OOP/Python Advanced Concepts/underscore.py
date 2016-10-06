#underscore assignment

#lambda x: x**2

#should practice comprehensions

class Underscore(object):
    def map(self, arr, iteratee):
        return [iteratee(arr[index], index, arr) for index in range(len(arr))]

        # result = []
        # for index in range(len(arr)):
        #     result.append( iteratee(arr[index], index, arr))
        # return result

    def reduce(self, arr, iteratee, memo=None):
        # return [interatee(memo, arr[index], index, arr) for index in range(len(arr)) memo = arr[0] if index==0 and memo==None else continue]

        for index in range(len(arr)):
            if index==0 and memo==None:
                memo = arr[0]
                continue
            memo = iteratee(memo, arr[index], index, arr)
        return memo

    def find(self, arr, predicate):
        # return for element in arr element if predicate(element)

        for element in arr:
            if predicate(element):
                return element
        return None

    def filter(self, arr, predicate):
        filterList = []
        for element in arr:
            if predicate(element):
                filterList.append(element)
        return filterList

    def reject(self, arr, predicate):
        rejectList = []
        for element in arr:
            if not predicate(element):
                rejectList.append(element)
        return rejectList



pie = Underscore()
print pie.map([1,2,3,4,5], lambda num, key, arr: num**2)
print pie.reduce([1,2,3], lambda memo,num,key,arr: memo+num, 2)
print pie.find([1,2,3,4,5,6], lambda num: num % 2 == 0 and num > 4)
print pie.filter([1,2,3,4,5,6,7,8,9,10], lambda num: num % 2 == 0 and num > 3)
print pie.reject([1,2,3,4,5,6,7,8,9,10], lambda num: num % 2 == 0)

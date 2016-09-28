#math dojo
#
#part 1
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#     def add(self, *x):
#         self.addThis = 0
#         for value in x:
#             self.addThis += value
#         self.result += self.addThis
#         return self
#     def subtract(self, *y):
#         self.subThis = 0
#         for value in y:
#             self.subThis += value
#         self.result -= self.subThis
#         return self
#
#
#
# md = MathDojo().add(2).add(2,5).subtract(3,2).result
#
# print md




# part 2
# class MathDojo(object):
#     def __init__(self):
#         self.result = 0
#
#     def add(self, *x):
#         for obj in x:
#             if type(obj) == list:
#                 for value in obj:
#                     self.result += value
#             elif type(obj) == int:
#                 self.result += obj
#         # isinstance <-- python
#         return self
#
#     def subtract(self, *a):
#         for obj in a:
#             if type(obj) == list:
#                 for value in obj:
#                     self.result -= value
#             elif type(obj) == int:
#                 self.result -= obj
#         return self
#
#
# list1 = [1,2,3,4,6]
# list2 = [3,5,7,9]
#
# md2 = MathDojo().add(list2,list1,5,6,list2).subtract(10,list1).result
#
# md3 = MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result
#
# print md3




#part 3
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self, *x):
        for obj in x:
            if isinstance(obj, (list, tuple)):
                for value in obj:
                    self.result += value
            elif isinstance(obj, int):
                self.result += obj
        return self

    def subtract(self, *a):
        for obj in a:
            if isinstance(obj, (list, tuple)):
                for value in obj:
                    self.result -= value
            elif isinstance(obj, int):
                self.result -= obj
        return self


list1 = [1,2,3,4,6]
# list2 = [3,5,7,9]
#
# md2 = MathDojo().add(list2,list1,5,6,list2).subtract(10,list1).result
#
# md3 = MathDojo().add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result

tuple1 = (1,2,3,5.6,10)
tuple2 = (5,10,15)

md4 = MathDojo().add(tuple1,list1,14).subtract(tuple2,tuple1,7).result

print md4

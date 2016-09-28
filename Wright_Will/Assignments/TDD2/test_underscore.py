import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.squared = lambda x: x * x
        self.map_result = self._.map([1,2,3,4,5], self.squared)
        self.sum = lambda x,y: x + y
        self.reduce_result = self._.reduce([1,2,3,4,5], self.sum,0)
        self.find_result1 = self._.find([0,1,2,3,4],lambda x: x == 2)
        self.filter_result1 = self._.filter([0,1,2,3,4],lambda x: x > 2)
        self.reject_result1 = self._.reject([0,1,2,3,4],lambda x: x > 2)

    def testMap(self):
        return self.assertEqual([1,4,9,16,25], self.map_result)
    def testReduce(self):
        return self.assertEqual(15, self.reduce_result)
    def testFind(self):
        return self.assertEqual(2,self.find_result1)
    def testFilter(self):
        return self.assertEqual([3,4],self.filter_result1)
    def testReject(self):
        return self.assertEqual([0,1,2],self.reject_result1)

if __name__ == "__main__":
    unittest.main()

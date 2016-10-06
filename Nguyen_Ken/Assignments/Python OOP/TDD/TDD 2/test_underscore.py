import unittest
from underscore import Underscore

class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        
        # create an instance of the Underscore module we created
        self._ = Underscore()

        
        # initialize a list to run our tests on
        self.map_test_list = [1,2,3,4,5]
        self.test_list = [1,2,3,4,5]


        # set up test functions with inputs
        self.testMaptest = self._.map(self.map_test_list, lambda num: num**2)
            #result: [1, 4, 9, 16, 25]
            #print self.test_list         this is how i debugged, the list was already changed in place
        self.testReducetest = self._.reduce(self.test_list, lambda memo, num: memo+num, 0)
            #result: 15
        self.testFindtest = self._.find(self.test_list, lambda num: num % 2 == 0 and num > 3)
            #result: 4
        self.testFiltertest = self._.filter(self.test_list, lambda num: num % 2 == 1)
            #result: [1, 3, 5]
        self.testRejecttest = self._.reject(self.test_list, lambda num: num % 2 == 1)
            #result: [2,4]
        
    def testMap(self):
        return self.assertEqual([1, 4, 9, 16, 25], self.testMaptest)
    def testReduce(self):
        return self.assertEqual(15, self.testReducetest)
    def testFind(self):
        return self.assertEqual(4, self.testFindtest)
    def testFilter(self):
        return self.assertEqual([1, 3, 5], self.testFiltertest)
    def testReject(self):
        return self.assertEqual([2,4], self.testRejecttest)

if __name__ == "__main__":
    unittest.main()


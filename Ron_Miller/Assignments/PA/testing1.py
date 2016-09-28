def insert_val_at(index, my_list, value):
    newArr=my_list
    if index>len(my_list)-1:
        return False
    for i in range(len(my_list)):
        if i==index:
            newArr=my_list[0:i]
            newArr.append(value)
            newArr=newArr+my_list[i:]

    return newArr
            
import unittest

class InsertValueTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [0,1,2,3,4]
        self.result = insert_val_at(2, self.test_list, 100)
        self.result2 = insert_val_at(6,self.test_list,100)
    def testInsertAtIndexTwo(self):
        return self.assertEqual([0,1,100,2,3,4], self.result)
    def testReturnFalseForInvalidIndex(self):
        return self.assertEqual(False, self.result2)
if __name__ == "__main__":
    unittest.main()
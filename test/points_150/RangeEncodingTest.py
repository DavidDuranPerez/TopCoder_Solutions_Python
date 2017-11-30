import unittest
from problems.points_150.RangeEncoding import RangeEncoding


class RangeEncodingTest(unittest.TestCase):
    # Setup for all the tests
    def setUp(self):
        # Create the object
        self.obj_class = RangeEncoding()

    # Test 0
    def test0(self):
        # Input
        arr=[1,2,3,4,5,6,7,8,9,10]

        # Output
        output=1

        # Result comparison
        self.assertEqual(output, self.obj_class.minRanges(arr))

    # Test 1
    def test1(self):
        # Input
        arr = [1, 6, 10, 20, 32, 49]

        # Output
        output=6

        # Result comparison
        self.assertEqual(output, self.obj_class.minRanges(arr))

    # Test 2
    def test2(self):
        # Input
        arr = [2,4,5,6,8,9,10,11,12,15]

        # Output
        output=4

        # Result comparison
        self.assertEqual(output, self.obj_class.minRanges(arr))

    # Test 3
    def test3(self):
        # Input
        arr = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

        # Output
        output=14

        # Result comparison
        self.assertEqual(output, self.obj_class.minRanges(arr))

if __name__ == '__main__':
    unittest.main()
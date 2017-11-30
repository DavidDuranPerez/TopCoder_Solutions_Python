import unittest
from problems.points_200.Genetics import Genetics


class GeneticsTest(unittest.TestCase):
    # Setup for all the tests
    def setUp(self):
        # Create the object
        self.obj_class = Genetics()

    # Test 0
    def test0(self):
        # Inputs
        g1="AAAA"
        g2="AAaa"
        dom="DRDR"

        # Expected output
        output="AAAa"

        # Result comparison
        self.assertEqual(output, self.obj_class.getOffspring(g1,g2,dom))

    # Test 1
    def test1(self):
        # Inputs
        g1 = "ABCDEFG"
        g2 = "abcdefg"
        dom = "DDRRRDR"

        # Expected output
        output = "ABcdeFg"

        # Result comparison
        self.assertEqual(output, self.obj_class.getOffspring(g1, g2, dom))

    # Test 2
    def test2(self):
        # Inputs
        g1 = "Z"
        g2 = "z"
        dom = "D"

        # Expected output
        output = "Z"

        # Result comparison
        self.assertEqual(output, self.obj_class.getOffspring(g1, g2, dom))

    # Test 3
    def test3(self):
        # Inputs
        g1 = "MGskgzTFQoclnDjZu"
        g2 = "mgSKGzTFQoClnDJzU"
        dom = "DDDDDRDDDDRDDDDDD"

        # Expected output
        output = "MGSKGzTFQoclnDJZU"

        # Result comparison
        self.assertEqual(output, self.obj_class.getOffspring(g1, g2, dom))

if __name__ == '__main__':
    unittest.main()
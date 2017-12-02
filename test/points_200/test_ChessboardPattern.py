import unittest
from problems.points_200.ChessboardPattern import ChessboardPattern


class RangeEncodingTest(unittest.TestCase):
    # Setup for all the tests
    def setUp(self):
        # Create the object
        self.obj_class = ChessboardPattern()

    # Test 0
    def test0(self):
        # Input
        rows=8
        columns=8

        # Output
        output=("X.X.X.X.", ".X.X.X.X", "X.X.X.X.", ".X.X.X.X",
                          "X.X.X.X.", ".X.X.X.X", "X.X.X.X.", ".X.X.X.X")

        # Result comparison
        self.assertEqual(output,self.obj_class.makeChessboard(rows, columns))

    # Test 1
    def test1(self):
        # Input
        rows=1
        columns=20

        # Output
        output=(".X.X.X.X.X.X.X.X.X.X",)

        # Result comparison
        self.assertEqual(output,self.obj_class.makeChessboard(rows, columns))

    # Test 2
    def test2(self):
        # Input
        rows=5
        columns=1

        # Output
        output=(".", "X", ".", "X", ".")

        # Result comparison
        self.assertEqual(output,self.obj_class.makeChessboard(rows, columns))


    # Test 3
    def test3(self):
        # Input
        rows=5
        columns=13

        # Output
        output=(".X.X.X.X.X.X.", "X.X.X.X.X.X.X", ".X.X.X.X.X.X.", "X.X.X.X.X.X.X", ".X.X.X.X.X.X.")

        # Result comparison
        self.assertEqual(output,self.obj_class.makeChessboard(rows, columns))

if __name__ == '__main__':
    unittest.main()
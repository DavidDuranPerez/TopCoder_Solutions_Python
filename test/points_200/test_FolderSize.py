import unittest
from problems.points_200.folder_size import FolderSize


class GeneticsTest(unittest.TestCase):
    # Setup for all the tests
    def setUp(self):
        # Create the object
        self.obj_class = FolderSize()

    # Test 0
    def test0(self):
        # Inputs
        files=("0 55", "0 47", "1 86")
        folderCount=3
        clusterSize=50

        # Expected output
        output=(48, 14, 0)

        # Result comparison
        self.assertEqual(output, self.obj_class.calculateWaste(files,folderCount,clusterSize))

    # Test 1
    def test1(self):
        # Inputs
        files=("0 123", "2 456", "4 789", "6 012", "8 345")
        folderCount=10
        clusterSize=98

        # Expected output
        output=(73, 0, 34, 0, 93, 0, 86, 0, 47, 0 )

        # Result comparison
        self.assertEqual(output, self.obj_class.calculateWaste(files,folderCount,clusterSize))

    # Test 2
    def test2(self):
        # Inputs
        files=()
        folderCount=5
        clusterSize=100

        # Expected output
        output=(0, 0, 0, 0, 0 )

        # Result comparison
        self.assertEqual(output, self.obj_class.calculateWaste(files,folderCount,clusterSize))

    # Test 3
    def test3(self):
        # Inputs
        files=("0 93842", "1 493784", "2 43212", "3 99327", "4 456209", "5 947243", "6 59348", "7 58237", "8 5834",
               "9 492384", "0 58342", "3 538432", "6 1432", "9 453983", "2 4321", "4 583729", "6 6974", "8 9864",
               "4 43211", "8 38437")
        folderCount=10
        clusterSize=22485

        # Expected output
        output=(27696, 886, 19922, 14306, 18616, 19612, 44671, 9218, 35805, 20488)

        # Result comparison
        self.assertEqual(output, self.obj_class.calculateWaste(files,folderCount,clusterSize))

if __name__ == '__main__':
    unittest.main()
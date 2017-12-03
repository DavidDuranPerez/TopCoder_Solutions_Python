def main():
    # Create the object
    objClass=FolderSize()

    # Call the main method
    print(objClass.calculateWaste(("0 123", "2 456", "4 789", "6 012", "8 345"), 10, 98))


# Main class
class FolderSize():
    # Constructor
    def __init__(self):
        pass

    def calculateWaste(self, files, folderCount, clusterSize):
        # Create the tuple of integers of waste memory
        wasteMemory=[]
        for i in range(0,folderCount):
            wasteMemory.append(0)

        # Loop through the tuple of files
        for file in files:
            pair=file.split() # Split by spaces

            # Get the different values of the pair
            numFolder=int(pair[0])
            fileSize=int(pair[1])

            # Get the waste space
            wasteSpace=clusterSize-fileSize%clusterSize

            # Assign to the corresponding element
            wasteMemory[numFolder]=wasteMemory[numFolder]+wasteSpace

        # Convert the list to tuple
        wasteMemory=tuple(wasteMemory)

        # Return the tuple
        return wasteMemory


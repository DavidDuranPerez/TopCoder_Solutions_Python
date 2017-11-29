def main():
    # Array in an increasing order always
    arr=[2,4,5,6,8,9,10,11,12,15]

    # Create the object
    obj_class = RangeEncoding()

    # Call the main method
    numRanges=obj_class.minRanges(arr)
    print(numRanges)


# Main class
class RangeEncoding():
    # Constructor
    def __init__(self):
        pass

    # Function returning the minimum of possible ranges
    def minRanges(self, arr):
        # Starting with one (which is the minimum)
        numRanges=1
        previous=arr[0]

        # Loop counting the ranges
        for item in arr:
            if item-previous>1:
                numRanges=numRanges+1

            previous=item

        return numRanges


# Call to the main
main()


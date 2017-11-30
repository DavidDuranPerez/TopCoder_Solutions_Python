# Main class
class ChessboardPattern():
    # Constructor
    def __init__(self):
        pass

    def makeChessboard(self, rows, columns):
        strTuple=()
        for i in range(0, rows):
            strRow=""
            for j in range(0, columns):
                if (j+i)%2==0:
                    if rows%2==0:
                        strRow=strRow+"X"
                    else:
                        strRow = strRow + "."
                else:
                    if rows%2==0:
                        strRow=strRow+"."
                    else:
                        strRow = strRow + "X"

            # Create the tuple
            strTuple=strTuple+(strRow,)

        # Return the tuple
        return strTuple



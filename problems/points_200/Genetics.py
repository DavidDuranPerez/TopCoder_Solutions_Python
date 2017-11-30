class Genetics():
    # Constructor
    def __init__(self):
        pass

    def getOffspring(self, g1, g2, dom):
        # Initialization
        offspring=""

        # All the strings have the same length
        for i in range(0,len(g1)):
            # Get if capital or not
            capital1=g1[i].isupper()
            capital2=g2[i].isupper()

            # Different cases
            if capital1 and capital2: # Both capitals
                offspring=offspring+g1[i]
            elif capital1 and not capital2: # First capital, the other not
                if dom[i]=='D':
                    offspring=offspring+g1[i]
                else:
                    offspring=offspring+g2[i]
            elif not capital1 and capital2: # Second capital, the first not
                if dom[i]=='D':
                    offspring=offspring+g2[i]
                else:
                    offspring=offspring+g1[i]
            else: # All are not capital
                offspring = offspring + g1[i]

        # Return the offspring
        return offspring

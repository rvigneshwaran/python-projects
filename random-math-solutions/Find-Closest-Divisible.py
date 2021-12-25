
class FindClosestDivisible:
    
    def __init__(self):
        print("Initializing Components")
        
    def findClosestDivNumber(self,inputNumber,denomNumber):
        quotient = int(inputNumber/denomNumber)
        possible_outcome1 =  inputNumber * quotient
        possible_outcome2 = denomNumber * (quotient + 1) if inputNumber * denomNumber > 0 else denomNumber * (quotient - 1)
        if abs(inputNumber - possible_outcome1) < abs(inputNumber-possible_outcome2):
            return possible_outcome1
        return possible_outcome2

    def findClosestDivisbleNumber(self,inputNumber,denomNumber):
        search_neg_criteria = list(range(inputNumber-denomNumber,inputNumber,1))
        search_pos_criteria = list(range(inputNumber,inputNumber+denomNumber,1))
        foundNegIndex = None
        foundNegNumber = None
        for index,search in enumerate(search_neg_criteria):
            if search % denomNumber == 0:
                foundNegIndex = index
                foundNegNumber = search
        print(str(foundNegNumber) + " is found in the index :: "+str(foundNegIndex))
        foundPosIndex = None
        foundPosNumber = None
        for index,search in enumerate(search_pos_criteria):
            if search % denomNumber == 0:
                foundPosIndex = index
                foundPosNumber = search
        print(str(foundPosNumber) + " is found in the index :: "+str(foundPosIndex))
        if foundPosIndex is not None and foundNegIndex is not None and foundPosIndex < foundNegIndex:
            print("The Closest Divisible Number is :: ",foundPosNumber)
        elif foundPosIndex is not None and foundNegIndex is not None and foundPosIndex > foundNegIndex:
            print("The Closest Divisible Number is :: ",foundNegNumber)
        elif foundPosIndex is None and foundNegIndex is not None:
            print("The Closest Divisible Number is :: ",foundNegNumber)
        elif foundPosIndex is not None and foundNegIndex is None:
            print("The Closest Divisible Number is :: ",foundPosNumber)
        elif foundPosIndex is not None and foundNegIndex is not None and foundPosIndex == foundNegIndex:
            print("The Closest Divisible Number is :: ",foundPosNumber)
            print("The Closest Divisible Number is :: ",foundNegNumber)
        else:
            print("Could Not Find out with this logic !!! ")

instance = FindClosestDivisible()
instance.findClosestDivisbleNumber(45,8)
print(instance.findClosestDivNumber(29,8))
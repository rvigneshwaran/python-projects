manchester_list = ["MARCUS RASHFORD","CRISTIANO RONALDO","BRUNO FERNANDES","FRED","SCOTT MCTOMINAY","JADON SANCHO","ALEX TELLES","HARRY MAGUIRE","VICTO LINDELOF","DIOGO DALOT","DAVID DE GEA","JESSE LINGARD"]

class ListOperations:
    
    def findType(self,inputElement):
        return type(inputElement)
    
    def findlengthOfList(self, inputElement):
        return len(inputElement)
    
    def getSingleElementfromList(self,inputElement,index):
        # Single Element from the list
        if inputElement is not None and len(inputElement)>=index:
            return inputElement[index]
    
    def getRangeOfElementsfromList(self,inputElement,start,end):
        if inputElement is not None and len(inputElement) >= end:
            return inputElement[start,end]
    
    def iterate_list(self,inputElement):
        if inputElement is not None and len(inputElement) > 0:
            # Iterating the values of the list using a while
            index = 0
            while index < self.findlengthOfList(inputElement):
                print("The value of the element is :: ",inputElement[index])
                index += 1
            # iterating the list of elements using a for in 
            for element in inputElement:
                print("The value of the element is :: ",element)
            # Iterating the list with index using the for in
            for index in len(self.findlengthOfList(inputElement)):
                print("The value of the element is :: ",inputElement[index])
            # Iterating the List using the enumerate
            for index,element in enumerate(inputElement):
                print("Element :: "+element+" is present in the index :: "+str(index))
                
    def list_management(self,inputElement):
        if inputElement is not None:
            # Adding Items in to the list
            inputElement.append("PAUL POGBA")
            # Adding muliple elements : Chaining appending
            inputElement.append("JESSE LINGARD").append("LUKE SHAW")
            # Remove an element from the list
            inputElement.remove("LUKE SHAW")
            # Removes the last element in the list
            inputElement.pop()
            # Removes the element by index
            inputElement.pop(3)
            # Negative Index Removal :: Removes the last element
            inputElement.pop(-1)
            # negative Index Removal :Removed the 3rd item from the list
            inputElement.pop(-1)
            # remove all the occurence of the list using __ne__
            inputElement = list(filter(("JESSE LINGARD").__ne__, inputElement))
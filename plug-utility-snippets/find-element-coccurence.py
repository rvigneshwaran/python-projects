from collections import Counter

manchester_list = ["MARCUS RASHFORD","CRISTIANO RONALDO","BRUNO FERNANDES","FRED","SCOTT MCTOMINAY","JADON SANCHO","ALEX TELLES","HARRY MAGUIRE","VICTO LINDELOF","DIOGO DALOT","DAVID DE GEA","JESSE LINGARD","MARCUS RASHFORD","JADON SANCHO","ALEX TELLES","JADON SANCHO","ALEX TELLES","JADON SANCHO","ALEX TELLES","HARRY MAGUIRE","VICTO LINDELOF","DIOGO DALOT","DAVID DE GEA","JESSE LINGARD","DIOGO DALOT","DAVID DE GEA","JESSE LINGARD","MARCUS RASHFORD","JADON SANCHO","ALEX TELLES","JADON SANCHO","ALEX TELLES","JADON SANCHO","ALEX TELLES","HARRY MAGUIRE","VICTO LINDELOF","DAVID DE GEA","JESSE LINGARD","MARCUS RASHFORD","JADON SANCHO","ALEX TELLES","JADON SANCHO"]

class FindElementOccurenceList:
    
    def __init__(self):
        print("Initializing Components !!!")
        
    def apply_line_separators(self,symbol="*",length=100):
        print(symbol*length)
        
    def find_occurences(self):
        search_element = "ALEX TELLES"
        occurence = manchester_list.count(search_element)
        print("Element "+search_element+" has occured in the list :: "+str(occurence)+ " times")
        self.apply_line_separators()
        counter_ins = Counter(manchester_list)
        print("Element "+search_element+" has occured in the list :: "+str(counter_ins[search_element])+ " times")
        self.apply_line_separators()
        print("Check below Occurence of Each Element in the list ::")
        print(counter_ins)
        self.apply_line_separators()
        response_list = [[player,manchester_list.count(player)] for player in set(manchester_list)]
        print("Finding occurence of Each lement in the list using List Comprehension :: ")
        print(response_list)
        self.apply_line_separators()
        
instance = FindElementOccurenceList()
instance.find_occurences()

class CreateCharacterPatterns:
    
    def createHalfPyramid(self,defautChar="*",isIncreasingOrder=False,defaultSize=6,startIndex=0):
        ascii_value = 65
        for indv in range(startIndex,defaultSize):
            indv_char = chr(ascii_value + indv)
            print(indv_char if defautChar == "ASCII" else defautChar,end='')
            for sub_indv in range(startIndex,indv):
                sub_indv_char = chr(ascii_value + sub_indv)
                print(sub_indv_char if isIncreasingOrder else indv_char if defautChar == "ASCII" else defautChar,end='')
            print("")
            
    def createHalfPyramidUsingNumbers(self,isIncreasingOrder=False,defaultSize=6):
        for indv in range(1,defaultSize):
            print(indv,end='')
            for sub_indv in range(1,indv):
                print(sub_indv if isIncreasingOrder else indv,end='')
            print("")
        
    def createHalfPyramidInDecOrder(self,defaultSize=6):
        for item in range(defaultSize,0,-1):
            for sub_item in range(item,0,-1):
                print(str(sub_item) +" ",end="")
            print("")
        
pattern_instance = CreateCharacterPatterns()
'''
*
**
***
****
*****
'''
pattern_instance.createHalfPyramid(startIndex=1)
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
'''
pattern_instance.createHalfPyramid(defautChar="ASCII")

'''
A
BA
CAB
DABC
EABCD
FABCDE
'''
pattern_instance.createHalfPyramid(defautChar="ASCII",isIncreasingOrder=True)
'''
1
22
333
4444
55555
'''
pattern_instance.createHalfPyramidUsingNumbers()
'''
10 9 8 7 6 5 4 3 2 1 
9 8 7 6 5 4 3 2 1 
8 7 6 5 4 3 2 1 
7 6 5 4 3 2 1 
6 5 4 3 2 1 
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
pattern_instance.createHalfPyramidInDecOrder(10)
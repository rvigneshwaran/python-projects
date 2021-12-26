
'''
An anagram is a word or phrase that's formed by rearranging the letters of 
another word or phrase. For example, the letters that make up 
“A decimal point” can be turned into the anagram “I'm a dot in place.
” People mainly make anagrams just for fun, but sometimes 
they're used as pseudonyms or codes.
source: https://www.vocabulary.com/dictionary
'''

import re

class AnagramCheck:
    
    def __init__(self):
        print("Initializing Components")
        
    def check_anagram(self,inputText1,inputText2):
        is_anagram = False
        output_text = None
        if inputText1 is not None and inputText2 is not None:
            mod_inputText1 = re.sub(r"\s+", "", inputText1).lower()
            mod_inputText2 = re.sub(r"\s+", "", inputText2).lower()
            is_anagram = set(mod_inputText1) == set(mod_inputText2)
        output_text = self.get_result(is_anagram,inputText1,inputText2)
        return output_text
            
    def get_result(self,result,inputText1,inputText2):
        text_to_append = inputText1 +" and "+inputText2
        return text_to_append + " are Anagrams" if result else text_to_append + " are NOT Anagrams"
            
instance = AnagramCheck()
print(instance.check_anagram("Fried","Fired"))
print(instance.check_anagram("Astronomer","Moon Starer"))
print(instance.check_anagram("Dormitory","Dirty Room"))
print(instance.check_anagram("Hot Water","Worth Tea"))
print(instance.check_anagram("Country side","No City Dust here"))
print(instance.check_anagram("The Morse Code","Here Comes Dots"))
print(instance.check_anagram("Vacation Time","I Am not Active"))

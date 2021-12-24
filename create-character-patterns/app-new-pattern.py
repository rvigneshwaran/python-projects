
class CreateNewPatterns:
    
    def create_double_size_pyramids(self,pattern_size=4):
        """[Create below type of Pattern]
        ****************
        ************
        ********
        ****
        Args:
            pattern_size (int, optional): [Size of the Tree]. Defaults to 4.
        """
        original_pattern_size = pattern_size
        for index_indv in range(pattern_size,0,-1):
            updated_index = original_pattern_size * pattern_size
            for index,sub_indv in enumerate(range(updated_index)):
                print("* ",end="")
            pattern_size = pattern_size-1
            print("")
            
    def create_magic_pattern(self,pattern_size=4):
        """[Create below type of Pattern]
        3 3 3 2 2 2 1 1 1 
        2 2 2 1 1 1 
        1 1 1
        Args:
            pattern_size (int, optional): [Size of the Tree]. Defaults to 4.
        """
        updated_pattern_size = pattern_size
        original_pattern_size = pattern_size
        for index_indv in range(original_pattern_size,0,-1):
            updated_index = original_pattern_size * updated_pattern_size
            count = 0
            for index,sub_indv in enumerate(range(updated_index)):
                print(str(index_indv)+" ",end="")
                count = count + 1
                if count == original_pattern_size:
                    index_indv = index_indv - 1
                    count = 0
            updated_pattern_size = updated_pattern_size-1
            print("")
            
        
patterns_ins = CreateNewPatterns()
patterns_ins.create_double_size_pyramids()
patterns_ins.create_magic_pattern()
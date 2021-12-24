
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
                print("*",end="")
            pattern_size = pattern_size-1
            print("")
            
        
patterns_ins = CreateNewPatterns()
patterns_ins.create_double_size_pyramids()
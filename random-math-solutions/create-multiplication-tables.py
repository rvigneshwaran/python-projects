class CreateMultiplicationTables:
    
    def __init__(self):
        print("Initialize Table Components")
        
    def create_tables(self,which_table):
        table_list = []
        for mul_element in range(1,11):
            table_list.append(which_table*mul_element)
        return table_list
    
    def create_tables_using_comprehension(self,which_table):
        return [element*which_table for element in range(1,11)]

mult_ins = CreateMultiplicationTables()
print(mult_ins.create_tables(9))
print(mult_ins.create_tables(8))
print(mult_ins.create_tables_using_comprehension(7))
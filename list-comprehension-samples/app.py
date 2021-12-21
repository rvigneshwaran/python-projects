input_list = [23,33,45,23,12,78,56,67,45,89,29,43,23,67]

# Approach of Iterating through the elements in the list
for input in input_list:
    print(input)
    
# Approach of Iterating through the string elements in the lsit
for indv_letter in "ronaldo":
    print(indv_letter)
    
# Using Comprehentions to Iterate through list and string element
created_list = []
# [expression for individual_item in list]
[print(indv_letter) for indv_letter in input_list]
[print(indv_letter) for indv_letter in "ronaldo"]

# Using Conditions with Comprehension
even_number_list = [x for x in range(30) if x % 2 == 0]
print(even_number_list)

# using Methods with Comprehensions for expression component
def evaluate_even(input_num):
    if input_num % 2 == 0:
        return input_num
    
even_number_list = [evaluate_even(x) for x in range(30)]
print(even_number_list)

# Nested Conditions for the evaluation with comprehension
cond_element = [x for x in input_list if x > 40 if x < 60]
print(cond_element)

# Using If Else Directly in Comprehension
num_list = ["Even" if input_ele % 2 == 0 else "Odd" for input_ele in range(15)]
print(num_list)

# Filter None Elements from the list
filtered_list = [x for x in even_number_list if x is not None]
print(filtered_list)

# Make the whole list amazing
sample_list = ["amazing" for x in range(5)]
print(sample_list)

# Apply Prebuild functions with Comprehension
sample_bud = [indv.upper() for indv in "christianoronaldo"]
print(sample_bud)
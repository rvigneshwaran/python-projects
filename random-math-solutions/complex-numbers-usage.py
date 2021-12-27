import cmath

class ComplexNumberManagement:
    
    def __init__(self):
        print("Initializing Components")
        
    def get_complex_number(self,realPart,imaginaryPart):
        return complex(realPart,imaginaryPart)
    
    def perform_operation(self,operation,complexNum1,complexNum2):
        result = None
        if operation == "Addition":
            result = complexNum1 + complexNum2
        elif operation == "Subtraction":
            result = complexNum1 - complexNum2
        elif operation == "Multiplication":
            result = complexNum1 * complexNum2
        elif operation == "Division":
            result = complexNum1 / complexNum2
        print(str(operation) + " on two complex numbers :: "+ str(complexNum1) + " and  "+ str(complexNum2) + " is "+ str(result))
    
instance = ComplexNumberManagement()
'''
The below code shows how when inputs passed to complex function transforms the input in to the complex numbers and how to find the phase of the complex number using cmath module
'''
complex_num  = instance.get_complex_number(2,4)
print("The Complex Number :: ",complex_num)
print("The Real part from the complex num is :: ",complex_num.real)
print("The Imaginary part from the complex num is :: ",complex_num.imag)
print("The phase(z) of the Complex number is :: ",cmath.phase(complex_num))

'''
The below code will help to understand how to transform the complex number in to polar and rectangular
'''
polar_in = cmath.polar(complex_num)
print("The Complex number in polar form is :: ",polar_in)
rect_in = cmath.rect(complex_num.real,complex_num.imag)
print("The Complex number in rectangular form is :: ",rect_in)

'''
To Find the Conjugate of the complex number
'''
conjuc_val = complex_num.conjugate()
print("The Conjugate value of the complex number is :: ",conjuc_val)

'''
How do we perform operations on a Complex Numbers
'''
complex_num1 = instance.get_complex_number(50,100)
complex_num2 = instance.get_complex_number(100,200)
instance.perform_operation("Addition",complex_num1,complex_num2)
instance.perform_operation("Subtraction",complex_num1,complex_num2)
instance.perform_operation("Multiplication",complex_num1,complex_num2)
instance.perform_operation("Division",complex_num1,complex_num2)


import traceback
from num2words import num2words

class HomeLoanEMIAnalyzer:
    def __init__(self):
        print("Initializing Components")
        
    def getInterestAmount(self,principal,rate,timeInYears):
        interest_amount = principal * (pow((1+(rate/100)),timeInYears))
        return interest_amount
    
    def getTotalAmountToBePaid(self,timeInYears,monhly_amount):
        return (timeInYears * 12) * monhly_amount
    
    def getMonthlyEMIAmount(self,principal,rateOfInterest,timeInYears):
        rateOfInterest = rateOfInterest / (12 * 100)
        timeInMonths = timeInYears * 12
        part_component = pow(1 + rateOfInterest, timeInMonths)
        monthlyPayment = (principal * rateOfInterest * part_component) / (part_component - 1)
        return monthlyPayment
    
    def getNumInWords(self,inputNumber):
        return "(" + str(num2words(int(inputNumber))) + " Rupees)"
    
loan_emi_analyzer = HomeLoanEMIAnalyzer()
try:
    principal = input("Enter the Principle Amount :: \n ")
    rateOfInterest = input("Enter the Rate of Interest :: \n ")
    numberOfYears = input("Enter the Number of Years :: \n ")
    principal = float(principal)
    rateOfInterest = float(rateOfInterest)
    numberOfYears = float(numberOfYears)
    emiAmount = loan_emi_analyzer.getMonthlyEMIAmount(principal,rateOfInterest,numberOfYears)
    print("The EMI amount to be paid is :: Rs.{:,}".format(round(emiAmount,2))+loan_emi_analyzer.getNumInWords(emiAmount))
    total_amount = loan_emi_analyzer.getTotalAmountToBePaid(emiAmount,numberOfYears)
    print("The Total that will be paid at the end of "+str(numberOfYears)+" Years is :: Rs.{:,}".format(round(total_amount,2))+loan_emi_analyzer.getNumInWords(total_amount))
    interest_amount_paid = abs(total_amount - principal)
    print("The Total Interest that will be paid at the end of "+str(numberOfYears)+" Years is :: Rs.{:,}".format(round(interest_amount_paid,2))+loan_emi_analyzer.getNumInWords(interest_amount_paid))
except:
    error_response = str(traceback.format_exc())
    print("Excption occured while executing the main method :: "+error_response)
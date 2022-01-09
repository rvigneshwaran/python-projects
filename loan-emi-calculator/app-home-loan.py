import traceback
from num2words import num2words

class HomeLoanEMIAnalyzer:
    def __init__(self):
        print("Initializing Components")
        
    def getInterestAmount(self,principal,rate,timeInYears):
        interest_amount = principal * (pow((1+(rate/100)),timeInYears))
        return interest_amount
    
    def getTotalAmountToBePaid(self,principal,rate,timeInYears):
        interest_amount = self.getInterestAmount(principal,rate,timeInYears)
        total_amount = interest_amount + principal
        return total_amount
    
    def getMonthlyEMIAmount(self,principal,rateOfInterest,timeInYears):
        rateOfInterest = rateOfInterest / (12 * 100)
        timeInMonths = timeInYears * 12
        part_component = pow(1 + rateOfInterest, timeInMonths)
        monthlyPayment = (principal * rateOfInterest * part_component) / (part_component - 1)
        return monthlyPayment
    
loan_emi_analyzer = HomeLoanEMIAnalyzer()
try:
    principal = input("Enter the Principle Amount :: \n ")
    rateOfInterest = input("Enter the Rate of Interest :: \n ")
    numberOfYears = input("Enter the Number of Years :: \n ")
    principal = float(principal)
    rateOfInterest = float(rateOfInterest)
    numberOfYears = float(numberOfYears)
    interest_amount = loan_emi_analyzer.getInterestAmount(principal,rateOfInterest,numberOfYears)
    interest_amount_words = "(" + str(num2words(int(interest_amount))) + ")"
    print("The Interest amount to be paid is :: Rs.{:,}".format(round(interest_amount,2))+interest_amount_words)
    emiAmount = loan_emi_analyzer.getMonthlyEMIAmount(principal,rateOfInterest,numberOfYears)
    emiAmount_words = "(" + str(num2words(int(emiAmount))) + ")"
    print("The EMI amount to be paid is :: Rs.{:,}".format(round(emiAmount,2))+emiAmount_words)
    total_amount = loan_emi_analyzer.getTotalAmountToBePaid(principal,rateOfInterest,numberOfYears)
    total_amount_words = "(" + str(num2words(int(total_amount))) + ")"
    print("The Total that will be paid at the end of "+str(numberOfYears)+" Years is :: Rs.{:,}".format(round(total_amount,2))+total_amount_words)
except:
    error_response = str(traceback.format_exc())
    print("Excption occured while executing the main method :: "+error_response)

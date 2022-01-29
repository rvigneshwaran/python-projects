import traceback
from num2words import num2words

class HomeLoanEMIAnalyzer:
    
    def __init__(self):
        print("Initializing Components")
        
    def getInterestAmount(self,principal,rate,timeInYears):
        """[This Method Intended to calculate the Compound Interest that is paid for the pricipal amount paid considering the total acmount of years,Rate of Interest for the Year]

        Args:
            principal ([float]): [Initial Amount that is borowwed or Invested]
            rate ([float]): [Rate of Interest for One Year]
            timeInYears ([float]): [Total Time Duration Invested/ Borrowed]

        Returns:
            [float]: [Compound Interest for the amount Invested or Borrowed]
        """
        interest_amount = principal * (pow((1+(rate/100)),timeInYears))
        return interest_amount
    
    def getTotalAmountToBePaid(self,timeInYears,monhly_amount):
        """[This Method is Intended to calculate the total amount considering the monthly EMI amount and total time duration]

        Args:
            timeInYears ([float]): [time duration]
            monhly_amount ([float]): [emi amount monthly]

        Returns:
            [float]: [Total Amount Paid during the Duration ]
        """
        return (timeInYears * 12) * monhly_amount
    
    def getMonthlyEMIAmount(self,principal,rateOfInterest,timeInYears):
        """[This Method is Intended to determine the Monthly Installment that is paid as an interest]

        Args:
            principal ([float]): [The Principal amount Invested or borroed]
            rateOfInterest ([float]): [Rate of Interest for each Year]
            timeInYears ([float]): [Total Time Duration]

        Returns:
            [float]: [Monthly EMI Amount]
        """
        rateOfInterest = rateOfInterest / (12 * 100)
        timeInMonths = timeInYears * 12
        part_component = pow(1 + rateOfInterest, timeInMonths)
        monthlyPayment = (principal * rateOfInterest * part_component) / (part_component - 1)
        return monthlyPayment
    
    def getNumInWords(self,inputNumber):
        """[This Method is intended to get the Number in Words]

        Args:
            inputNumber ([Float]): [Input Nummber]

        Returns:
            [str]: [Number in Words]
        """
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
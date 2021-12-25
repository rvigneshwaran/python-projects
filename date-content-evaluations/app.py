from datetime import date
from datetime import datetime
import pandas as pd

class DateDeltaEvaluator:
    
    def __init__(self):
        print("Initializing Components in data delta evaluator")
        
    def getCurrentTime(self):
        return datetime.now()

    def getDifferentBwDateObjects(self,inputDate1,inputDate2):
        deltaInstance = inputDate1 - inputDate2
        return abs(deltaInstance.days)
    
    def getDifferentBwTxtObjects(self,inputDate1,inputDate2):
        date_format = "%m/%d/%Y"
        inputDate1 = datetime.strptime(inputDate1, date_format)
        inputDate2 =  datetime.strptime(inputDate2, date_format)
        deltaInstance = inputDate1 - inputDate2
        return abs(deltaInstance.days)
    
    def getDateDiffUsingPandas(self,inputDate1,inputDate2):
        date_format = "%m/%d/%Y"
        inputDate1 = pd.to_datetime(inputDate1, format=date_format)
        inputDate2 =  pd.to_datetime(inputDate2, format=date_format)
        return abs((inputDate1-inputDate2).days)
    
instanceDate =  DateDeltaEvaluator()
inputDate1 = date(2021,4,29)
inputDate2 = date(2021,12,30)
print("Date Difference of Date Objects :: ")
print(instanceDate.getDifferentBwDateObjects(inputDate1,inputDate2))

inputDate1 = "4/29/2021"
inputDate2 = "12/30/2021"
print("Date Difference of Text Objects :: ")
print(instanceDate.getDifferentBwTxtObjects(inputDate1,inputDate2))

inputDate1 = "4/29/2021"
inputDate2 = "12/30/2021"
print("Date Difference of Text Objects using Pandas :: ")
print(instanceDate.getDateDiffUsingPandas(inputDate1,inputDate2))

# to retrive the current time using the datetime
print("Current Time :: ",instanceDate.getCurrentTime())

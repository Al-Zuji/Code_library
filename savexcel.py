# An example of creating a workbook using openpyxl
# excel-python.py
from openpyxl import Workbook
from time import strftime
Wb_test = Workbook()

while 1:
    Time = strftime("%I:%M:%S %p")
    Date = strftime("%d%m%Y")
    #print(Time)
    print(Date)
    if Time == "12:08:00 AM": #create excel file on set date
        name = strftime("%d%m%Y")
        print(name)
    Wb_test.save("/your/file/path")
    

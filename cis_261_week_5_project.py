#   Jeanne Olsen
#   CIS261 11/5/2022
#   Project Phase 2
def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter the From Date (mm/dd/yyyy) :  ")
    todate = input("Enter the To Date (mm/dd/yyyy) :  ")
    return fromdate, todate    
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
# the following code creates a for loop to read through EmpDetailList and assign values in list to variables
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[0]
        empname = EmpList[0]
        hours = EmpList[0]
        hourlyrate = EmpList[0]
        taxrate = EmpList[0]
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals ["TotEmp"] = TotEmployees
        EmpTotals ["TotHours"] = TotHours
        EmpTotals ["TotGrossPay"] =TotGrossPay
        EmpTotals ["TotTax"] = TotTax
        EmpTotals ["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Number Of Hours: {EmpTotals["TotHours"]}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]}')
    print(f'Total Tax: {EmpTotals["TotTax"]}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]}')

if __name__ == "__main__":
    # COMMENT OUT THE FOLLOWING CODE
    # #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00

    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
EmpDetail = (fromdate, todate, empname, hours, hourlyrate, taxrate)
   #write code to insert fromdate, todate, empname, hours, hourlyrate, and taxrate into list EmpDetail
   #the following code appends the list EmpDetail to the list EmpDetailList
EmpDetailList.append(EmpDetail)

        # COMMENT OUT THE FOLLOWING CODE
        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
printinfo (EmpDetailList)
PrintTotals (EmpTotals)





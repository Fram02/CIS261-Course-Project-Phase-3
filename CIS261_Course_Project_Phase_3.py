def getEmpName():
    empName = input("Enter employee name:  ")
    return empName

def getDatesWorked():
    fromDate = input("Enter Start Date (mm/dd/yyyy):  ")
    toDate = input("Enter End Date (mm/dd/yyyy):  ")
    return fromDate, toDate

def getHoursWorked():
    hours = float(input("Enter amount of hours worked:  "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate:  "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate:  "))
    return taxRate

def calcTaxAndNetPay(hours, hourlyRate, taxRate):
    grossPay = hours * hourlyRate
    incomeTax = grossPay * taxRate
    netPay = grossPay - incomeTax
    return grossPay, incomeTax, netPay

def printInfo(empDetailList):
    totEmployees = 0
    totHours = 0.00
    totGrossPay = 0.00
    totTax = 0.00
    totNetPay = 0.00

    for empList in empDetailList:
        fromDate = empList[0]
        toDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]

        grossPay, incomeTax, netPay = calcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, toDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grossPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")

        totEmployees += 1
        totHours += hours
        totGrossPay += grossPay
        totTax += incomeTax
        totNetPay += netPay

    empTotals["TotEmp"] = totEmployees
    empTotals["TotHrs"] = totHours
    empTotals["TotGrossPay"] = totGrossPay
    empTotals["TotTax"] = totTax
    empTotals["TotNetPay"] = totNetPay

def printTotals(empTotals):
    print()
    print(f"Total Number of Employees: {empTotals['TotEmp']}")
    print(f"Total Hours Worked: {empTotals['TotHrs']}")
    print(f"Total Gross Pay: {empTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {empTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {empTotals['TotNetPay']:,.2f}")

def writeEmployeeInformation(employee):
    file = open("employeeinfo.txt", "a")

    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

def getFromDate():
    valid = False
    fromDate = ""

    while not valid:
        fromDate = input("Enter from date (mm/dd/yyyy):  ")
        if (len(fromDate.split('/')) != 3 and fromDate.upper() != 'ALL'):
            print("Invalid date format:  ")
        else:
            valid = True
    return fromDate

def readEmployeeInformation(fromDate):
    empDetailList = []

    file = open("employeeinfo.txt", "r")
    data = file.readlines()

    condition = True

    if fromDate.upper() == 'ALL':
        condition = False

    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            empDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromDate == employee[0]:
                empDetailList.append([employee[0], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return empDetailList

if __name__ == "__main__":
    empDetailList = []
    empTotals = {}

    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break

        fromDate, toDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        
        print()

        empDetail = [fromDate, toDate, empName, hours, hourlyRate, taxRate]
        writeEmployeeInformation(empDetail)

        print()
        print()
        fromDate = getFromDate()

        empDetailList = readEmployeeInformation(fromDate)

        print()
        printInfo(empDetailList)
        print()
        printTotals(empTotals)



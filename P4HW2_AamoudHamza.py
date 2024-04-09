#Hamza Aamoud
#3/24/2024
#P4HW2
#Totaling pay info for multiple employees using a loop

'''
Enter name
while name NOT "Done"
    Enter hours
    Enter payRate

    If hours <= 40 then
        normPay = hours * rate
        grossPay = normPay
    else
        normPay = rate * 40
        overtimeHours = hour - 40
        overtimePay = overtimeHours * (rate * 1.5)
        grossPay = normPay + overtimePay
    totalOT += overtimePay
    totalReg += normPay
    totalEmp += 1
    totalGross += grossPay
    Display Name
    Display "Hours Worked    Pay Rate   Overtime Hours   Overtime Pay   Regular Pay   Gross Pay"
    Display  hours           payRate    overtimeHours    overtimePay    normPay       grossPay   
    Display "Enter name or "Done" to terminate"
Display "Total number of employees =",totEmp
Display "Total amount of overtime pay =",totOT
Display "Total amount of reuglar pay =",totReg
Display "Total amount of Gross pay =",totGross
'''

totEmp = 0
totOT = 0
totReg = 0
totGro = 0
eName = (input("Enter Employee Name : "))
while eName.lower() != "done":
    worked = float(input("Enter Hours Worked : "))
    rate = float(input("Enter Pay Rate : "))
    otHours = 0
    otPay = 0

    if worked <= 40 :
        normPay = float(worked * rate)
        grossPay = normPay
    elif worked > 40 :
        otHours = float(worked - 40)
        normPay = float(rate * 40)
        otPay = float(otHours * (rate * 1.5))
        grossPay = normPay + otPay

    print("-----------------------------------------------------------------------------------------------")
    print(f'Employee Name : {eName}')
    print("")
    print("Hours Worked     Pay Rate     Overtime Hours     Overtime Pay     Regular Pay     Gross Pay")
    print("-----------------------------------------------------------------------------------------------")
    print(f'{worked:<17}${rate:<12.2f}{otHours:<19}${otPay:<16.2f}${normPay:<15.2f}${grossPay:.2f}')

    totEmp += 1
    totOT += otPay
    totReg += normPay
    totGro += grossPay

    print(f'Enter employee name or "Done" to terminate :')
    eName = (input("Enter Employee Name : "))
    print("")

print("-----------------------------------------------------------------------------------------------")
print("Total number of employees entered:   $",totEmp)
print(f'Total amount paid for overtime:      ${totOT:.2f}')
print(f'Total amount paid for regular hours: ${totReg:.2f}')
print(f'Total amount paid in gross:          ${totGro:.2f}')
#Hamza Aamoud
#3/24/2024
#P3HW2
#Calculating pay using if statements for overtime

'''
Enter name
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

Display Name
Display "Hours Worked    Pay Rate   Overtime Hours   Overtime Pay   Regular Pay   Gross Pay"
Display  hours           payRate    overtimeHours    overtimePay    normPay       grossPay   
'''

#Inputs/variables
eName = (input("Enter Employee Name : "))
worked = float(input("Enter Hours Worked : "))
rate = float(input("Enter Pay Rate : "))
otHours = 0
otPay = 0

#Calculation
if worked <= 40 :
    normPay = float(worked * rate)
    grossPay = normPay
elif worked > 40 :
    otHours = float(worked - 40)
    normPay = float(rate * 40)
    otPay = float(otHours * (rate * 1.5))
    grossPay = normPay + otPay

#Output
print("-----------------------------------------------------------------------------------------------")
print(f'Employee Name : {eName}')
print("")
print( "Hours Worked     Pay Rate     Overtime Hours     Overtime Pay     Regular Pay     Gross Pay")
print("-----------------------------------------------------------------------------------------------")
print(f'{worked:<17}${rate:<12.2f}{otHours:<19}${otPay:<16.2f}${normPay:<15.2f}${grossPay:.2f}')

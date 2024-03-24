#Hamza Aamoud
#3/24/2024
#P3HW2
#Calculating pay using if statements for overtime

'''

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
print("------------------------------------------------------------------------------------------------------------------")
print(f'Employee Name : {eName}')
print("------------------------------------------------------------------------------------------------------------------")

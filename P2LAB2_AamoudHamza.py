#Hamza Aamoud
#2/27/2024
#P2LAB2
#Calculating rpoducts and averages

num1 = float(input("Enter first number:  "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number:  "))
num4 = float(input("Enter fourth number: "))

prod = num1 * num2 * num3 * num4
avg = (num1 + num2 + num3 + num4)/4

print("The rounded product of your numbers = "f'{prod:.0f}')
print("The rounded average of your numbers = "f'{avg:.0f}')
print("The product of your numbers to the thousandth place = "f'{prod:.3f}')
print("The average of your numbers to the thousandth place = "f'{avg:.3f}')
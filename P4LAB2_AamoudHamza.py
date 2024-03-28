#Hamza Aamoud
#3/26/24
#P4LAB2
#Using range function

num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter a target number: "))


while num1 > num2:
    print("The first number must be smaller!!!")
    num1 = int(input("Enter a starting number: "))
    num2 = int(input("Enter a target number: "))

for number in range(num1, num2+1,5):
    print(number)
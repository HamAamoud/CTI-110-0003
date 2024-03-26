#Hamza Aamoud
#3/26/24
#P4LAB2
#Using range function

num1 = int(input("Enter a starting number: "))
num2 = int(input("Enter a target number: "))

l = 1
while l == 1:
    if num1 < num2:
        l = 0
        while num1 <= num2:
            print(num1)
            num1 += 5
    else:
        print("The first number must be smaller!!!")
        num1 = int(input("Enter a starting number: "))
        num2 = int(input("Enter a target number: "))
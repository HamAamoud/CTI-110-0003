#Hamza Aamoud
#3/14/2024
#P3LAB
#Calculating andprinting exact change

changeAmount = int(input("Enter the amount of change : "))
dollars = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

if changeAmount <= 0:
    print("No change owed")

while changeAmount >= 100:
    changeAmount -=100
    dollars +=1
while changeAmount >= 25:
    changeAmount -=25
    quarters +=1
while changeAmount >= 10:
    changeAmount -=10
    dimes +=1
while changeAmount >= 5:
    changeAmount -=5
    nickels +=1
while changeAmount >= 1:
    changeAmount -=1
    pennies +=1

if dollars > 1:
    print(dollars, "Dollars")
elif dollars == 1:
    print(dollars, "Dollar")

if quarters > 1:
    print(quarters, "Quarters")
elif quarters == 1:
    print(quarters, "Quarter")

if dimes > 1:
    print(dimes, "Dimes")
elif dimes == 1:
    print(dimes, "Dime")

if nickels > 1:
    print(nickels, "Nickels")
elif nickels == 1:
    print(nickels, "Nickel")

if pennies > 1:
    print(pennies, "Pennies")
elif pennies == 1:
    print(pennies, "Penny")
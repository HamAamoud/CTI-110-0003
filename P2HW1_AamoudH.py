#Hamza Aamoud
#3/3/2024
#P2HW2
#Alligning print elements
'''
Declare Real budget, gas, accom, food, expenses, remaining
Declare String dest
Display "Enter your budget: "
Input budget
Display "Enter your destination: "
Input dest
Display "How much do you expect to spend on gas: "
Input gas
Display "Enter accomodation costs: "
Input accom
Display "Enter cost of food: "
Input food
expenses = gas + food + accom
remaining = budget - expenses
Display "Budget = ",budget
Display "Destination = ",dest
Display "Gas cost = ",gas
Display "Accomodation cost = ",accom
Display "Food cost = ",food
Display "Remaining balance = ",remaining
'''
print()
print("This program calculates travel expenses")
budget = float(input("Enter your budget: "))
dest = input("Enter your destination: ")
gas = float(input("Enter expected gas cost: "))
food = float(input("Enter expected food cost: "))
accom = float(input("Enter expected accomodation cost:"))
expenses = gas + food + accom
print()
print("-------Travel Expenses-------")
print("Destination :", "{:>???}" .format(dest))
print("Budget =", "{:>???.2f}" .format(budget))
print("Gas cost =", "{:>???.2f}" .format(gas))
print("Accomodation cost =", "{:>???.2f}" .format(accom))
print("Food cost =", "{:>???.2f}" .format(food))
remaining = budget - expenses
print("-----------------------------")
print("Remaining balance =", "{:>???.2f}" .format(remaining))

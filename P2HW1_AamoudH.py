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
print(f'Destination          = {dest}')
print(f'Budget               = ${budget:.2f}')
print(f'Gas cost             = ${gas:.2f}')
print(f'Accomodation cost    = ${accom:.2f}')
print(f'Food cost            = ${food:.2f}')
remaining = budget - expenses
print("-----------------------------")
print(f'Remaining balance    = ${remaining:.2f}')

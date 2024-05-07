#Hamza Aamoud
#2/27/2024
#P2LAB1
#Coding mathematical calculations and displaying them

gas_mile = float(input("Enter you cars gas milage: "))
gas_cost = float(input("Enter the cost of gas: "))

cost_20 = 20 / gas_mile * gas_cost
cost_75 =  75 / gas_mile * gas_cost
cost_500 = 500 / gas_mile * gas_cost

print("The cost to drive 20 miles is  $"f'{cost_20:.2f}')
print("The cost to drive 75 miles is  1$"f'{cost_75:.2f}')
print("The cost to drive 500 miles is $"f'{cost_500:.2f}')
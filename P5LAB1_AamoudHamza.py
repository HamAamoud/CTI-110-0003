#Hamza Aamoud
#4/16/24
#P5LAB
#User-defined functions

#Function to determine change returned to customer
def disperse_change(change):
        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                
    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")


def show_avail_items(dictionary):
    print(f"{'Grocery Item':<15}{'Price'}")
    print("--------------------------------------")
    for key, value in dictionary.items():
        print(f"{key:<15}${value:.2f}")
    print("--------------------------------------")

def add_items(dictionary):
    cart = []
    print("Welcome to Grocery Checkout")
    print()
    choice = input("Enter an item to add to the cart or type 'end' to stop : ").lower()
    while choice != "end":
            if choice in dictionary.keys():
                cart.append(choice)
            else:
                 print(f'{choice} is not in stock')
            choice = input("Enter an item to add to the cart or type 'end' to stop : ").lower()
    print("----------------------------")
    return cart

def calc_totals(cart,dictionary):
    subTotal = 0
    for item in cart:
        subTotal += dictionary[item]
    tax = subTotal * .07
    finTotal = subTotal + tax
    return subTotal, tax, finTotal

#Main Function
def main():
    #Test it
    food_dictionary = {'apples':3.69, 'berries':4.00, "chocolate":2.89 ,"turkey":6.99 ,"cheese":4.00 ,"pepsi":7.89 ,"egg":3.50 ,"bread":3.00 }
    show_avail_items(food_dictionary)

    cart = add_items(food_dictionary)
    
    print("Items in your cart:")
    for item in cart:
        print(f'{item}        ${food_dictionary[item]:.2f}')
    print("--------------------------")
    subTotal, tax, finTotal = calc_totals(cart, food_dictionary)
    print(f'Subtotal      ${subTotal:.2f}')
    print()
    print(f'Tax           ${tax:.2f}')
    print()
    print(f'Final Total   ${finTotal:.2f}')
    print()
    payment = float(input("How much money are you putting in? : "))
    change = payment - finTotal
    change = change * 100
    print()
    print("Your change is : ")
    disperse_change(change)


#Call the main function
main()
        


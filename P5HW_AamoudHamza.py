#Hamza Aamoud
#4/18/2024
#P5HW
#Using functions and generating random nums
import random

def endProg():
    print("Program Ended")

def ranNums():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    return num1, num2

def corAns(guesses):
    print("Congrats You Got it Right!!!")
    print("Number of Guesses :", guesses)
    print()


def addNums():
    answer = 3000
    num1 , num2 = ranNums()
    print("    ",num1)
    print("   +",num2)
    print()
    solution = num1 + num2
    guesses = 0
    while answer != solution:
        answer = int(input("Enter answer : "))
        guesses +=1
        if answer == solution:
            corAns(guesses)
        elif answer > solution:
            print("Incorrect : Answer too high")
        elif answer < solution:
            print("Incorrect : Answer too low")
    
    

def subNums():
    answer = 3000
    num1 , num2 = ranNums()
    print("    ",num1)
    print("   -",num2)
    print()
    solution = num1 - num2
    guesses = 0
    while answer != solution:
        answer = int(input("Enter answer : "))
        guesses +=1
        if answer == solution:
            corAns(guesses)
        elif answer > solution:
            print("Incorrect : Answer too high")
        elif answer < solution:
            print("Incorrect : Answer too low")

def menu():
    choice = 0
    while choice != 3:
        print("MAIN MENU")
        print("---------------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print()
        choice = int(input("Please choose one of the menu options : "))
        if choice == 1:
            addNums()
        elif choice == 2:
            subNums()
        elif choice == 3:
            endProg()
        else:
            print("Invalid choice")
    

def main():
    print("Welcome to Math Quiz")
    menu()

main()

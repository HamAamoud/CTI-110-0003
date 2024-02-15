'''
#converting datatype
weekly_rate = input("Enter your weekly pay: ")

weekly_rate = float(weekly_rate)

print("Your weekly pay is:", weekly_rate, "dollars")

#See what the datatype is for a variable
print(type(weekly_rate))

#Display biweekly pay
print("Every two weeks you make","$" + str(weekly_rate * 2))
''' 
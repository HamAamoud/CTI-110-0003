#Hamza Aamoud
#3/17/2024
#P3HW1
#Fix errors in code

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1,mod_2,mod_3,mod_4,mod_5,mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# determine letter grade for average

print('------Results------')
print("Lowest Grade:     ",low)
print("Higfhest Grade:   ",high)
print("Sum of Grades:    ",sum)
print(f'Average:           {avg:.2f}')
print('-------------------')
if avg >= 90:
    print('Your grade is: A')
else:
    if avg >= 80:
        print('Your grade is: B')
    else:
        if avg >= 70:
            print('Your grade is: C')
        else:
            if avg >= 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F') # TO DO: finish this






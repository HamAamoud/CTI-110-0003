#Hamza Aamoud
#3/5/24
#P2HW2
#Taking user input and creating a list

#Take module 1-6 test score inputs from user
#Insert test scores into scores list
#Find list min,max,sum, and length
#Divide sum but length to find average
#Display min, max, sum, and average

mod1 = float(input("Enter Module 1 Test Score : "))
mod2 = float(input("Enter Module 2 Test Score : "))
mod3 = float(input("Enter Module 3 Test Score : "))
mod4 = float(input("Enter Module 4 Test Score : "))
mod5 = float(input("Enter Module 5 Test Score : "))
mod6 = float(input("Enter Module 6 Test Score : "))

scores = []
scores .append(mod1)
scores .append(mod2)
scores .append(mod3)
scores .append(mod4)
scores .append(mod5)
scores .append(mod6)

low = min(scores)
high = max(scores)
sum = sum(scores)
length = len(scores)
avg = sum / length

print()
print("-----Results-----")
print(f'Lowest Grade:   {low}')
print(f'Highest Grade:  {high}')
print(f'Sum of Grades:  {sum}')
print(f'Average:        {avg}')
print("-----------------")
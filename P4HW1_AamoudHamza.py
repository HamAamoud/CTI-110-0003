#Hamza Aamoud
#3/28/2024
#P4HW1
#Taking user input using a loop and finding the average

num = int(input("How many grade would you like to enter? : "))
scores = []
for count in range (num):
    grade = float(input(f'Enter a grade #{count+1} : '))
    while (grade > 100 or grade <0):
        print("Grade is invalid")
        grade = float(input("Enter valid grade"))
    scores.append(grade)

print("-------------Results--------------")
print(f'Lowest score    : {min(scores)}')
scores.remove(min(scores))
avg = sum(scores)/len(scores)
print(f'Modified List   : {scores}')
print(f'Scores Average  : {(sum(scores)/len(scores)):.2f}')

if avg >=90:
    print("Grade : A")
elif avg >=80:
    print("Grade : B")
elif avg >= 70:
    print("Grade : C")
elif avg >= 60:
    print("Grade : D")
else:
    print("Grade : F")

print("----------------------------------")
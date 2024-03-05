#Making lists in python
nums = []

#Add values to the list (hard coded)
nums .append(5)
nums .append(5.785)
nums .append(63.0)
 
print(nums)

num1 = float(input("Enter a float value"))

#Add variables to the list
nums .append(num1)
nums .append(float(input("Enter a float value")))

print(nums)

#Get the sum of all values in the list
list_sum = nums[0] + nums[1] + nums[2] #very slow
list_sum = sum(nums)
print(list_sum)

#Get the minimum value from the list
list_min = min(nums)
print(list_min)

#Get the maximum value from the list
list_max = max(nums)
print(list_max)

#Get the length of the list
list_len = len(nums)
print(list_len)

#Get list average
list_avg = list_sum / list_len
print(list_avg)
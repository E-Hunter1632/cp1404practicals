"""List Exercises"""
# 1st Exercise: Getting numbers and printing facts about them.
amount = 5
numbers = []
for item in range(amount):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("The first number is: ", numbers[0])
print("The last number is: ", numbers[-1])
print("The smallest number is: ", min(numbers))
print("The largest number is: ", max(numbers))
print("The average of numbers is: ", sum(numbers) / 2)

# 2nd Exercise:


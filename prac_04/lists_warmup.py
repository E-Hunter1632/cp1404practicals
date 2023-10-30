numbers = [3, 1, 4, 1, 5, 9, 2]
# Answering questions:
# 1) numbers[0] gives '3'
# 2) numbers[-1] gives '2'
# 3) numbers[3] gives '1'
# 4) numbers[:-1] gives ['3', '1', '4', '1', '5', '9']
# 5) numbers[3:4] gives '1'
# 6) 5 in numbers gives 'True'
# 7) 7 in numbers gives 'False'
# 8) "3" in numbers gives 'False'
# 9) numbers + [6, 5, 3] gives [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
numbers[0] = "Ten"
print(numbers)

numbers[-1] = 1
print(numbers)

print(numbers[2:])

print(9 in numbers)

# TASK 1:
name = input("Enter your name: ")
filename = "name.txt"
out_file = open(filename, 'w')
print(name, file=out_file)
out_file.close()

# TASK 2:
in_file = open(filename, 'r')
for line in in_file:
    print(f"Your name is {line}")
in_file.close()

# TASK 3:
in_file = open("numbers.txt", 'r')
num_1 = int(in_file.readline())
num_2 = int(in_file.readline())
result = num_1 + num_2
print(f"Result is {result}")
in_file.close()


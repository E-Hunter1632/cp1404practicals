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

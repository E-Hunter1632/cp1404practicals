# TASK 1:
name = input("Enter your name: ")
filename = "name.txt"
out_file = open(filename, 'w')
print(name, file=out_file)
out_file.close()


# a)
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

# b)
for i in range (20, 0, -1):
    print(i, end=' ')
print()

# c)
num_of_stars = int(input("Enter number of stars: "))
for i in range(num_of_stars):
    print('*', end='')
print()

# d)
num_of_stars = int(input("Enter number of stars: "))
for i in range(1, num_of_stars + 1):
    print('*' * i)
print()

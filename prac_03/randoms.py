"""'Random' function testing and tasks"""
# ---------------------------------------------------------------------------------
# help(random.randint)
# Help
# on
# method
# randint in module
# random:
# randint(a, b)
# method
# of
# random.Random
# instance
# Return
# random
# integer in range[a, b], including
# both
# end
# points.
#
# help(random.randrange)
# Help
# on
# method
# randrange in module
# random:
# randrange(start, stop=None, step=1, _int= <
#
#
# class 'int'> ) method of random.Random instance
# Choose a random item from range(start, stop[, step]).
#
# This fixes the problem with randint() which includes the
# endpoint; in Python this is usually not what you want.
# ---------------------------------------------------------------------------------

# PRAC TASK:
# import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# ANSWERS FROM QUESTIONS FROM PRAC TASKS:
# Line 1 -> Smallest number can be '5', largest '20'
# Line 2 -> Smallest number can be '3', largest '9', Can not produce a '4' due to the step
# Line 3 -> Large decimal, smallest can be '2.5', largest can be '5.5'

# TASK FROM PRAC:
import random
print(random.randint(1, 100))


"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# -------------------------------------------------------------------------------
# ANSWERING QUESTIONS FROM PRAC TASK:
# 1) ValueError will occur when input is not an integer.
# 2) ZeroDivisionError will occur when denominator input is a zero.
# 3) To avoid the possibility of a ZeroDivisionError, the code would need to add,
# add an if statement to make sure that if a zero is entered, to not even proceed,
# to avoid the error even being passed to begin with.

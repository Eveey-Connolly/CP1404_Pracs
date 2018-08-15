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

# The ValueError will occur when a non-integer character is entered by the user
# The ZeroDivisionError will occur when 0 is entered for the denominator by the user
# Could you change the code to avoid the possibility of a ZeroDivisionError? while loop until the integer doesnt equal 0 in the denominator

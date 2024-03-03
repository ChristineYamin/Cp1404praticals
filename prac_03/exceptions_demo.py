"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occuur when user input is invalid ,for example alphabets.

2. When will a ZeroDivisionError occur?
A ZeroDivisionERror will occur when user input is zero instead of other integers.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, we could change the code by using random.uniform.
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
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

# 1.When will a ValueError occur?
# When type the value which is not numbers.

# 2.When will a ZeroDivisionError occur?
# When type 0 in denominator or type 0 in numerator and denominator.

# 3.Could you change the code to avoid the possibility of a ZeroDivisionError?
# if you could figure out the answer to question 3, then make this change now


numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

while numerator == 0 or denominator == 0:
    # while numerator or denominator == 0:
    # while not numerator or denominator == 0:
    print("Invalid")
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

fraction = numerator / denominator
print(fraction)
print("Finished.")

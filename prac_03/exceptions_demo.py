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
    if denominator == 0:
        print("Denominator cannot be zero. Please enter a non-zero value.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")



"""
1.A ValueError will occur if the input for denominator or numerator was entered in float or other which the user should 
enter the integer.

2.A ZeroDivisionError will occur when the user enters 0 for the denominator.

3.Yes, by avoiding  the possibility of a ZeroDivisionError, we can add a condition to check if the denominator is 0 
before  dividing. If the denominator is zero we can tell the user to enter the non zero value.
"""


"""
Write a program to calculate the value of a function
f(a, b) = 3(a + b)^3 + 275b^2 - 127a - 41 by entered integer values
a and b.

Input data format
The input to the program is two integers, each on a separate line. The first line is the value
a, in the second line - the value of b.

Output format
The program should display the value of the function according to the entered numbers
a and b.
"""
a, b = int(input()), int(input())
print(3*(a+b) ** 3+275*b**2 - 127*a - 41)
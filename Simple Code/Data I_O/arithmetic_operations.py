"""
Write a program that calculates the sum, 
difference, and product of two integers entered from the keyboard.

Input data format
The input to the program is two integers, each on a separate line.

Output format
The program should print the sum, difference, and product of the entered numbers, each on a separate line.
"""
a, b = int(input()), int(input())
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)
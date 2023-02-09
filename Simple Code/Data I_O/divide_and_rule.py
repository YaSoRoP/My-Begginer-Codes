"""
Write a program that reads a positive integer
x displays a sequence of numbers
x, x2, x3, x4, x5 separated by three dashes.

Input data format
The input to the program is a positive integer.

Output format
The program should display the text according to the condition of the problem.
"""
a = int(input())
print(a, a*2, a*3, a*4, a*5, sep="---")
"""
Write a program to display three consecutive numbers on the screen, 
each on a separate line. The first number is entered by the user, 
the remaining numbers are calculated in the program.

Input data format
The input to the program is a single integer.

Output format
The program should display three consecutive numbers in accordance with the 
condition of the problem.
"""
number = int(input())
print(number, number+1, number+2, sep="\n")
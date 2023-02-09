"""
Write a program that reads a delimiter string and three lines and then outputs 
the specified lines separated by a delimiter.

Input data format
The input to the program is a delimiter line and three lines, each on a separate line.

Output format
The program should display the entered three lines separated by a separator.
"""
symbol, line1, line2, line3 = input(), input(), input(), input()
print(line1, line2, line3, sep=symbol)
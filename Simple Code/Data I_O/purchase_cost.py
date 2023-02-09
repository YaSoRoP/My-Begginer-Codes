"""
Write a program that calculates the cost of three computers, consisting of a monitor, 
a system unit, a keyboard, and a mouse.

Input data format
The input to the program is four integers, each on a separate line. The first line is the cost of the monitor, the second line is the cost of the system unit, the third line is the cost of the keyboard, and the fourth line is the cost of the mouse.

Output format
The program should display one number - the cost of the purchase (of three computers).
"""
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(3*(a+b+c+d))
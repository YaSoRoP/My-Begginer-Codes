"""
Write a program to find the digits of a four digit number.

Input data format
The input to the program is a positive four-digit integer.

Output format
The program should display the text in accordance with the condition of the problem.
"""
number = int(input())
print("Цифра в позиции тысяч равна", number//1000, sep=" ")
print("Цифра в позиции сотен равна", (number//100) % 10, sep=" ")
print("Цифра в позиции десятков равна", (number//10) % 10, sep=" ")
print("Цифра в позиции единиц равна", number%10, sep=" ") 
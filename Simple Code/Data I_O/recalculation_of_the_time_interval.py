"""
Write a program to convert a time interval 
given in minutes to a value expressed in hours and minutes.

Input data format
The input to the program is an integer - the number of minutes.

Output format
The program should display the text in accordance with the condition of the problem.
"""
minute = int(input())
print(f"{minute} мин - это {minute//60} час {minute%60} минут.")
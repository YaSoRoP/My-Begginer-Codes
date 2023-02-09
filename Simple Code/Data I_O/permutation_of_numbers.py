"""
Given a three-digit number abc, 
in which all digits are different. 
Write a program that prints the six numbers formed 
by permuting the digits of a given number.

Input data format
The input to the program is a positive three-digit integer, 
all digits of which are different.

Output format
The program should display six numbers formed by rearranging the digits 
of a given number in the following order: abc, acb, bac, bca, cab, cba.
"""
n = int(input())
x = n//100
y = (n//10)%10
c = n%10
print(x,y,c, sep=("")) 
print(x,c,y, sep=(""))
print(y,x,c, sep=(""))
print(y,c,x, sep=(""))
print(c,x,y, sep=(""))
print(c,y,x, sep=(""))
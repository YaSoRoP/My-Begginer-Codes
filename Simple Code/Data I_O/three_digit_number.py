"""
Write a program that calculates the sum 
and product of the digits of a positive three-digit number.

Input data format
The input to the program is a positive three-digit number.

Output format
The program should display two numbers with explanatory text: 
the sum of the digits and the product of the digits.
"""
num = int(input())
sum1, sum2, sum3 = num%10, (num//10) % 10, num//100
print("Сумма цифр =", sum1+sum2+sum3)
print("Произведение цифр =", sum1*sum2*sum3)
"""
Write a program that reads an integer and then prints the next and previous 
integer with explanatory text.

Input data format
The input to the program is an integer.

Output format
The program should display the text according to the condition of the problem.
"""
num = int(input())
print("Следующее за числом", num, "число:", num+1)
print("Для числа", num, "предыдущее число:", num-1)
"""
The compartment car has 9 compartments with four seats for passengers 
in each. Write a program that determines the number of the compartment 
in which the seat with the given number is located 
(numbering of seats is continuous, starting from 1).

Input data format
The input to the program is an integer - a place with a given number in the car.

Output format
The program should display one number - the number of the compartment 
in which the specified place is located.
"""
print((int(input())-1) // 4+1)
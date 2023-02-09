"""
Write a program that calculates the volume of a cube and its total surface area, 
given the value of the length of the edge.

Input data format
The input to the program is a single integer - the length of the edge.

Output format
The program should display text and numbers in accordance with the condition of the problem.

Note. The volume of a cube and the total surface area can be calculated using the formulas
V=a^3, S=6a^2
"""
lenght_rib = int(input())
print("Объём =", lenght_rib**3)
print("Площадь полной поверхности =",6*lenght_rib**2)

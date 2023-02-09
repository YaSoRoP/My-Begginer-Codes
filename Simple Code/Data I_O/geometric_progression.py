"""
A geometric progression is a sequence of numbers b1, b2, ....bn each of which, starting with 
b2, obtained from the previous one by multiplying by the same constant number
q(denominator of progression)

Input data
The program receives three integers as input:
b1, q and n, each on a separate line.

Output
The program should output
n-th member of a geometric progression.
"""
b1, q, n = int(input()), int(input()), int(input()),
print(b1 * q**(n-1))
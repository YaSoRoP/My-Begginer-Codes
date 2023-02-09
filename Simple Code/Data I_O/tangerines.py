"""
n schoolchildren divide k tangerines equally, 
the non-divisible remainder remains in the basket. 
How many whole tangerines will each student get? 
How many whole tangerines will be left in the basket?

Input data format
The program receives two integers as input: the number of 
schoolchildren and the number of tangerines, each on a separate line.

Output format
The program should print two numbers: the number of tangerines that each 
student will get, and the number of tangerines that will remain in the basket, 
each on a separate line.
"""
n, k = int(input()), int(input())
print(k // n)
print(k % n)
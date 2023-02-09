"""
inevitability itself
The Mad Titan Thanos has collected all 6 Infinity 
Stones and intends to wipe out half the population
of the universe with a snap of his fingers. 
Moreover, if the population of the Universe is an odd number, 
then the titan will show mercy and round the number of survivors up. 
Help the Avengers count the number of survivors.

Input data format
The input is an integer
n is the population of the universe.

Output format
The program should print a single number - the number of survivors.
"""
number = int(input())
print(number - (number//2))
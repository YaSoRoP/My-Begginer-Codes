"""
Write a program that greets the user by displaying the word "Hello" 
(without the quotes), followed by a comma and a space, followed by the user's 
name and an exclamation point.

Input data format
The input to the program is one string - the username.

Output format
The program should display the text in accordance with the condition of the problem.

Note 1: There must be no spaces before the exclamation mark.

Note 2: Use the optional end parameter.
"""
name = input()
print("Привет,",name, end="!")
#Write a Python program that prompts the user to input three digits (0-9) and checks if the entered digits are valid. If the digits are valid, the program generates all possible combinations of these three digits and prints them. Each combination is formed by arranging the digits in different orders. If the input is not valid (digits are not between 0 and 9), the program should display as "Invalid".
from itertools import permutations

def is_valid_digit(d):
	return 0<= d <=9

digit1 = int(input("digit1 (0-9): "))
digit2 = int(input("digit2 (0-9): "))
digit3 = int(input("digit3 (0-9): "))

if is_valid_digit(digit1) and is_valid_digit(digit2) and is_valid_digit(digit3):
	digits = [digit1, digit2, digit3]

	for perm in sorted (set(permutations(digits))):
		print("".join(map(str, perm)))
else:
	print("Invalid")

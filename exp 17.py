#Write a program to count the number of vowels using sets in a given string.
"""def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
#str = input()
vowel_count(str)"""

def count_vowels(s):
	vowels = {'a','e','i','o','u','A','E','I','O','U'}
	return sum(1 for char in s if char in vowels)
string = input()
print(count_vowels(string))

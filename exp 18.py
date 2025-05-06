#Write a Python program to find whether a given string is a palindrome or not.
def is_palindrome(s):
	return s == s[::-1]
string = input()
if is_palindrome(string):
	print("palindrome")
else:
	print("not a palindrome")

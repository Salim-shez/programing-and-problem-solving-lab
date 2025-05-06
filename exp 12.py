#Write a python program to print factorial of given number.
# Type Content here...
n= int(input('Enter a number : '))
if n<0:
	print('Enter a positive number')
else:
	fact = 1
	for i in range(1,n+1):
		fact *= i
	print(f"Factorial of given number is : {fact}")

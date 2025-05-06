# Write a Python program to check if a given year is a leap year or not.
year = int(input("Enter a year: "))
if year %4 ==0:
	print("%d is a leap year" % year)
else:
	print("%d is not a leap year" % year)

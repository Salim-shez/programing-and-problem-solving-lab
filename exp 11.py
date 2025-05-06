# Write a Python program that prompts the user to input a date (year, month, and day) and checks if it is a valid date. If the entered date is valid, the program should increment the date by one day and display the incremented date. The program should take into account leap years when determining the number of days in February.

def is_leap_year(year):
	return(year % 4==0 and year % 100 !=0) or (year % 400 == 0)


def gets_days_in_month(year,month):
	if month in {1,3,4,5,8,10,12}:
		return 31
	elif month in {4,6,9,11}:
		return 30
	elif month == 2:
		return 29 if is_leap_year(year) else 28
	return 0

def increment_data(year,month,day):
	days_in_month = gets_days_in_month(year,month)

	if month < 1 or month > 12 or day < 1 or day > days_in_month:
		print("invalid")
		return

	day += 1
	if day>days_in_month:
		day=1
		month+=1
		if month>12:
			month =1
			year+=1


	print("valid")
	print(f"incremented date: {year}-{month:02d}-{day:02d}")

y = int(input('year: '))
m = int(input("month: "))
d = int(input("day: "))

increment_data(y,m,d)

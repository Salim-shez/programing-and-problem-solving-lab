# Write a program to calculate the area of a circle and print the result as shown in the displayed test cases.
def calculate_circle_area(radius):
	pi = 3.14
	area = pi * radius**2
	return area

radius = float(input("Enter the radius : "))
if 0.0 <= radius <=100.0:
	area = calculate_circle_area(radius)
	print("Area of circle = {:.6f}".format(area))
else:
	print("Enter a positive value upto 100")


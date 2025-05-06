# Write a Python program to calculate the average marks for 5 subjects. The program should prompt the user to input the marks for each subject. After receiving the input, it should compute the average marks and then determine the corresponding grade based on the following grading system:

s1 = float(input('subject 1: '))
s2 = float(input('subject 2: '))
s3 = float(input('subject 3: '))
s4 = float(input('subject 4: '))
s5 = float(input('subject 5: '))

avg = (s1+s2+s3+s4+s5)/5

print('Average Marks:',format(avg, '.2f'))
if(avg>=90 and avg<=100):
	print('Grade: A')
elif (avg>=80 and avg<=89):
	print('Grade: B')
elif(avg>=70 and avg<=79):
	print('Grade: C')
elif(avg>=60 and avg<=69):
	print('Grade: D')
elif (avg<60):
	print('Grade: F')

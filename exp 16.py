#Write a Python program that prints prime numbers less than n which represents the upper limit.
def id_prime(mun):
	if num < 2:
		return False
	for i in range (2, int (num ** 0.5) + 1):
		if num % i==0:
			return False
	return True

n = int (input("Enter upper limit: "))

for num in range(2,n):
	if id_prime(num):
		print(num)

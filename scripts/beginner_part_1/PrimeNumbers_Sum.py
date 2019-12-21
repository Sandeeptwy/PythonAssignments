import math
import time

def isPrime(num):
	if num==1:
		return False
	if num==2:
		return True
	if num>2 and num%2==0:
		return False

	max_divisor = math.floor(math.sqrt(num))
	# print(str(math.sqrt(num))

	for n in range(3,1+max_divisor,2):
		if num % n == 0:
			# print(str(n)+" Number "+str(num)+" is not a prime number")
			return False
	return True

sumOfPrime = 0

for a in range(2,2000000):
	if(isPrime(a)==True):
		sumOfPrime+=a

print(sumOfPrime)
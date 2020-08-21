# Rules: In range 1 to 100, 
# if the number is divisible by 3, the output will be "Fizz", 
# if the number is divisible by 5, it will be "Buzz"
# if the number is divisible by both, it will be "Fizz-Buzz"

n = int(input("Insert the lower limit: "))
m = int(input("Insert the upper limit: "))

for i in range(n, m + 1):
	if i%3 == 0:	
		if i%5 == 0:
			print("Fizz-Buzz")
		else:
			print("Fizz")
	elif i%5 == 0:
		print("Buzz")
	else:
		print(i)



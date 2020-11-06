x = 0
y = 1
temp = 0

n = int(input("Insert the upper limit: "))

# without recursion
Fib = [x, y]
for i in range(0, n):
	temp = x
	x = y
	y += temp
	Fib.append(y)

print(Fib)

# with recursion
def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n - 1) + fibonacci(n - 2))

if n <= 0:
	print('n is not positive, please enter a positive integer')
else:
	print([fibonacci(i) for i in range(n)])
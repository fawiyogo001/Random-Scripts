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

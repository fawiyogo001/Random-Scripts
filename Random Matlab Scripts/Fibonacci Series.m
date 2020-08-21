function f = fibo(n)
f(1) = 0;
f(2) = 1;

for ii = 3:n
	f(ii) = f(ii - 2) + f(ii - 1);
end
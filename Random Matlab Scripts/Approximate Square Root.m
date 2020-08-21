function y = approx_sqrt(x)
y = x;
while abs(y^2 - x) > 0.0001*x
	y = (x/y + y)/2
end

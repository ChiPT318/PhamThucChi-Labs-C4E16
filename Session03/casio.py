x = int(input(" X = "))
Ope = input("Operation +, -, *, / ")
y = int(input("Y = "))

if Ope == "+":
	result = x+y
elif Ope == "-":
	result = x-y
elif Ope == "*":
	result = x*y
else:
	result = x/y

print("{0} {1} {2} = {3}".format(x, Ope, y, result))

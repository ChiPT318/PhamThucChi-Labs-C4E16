from random import randint, choice
from evaluation import calc

x = randint(0, 10)
y = randint(0, 10)
error = randint(-1, 1)
ope = ["+", "-", "*", "/"]
math = choice(ope)
result = calc(x, y, math)
# if math == "+":
#     result = x + y
# elif math == "-":
#     result = x - y
# elif math == "/":
#     result = x / y
# else:
#     result = x * y

result += error

print("{0} {1} {2} = {3}".format(x, math, y, result))

ans = input("Y/N:").lower()

if (error == 0 and ans == "y") or (error != 0 and ans == "n"):
    print("Yay")
else:
    print("Stupid!!")

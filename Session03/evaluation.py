from random import choice

# x = 3
# Ope = choice(["+", "-", "*", "/"])
# y = 7
#
# if Ope == "+":
# 	result = x+y
# elif Ope == "-":
# 	result = x-y
# elif Ope == "*":
# 	result = x*y
# else:
# 	result = x/y
#
# print(result)

def calc(x, y, Ope):
    if Ope == "+":
    	result = x+y
    elif Ope == "-":
    	result = x-y
    elif Ope == "*":
    	result = x*y
    elif Ope == "/":
    	result = x/y

    return result
# res = calc(3, 7, "-")
# print(res)
#
# r = calc(1, 2, "-")
# print(r)

# argument, parameter
# calc()

calc(3,2, "+")

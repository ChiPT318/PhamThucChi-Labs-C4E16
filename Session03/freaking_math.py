from random import randint


x = randint(0, 10)
y = randint(0, 10)
error = randint(-1, 1)
result = x + y + error

print("{0} + {1} = {2}".format(x, y, result))

ans = input("Y/N:").lower()

if (error == 0 and ans == "y") or (error != 0 and ans == "n"):
    print("Yay")
else:
    print("Stupid!!")
# if error == 0:
#     if ans == "y":
#         print("yay")
#     else:
#         print("stupid")
# else:
#     if ans == "y":
#         print("stupid")
#     else:
#         print("yay")

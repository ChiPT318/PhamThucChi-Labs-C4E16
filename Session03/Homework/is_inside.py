def is_inside(a, b):
    if b[0] <= a[0] <= (b[0] + b[2]) and b[1] <= a[1] <= (b[1]+b[3]):
        return True
    else:
        return False

a1 = [100, 120]
b1 = [140, 60, 100, 200]
a2 = [200, 120]
b2 = [140, 60, 100, 200]

if is_inside(a1, b1) == False and is_inside(a2, b2) == True:
    print("Correct code")
else:
    print("Bug")

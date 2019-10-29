#program for Quadratic quation
import math
a = float(input("Enter the Value for a : "))
b = float(input("Enter the Value for b : "))
c = float(input("Enter the Value for c : "))

d = b ** 2 - 4 * a * c

if d < 0:
    print("No solution")
elif d == 0:
    x = -b / 2 * a
    print("The Root x:", x)
else:
    x1 = (-b - math.sqrt(d)) / 2 * a
    x2 = (-b + math.sqrt(d)) / 2 * a
    print("The Root x1:", x1, "Root x2:", x2)
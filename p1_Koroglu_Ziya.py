# Ziya Batur Koroglu
# Homework 1, Problem 1 - Quadratic Equations

import math
import matplotlib.pyplot as plt

while True:

    first = input("Enter a: ")

    if first == "":
        break

    a = float(first)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("no real solutions")
    elif delta == 0:
        x1 = -b / (2*a)
        print("one solution: %.5f" % x1)
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        print("two solutions: x1=%.5f x2=%.5f" % (x1, x2))

    print()

    xopt = -b / (2*a)
    d = math.sqrt(abs(delta)) / abs(a)

    if d < 1:
        d = 1

    left = xopt - d
    right = xopt + d

    n = 150
    step = (right - left) / (n - 1)

    x = []
    y = []

    for i in range(n):
        xi = left + i*step
        x.append(xi)
        y.append(a*xi**2 + b*xi + c)

    plt.figure()
    plt.plot(x, y, "b.")
    plt.grid(True)
    plt.show()

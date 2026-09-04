# p4_koroglu_ziya.py
# Problem 4 - Function Visualization

import math
import matplotlib.pyplot as plt


def plot_function(fun_str, domain, ns):
    """Sample the function given in fun_str over the interval domain = (xmin, xmax),
    print a table of the values, and draw the chart with matplotlib."""

    xmin = domain[0]
    xmax = domain[1]

    # Distance between two consecutive sample points. We want ns points that
    # include both ends of the interval, so there are ns - 1 gaps between them.
    step = (xmax - xmin) / (ns - 1)

    # the sample points
    xs = []
    for i in range(ns):
        xs.append(xmin + i * step)

    # the value of the function at each sample point
    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    # print the table
    print("{:>10}{:>10}".format("x", "y"))
    print("-" * 20)
    for i in range(ns):
        print("{:10.4f}{:+10.4f}".format(xs[i], ys[i]))

    # draw the chart
    plt.plot(xs, ys, marker=".")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.show()


# code that reads the arguments from the terminal and calls the function

fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

plot_function(fun_str, (xmin, xmax), ns)

import math


def do_something(end, start=1):
    x1 = start
    x2 = 1000 * 1000

    while x1 < end:
        math.sqrt((x1 - x2) - (x1 - x2))
        x1 += 1

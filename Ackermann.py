import sys
import time


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)


# https://en.wikipedia.org/wiki/Ackermann_function
def ack(m, n):
    if m == 0:
        ans = n + 1
    elif n == 0:
        ans = ack(m - 1, 1)
    else:
        ans = ack(m - 1, ack(m, n - 1))
    return ans


time_start = time.time()

with recursionlimit(4000):  # dangerous
    a = 3
    b = 7
    value = ack(a, b)
    time_end = time.time()
time_elapsed = time_end - time_start
print(f"It took ~{round(time_elapsed, 4)} seconds for ack({a},{b}) to produce a value of {value}")

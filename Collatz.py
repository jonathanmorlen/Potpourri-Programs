import time

current = 0
high = 0

time_start = time.time()


def Collatz(num):
    counter = 0
    while num != 1:
        counter += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
    return counter


# test numbers 1 to n for the longest progression of the Collatz sequence
# https://en.wikipedia.org/wiki/Collatz_conjecture
n = 10000
number = 0
for i in range(1, n):
    current = Collatz(i)
    if current > high:
        high = current
        number = i

elapsed_time = time.time() - time_start

print(f"Length of longest chain: {high}")
print(f"Starting number: {number}")
print(f"Time taken to find longest progression from 1 to {n}: {elapsed_time}")

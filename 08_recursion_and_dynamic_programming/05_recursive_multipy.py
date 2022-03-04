import math
import time


def multiply(a, b):
    sum = remainder = 0
    if a < b:
        sum = recursiveMultipy(b, a, b)
        remainder = 0 if a%2 == 0 else b
    else:
        sum = recursiveMultipy(a, b, a)
        remainder = 0 if b%2 == 0 else a

    return (sum<<1)+remainder


def recursiveMultipy(a, b, add, counter=1):
    if counter < b//2:
        add = recursiveMultipy(a, b, add+a, counter+1)
    return add


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    print(multiply(5, 6))      # 30
    print(multiply(15, 27))    # 405

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)
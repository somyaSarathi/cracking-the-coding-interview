# Approch:
# 1. Bottom-UP
# 2. Top-Down
# 3. Half-and-half

# bottom up
def fib_bottom_up(n: int) -> int:
    if n == 0: return 0
    elif n <= 2: return 1

    a = b = 1
    for _ in range(3, n+1):
        c = a+b
        a = b
        b = c

    return b


# top-down
def fib_top_down(n: int, memo: list[int]=None):
    if n == 0: return 0
    elif n <= 2: return 1

    if memo is None:
        memo = [0]*(n+1)
        memo[1] = memo[2] = 1

    if memo[n] == 0:
        memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)

    return memo[n]


if __name__ == '__main__':
    print(fib_bottom_up(32))
    print(fib_top_down(32))
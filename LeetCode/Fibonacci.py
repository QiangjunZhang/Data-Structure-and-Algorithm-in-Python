import time

start_time = time.time()

memo = {}


def fib(n):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
        return 0

    if n == 1:
        memo[1] = 1
        return 1

    val = fib(n - 2) + fib(n - 1)

    memo[n] = val

    return val


def main():
    Fib = [fib(n) for n in range(100)]
    print(Fib)

    print("time elapsed: {:.2f}s".format(time.time() - start_time))


if __name__ == '__main__':
    main()

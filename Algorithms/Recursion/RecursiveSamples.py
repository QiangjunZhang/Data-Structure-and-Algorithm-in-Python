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


def recur_fib(n):
    if n == 1:
        return (0, 1)

    a, b = RecurFib(n-1)
    return a + b, a


def recur_sum(n, S):
    if n == 0 :
        Sum = 0
    else:
        Sum = RecurSum(n-1,S) + S[n-1]
    return Sum


def binary_sum(S, start, stop):
    if stop == start + 1:
        return S[start]
    elif start >= stop:
        return 0
    else:
        mid = (stop + start) //2
        sum = binary_sum(S,start, mid) + binary_sum(S, mid, stop)
        return sum


def linear_reverse(S):
    n = len(S)
    if len(S) == 2:
        return [S[1], S[0]]
    else:
        S_rev = [S[n-1]] + linear_reverse(S[0:n-1])
        return S_rev


def divide_reverse(S, start, stop):
    if start < stop -1:
        S[start], S[stop-1] = S[stop-1], S[start]
        divide_reverse(S, start+1, stop-1)


def power(x, n):
    if n == 0:
        return 1
    else:
        return power(x,n-1)*x


def div_power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n % 2 == 0:
        m = div_power(x, n // 2)
        return m * m
    elif n % 2 != 0:
        m = div_power(x, (n-1) // 2)
        return m * m * x


def unique3(S, start, stop):

    if stop - start <= 1: return True
    elif not unique3(S, start, stop - 1): return False
    elif not unique3(S, start + 1, stop): return False
    else: return S[start] != S[stop-1]


def main():
    # Fib = [fib(n) for n in range(100)]
    # print(Fib)
    # print([RecurFib(n) for n in range(1,10)])
    # print("time elapsed: {:.2f}s".format(time.time() - start_time))
    # S = RecurSum(6,[2,2,2,2,2,2])
    # S = linear_reverse([1,2,3,4,5])
    # S = [1,2,3,4,5]
    # divide_reverse(S, 0, 5)
    # S = power(10, 2)
    S = [1,2,3,4]
    sum = binary_sum(S,0,4)
    # S = div_power(2, 10)
    print(sum)

if __name__ == '__main__':
    main()

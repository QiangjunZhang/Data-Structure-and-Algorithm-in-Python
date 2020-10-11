import heapq


def nthSuperUglyNumber(n, primes):
    q, uglyNums = [], [1]
    k = len(primes)
    for i in range(k):
        heapq.heappush(q, (primes[i], 0, primes[i]))

    while len(uglyNums) < n:
        x, i, p = q[0]
        uglyNums += [x]
        while q and q[0][0] == x:
            x, i, p = heapq.heappop(q)
            heapq.heappush(q, (p * uglyNums[i], i + 1, p))

    return uglyNums[-1]


def test():
    print(nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32)


if __name__ == '__main__':
    test()

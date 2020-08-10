
def add(a , b):
    if b == 0:
        return a
    print(a, b)
    ans = a ^ b
    carry = (a & b) << 1

    return add(ans, carry)

ans = add(3, 1)


print(ans)

def LCS(X, Y):
    memo = {}
    # memo[0,0] = 0
    solution = []

    def dp(i, j):
        if i <0 or j < 0:
            return 0
        if (i,j) not in memo:
            if X[i] == Y[j]:
                solution.append(X[i])
                memo[i,j] = 1 + dp(i-1,j-1)
            else:
                memo[i,j] = max(dp(i-1, j), dp(i, j - 1))
        return memo[i,j]

    return dp(len(X)-1, len(Y)-1), solution

X = 'abbcdde'
Y = 'bbbcdeg'

ans = LCS(X,Y)
print(ans)
# print(solution)
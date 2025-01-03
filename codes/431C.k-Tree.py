n, k, d = map(int, input().split())
mod = 10**9 + 7
dp1 = [1] + [0] * n
dp2 = [1] + [0] * n
for i in range(1, n+1):
    for j in range(1, min(i, k) + 1):
        dp1[i] = (dp1[i] + dp1[i-j]) % mod
    for j in range(1, min(d, i + 1)):
        dp2[i] = (dp2[i] + dp2[i-j]) % mod
print((dp1[n]-dp2[n])%mod)
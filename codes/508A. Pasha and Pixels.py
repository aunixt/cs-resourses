n, m, k = map(int, input().split())
dp = [[0] * (m+2) for _ in range(n+2)]
direction1 = [(0,-1),(-1,-1),(-1,0)]
direction2 = [(-1,0),(-1,1),(0,1)]
direction3 = [(0,1),(1,1),(1,0)]
direction4 = [(1,0),(1,-1),(0,-1)]
for x in range(k):
    i, j = map(int, input().split())
    dp[i][j] = 1
    if dp[i+direction1[0][0]][j+direction1[0][1]] == 1 and dp[i+direction1[1][0]][j+direction1[1][1]] == 1 and dp[i+direction1[2][0]][j+direction1[2][1]] == 1:
        print(x+1)
        break
    elif dp[i+direction2[0][0]][j+direction2[0][1]] == 1 and dp[i+direction2[1][0]][j+direction2[1][1]] == 1 and dp[i+direction2[2][0]][j+direction2[2][1]] == 1:
        print(x+1)
        break
    elif dp[i+direction3[0][0]][j+direction3[0][1]] == 1 and dp[i+direction3[1][0]][j+direction3[1][1]] == 1 and dp[i+direction3[2][0]][j+direction3[2][1]] == 1:
        print(x+1)
        break
    elif dp[i+direction4[0][0]][j+direction4[0][1]] == 1 and dp[i+direction4[1][0]][j+direction4[1][1]] == 1 and dp[i+direction4[2][0]][j+direction4[2][1]] == 1:
        print(x+1)
        break
else:
    print(0)
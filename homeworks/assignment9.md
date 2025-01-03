# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>徐贤天、工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：



代码：

```python
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def dfs(x, y, matrix, visited):
    stack = [(x, y)]
    visited[x][y] = True
    area = 0
    while stack:
        x, y = stack.pop()
        area += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if matrix[nx][ny] == 'W' and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = True
    return area

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = [[0]*(m+2)]
    for _ in range(n):
        matrix.append([0] + list(input()) + [0])
    matrix.append([0]*(m+2))
    visited = [[False] * (m+2) for _ in range(n+2)]
    max_area = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            if matrix[x][y] == 'W' and not visited[x][y]:
                max_area = max(max_area, dfs(x, y, matrix, visited))
    print(max_area)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241120213310591](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241120213310591.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：

刚开始在nx和ny处判断是否到1点，结果一直WA，看了群里才发现特殊情况没有考虑

代码：

```python
from collections import deque
directions = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y,matrix,step):
    q = deque()
    inq = set()
    q.append((x,y,step))
    inq.add((x,y))
    while q:
        x,y,step = q.popleft()
        if matrix[x][y] == 1:
            return step
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in inq and matrix[nx][ny] != 2:
                q.append((nx,ny,step+1))
                inq.add((nx,ny))
    return 'NO'
m, n = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(m)]
print(bfs(0,0,matrix,0))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241123151820739](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241123151820739.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：



代码：

```python
#pylint:skip-file
T = int(input())
directions = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def dfs(x, y, step):
    global cnt
    visited[x][y] = True
    if step == n*m-1:
        cnt += 1
        visited[x][y] = False
        return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny, step+1)
    visited[x][y] = False

for _ in range(T):
    n, m, x, y = map(int, input().split())
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    dfs(x, y, 0)
    print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241123154839344](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241123154839344.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：



代码：

```python
n, m = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
path = []
max_sum = -float('inf')
visited = [[False] * m for _ in range(n)]

def dfs(x, y, temp, now_sum):
    global max_sum, path
    visited[x][y] = True
    temp.append((x,y))
    now_sum += matrix[x][y]
    if x == n-1 and y == m-1:
        if now_sum > max_sum:
            max_sum = now_sum
            path = temp[:]
            temp.pop()
            visited[x][y] = False
            return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            dfs(nx, ny, temp, now_sum)
    temp.pop()
    visited[x][y] = False
dfs(0, 0 ,[], 0)
for x, y in path:
    print(x+1, y+1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241123165305961](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241123165305961.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：



代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241123170540336](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241123170540336.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：



代码：

```python
from math import sqrt
A = int(input())
ls = [int(x) for x in str(A)]
def dfs(i):
    if i == len(ls):
        return True
    num = 0
    for j in range(i,len(ls)):
        num = num * 10 + ls[j]
        if sqrt(num) % 1 == 0 and num != 0:
            if dfs(j+1):
                return True
    return False
print('Yes' if dfs(0) else 'No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241123200049673](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241123200049673.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

这次的作业比较友好，基本就是照着模板来的，只是一些细节的地方还是得多加注意。

在矩阵最大权值路径中又一次需要拷贝，这同样是语法上的细节需要注意。

照着讲义上的题目一道一道练下来，对dfs和bfs的掌握更加熟练了。


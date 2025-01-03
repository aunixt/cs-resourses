# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>徐贤天，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：



代码：

```python
n,m = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(n)]
directions = [(-1,0),(1,0),(0,1),(0,-1)]
cnt = 0
for x in range(n):
    for y in range(m):
        if mp[x][y] == 1:
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or mp[nx][ny] == 0:
                    cnt += 1
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 192215](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-11-13 192215.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
class Solution:
    def spiralOrder(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        d_idx = 0
        order = []
        x, y = 0, 0
        for i in range(row*col):
            order.append(matrix[x][y])
            matrix[x][y] = '*'
            dx, dy = directions[d_idx]
            if not (0 <= x + dx < row and 0 <= y + dy < col and matrix[x + dx][y + dy] != '*'):
                d_idx = (d_idx + 1) % 4
            x += directions[d_idx][0]
            y += directions[d_idx][1]
        return order
matrix = eval(input())
x = Solution().spiralOrder(matrix)
print(x)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-11-13 211144](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-11-13 211144.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d = int(input())
n = int(input())
matrix = [[0] * 1025 for _ in range(1025)]
for _ in range(n):
    x, y, i = map(int,input().split())
    for a in range(max(0,x-d),min(1025,x+d+1)):
        for b in range(max(0,y-d),min(1025,y+d+1)):
            matrix[a][b] += i
max_trash = 0
cnt = 0
for i in range(1025):
    for j in range(1025):
        if matrix[i][j] > max_trash:
            cnt = 1
            max_trash = matrix[i][j]
        elif matrix[i][j] == max_trash:
            cnt += 1
print(cnt,max_trash)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![屏幕截图 2024-11-13 213124](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-11-13 213124.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] * n
        down = [1] * n
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                up[i] = up[i-1]
            else:
                up[i] = max(up[i-1], down[i-1]+1)
            if nums[i] >= nums[i-1]:
                down[i] = down[i-1]
            else:
                down[i] = max(down[i-1], up[i-1]+1)
        return max(up[n-1], down[n-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241116143422528](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241116143422528.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

将dp[i]定义为以i为最大值，在从原始序列里取出的子列中能得到的最大分。若不取i，则最大分为dp[i-1]；若取i，则最大分为x*count[x]+dp[1-2]。两者取大。

代码：

```python
n = int(input())
nums = [int(x) for x in input().split()]
max_num = max(nums)
count = [0]*(max_num+1)
for i in nums:
    count[i] += 1
dp = [0]*(max_num+1)
dp[1] = count[1]
for i in range(2,max_num+1):
    dp[i] = max(dp[i-1],dp[i-2]+i*count[i])
print(dp[max_num])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241116152524442](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241116152524442.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    t_horses = [int(x) for x in input().split()]
    k_horses = [int(x) for x in input().split()]
    t_horses.sort()
    k_horses.sort()
    lt, rt = 0, n-1
    lk, rk = 0, n-1
    while lt <= rt:
        if t_horses[rt] > k_horses[rk]:
            cnt += 1
            rt -= 1
            rk -= 1
        elif t_horses[lt] > k_horses[lk]:
            cnt += 1
            lt += 1
            lk += 1
        else:
            if t_horses[lt] < k_horses[rk]:
                cnt -= 1
            lt += 1
            rk -=1
    print(cnt * 200)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241116190833701](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241116190833701.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

期中考结束了，最近在计概上投入的时间更多了。

感觉作业题中矩阵部分比较简单，后面的dp题也比较容易理解，重点是选择子问题的方式、确定初始状态和找到转移方程。

田忌赛马真的比较难，尤其是贪心算法的选取，看了题解收获很大，但dp的方法想了很久才明白。




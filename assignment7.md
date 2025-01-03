# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>徐贤天，工学院</mark>



**说明：**

1）⽉考： AC3 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n = int(input())
ls = []
for _ in range(n):
    case = input().split()
    ls.append(case)
old = []
young = []
for x in ls:
    if int(x[1]) >= 60:
        old.append(x)
    else:
        young.append(x)
old.sort(key = lambda x: int(x[1]),reverse = True)
for i in range(len(old)):
    print(old[i][0])
for i in range(len(young)):
    print(young[i][0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241109211645767](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109211645767.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,m1,m2 = map(int,input().split())
A = [[0]*n for _ in range(n)]
B = [[0]*n for _ in range(n)]
for _ in range(m1):
    i,j,x = map(int,input().split())
    A[i][j] = x
for _ in range(m2):
    i,j,x = map(int,input().split())
    B[i][j] = x
C = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k]*B[k][j]
for i in range(n):
    for j in range(n):
        if C[i][j] != 0:
            print('{} {} {}'.format(i,j,C[i][j]))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241109211711551](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109211711551.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
nCase = int(input())
for _ in range(nCase):
    n,m,b = map(int,input().split())
    case = []
    s = set()
    for _ in range(n):
        case.append(list(map(int,input().split())))
    for i in range(n):
        s.add(case[i][0])
    s = list(s)
    s.sort()
    for i in s:
        ls = []
        for j in range(n):
            if case[j][0] == i:
                ls.append(case[j][1])
        ls.sort(reverse = True)
        if len(ls) <= m:
            b -= sum(ls)
        else:
            b -= sum(ls[0:m])
        if b <= 0:
            print(i)
            break
    else:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241109211736521](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109211736521.png)

### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：



代码：

```python
def make_changes(dp,coins,change):
    for cents in range(1,change+1):
        for coin in coins:
            if cents >= coin:
                dp[cents] = min(dp[cents],dp[cents-coin]+1)
    return dp[-1] if dp[-1] != float("inf") else -1
n,m = map(int,input().split())
coins = [int(x) for x in input().split()]
dp = [float('inf')]*(m+1)
dp[0] = 0
print(make_changes(dp,coins,m))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241109215051736](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109215051736.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：



代码：

```python
strs = input().split()
dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16,'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}
if strs[0] == 'negative':
    sgn = -1
    strs.pop(0)
else:
    sgn = 1

temp = 0
ans = 0
for i in strs:
    if i in ['thousand', 'million']:
        ans += temp * dict[i]
        temp = 0
        continue
    if i == 'hundred':
        temp *= 100
    else:
        temp += dict[i]
ans += temp
print(ans * sgn)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241109230228110](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109230228110.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

选择不相交区间问题

代码：

```python
n = int(input())
intervals = [[int(x) for x in input().split()] for _ in range(n)]
intervals.sort(key=lambda x: x[1])
end = -float('inf')
ans = 0
for i in range(n):
    a, b = intervals[i]
    if a > end:
        ans += 1
        end = b
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241109232755343](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241109232755343.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最近一直在准备数学的期中，计概刷题刷的少了，坐在考场上明显感觉到生疏，犯了很多低级的错误，浪费了很多时间。尤其是第一题，在病人年龄排序的时候竟然忘了加int，花了很多时间才检查出来，最后的那些题目来不及看了TAT。一些模版型的题目本该马上反应过来，题目应该说是比较简单的，但结果比较惨。这次考试实在给我敲响了警钟，在接下来的一个多月时间里要更加重视计概，每天都要保持两小时以上的时间。此外机房还是要多去几次，感觉机房的键盘和环境跟自己在笔记本上有很大不同，打字的时候经常敲错。




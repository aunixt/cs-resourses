# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>徐贤天，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
case = 0
while True:
    case += 1
    p, e, i, d = map(int,input().split())
    if p == e == i == d == -1:
        break
    p, e, i = p % 23, e % 28, i % 33
    for x in range(d+1, d+21253):
        if x % 23 == p and x % 28 == e and x % 33 == i:
            print('Case {}: the next triple peak occurs in {} days.'.format(case, x-d))
            break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241023194800100](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241023194800100.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

用ans变量储存more_weapons变量的最大值。有钱就买，没钱就卖。

代码：

```python
p = int(input())
ls = list(map(int,input().split()))
ls.sort()
more_weapons = 0
ans = 0
n = len(ls)
i, j = 0, n-1
while i <= j:
    if ls[i] <= p:
        more_weapons += 1
        ans = max(ans, more_weapons)
        p -= ls[i]
        i += 1
    else:
        more_weapons -= 1
        if more_weapons < 0:
            ans = 0
            break
        p += ls[j]
        j -= 1
print(ans)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241023222411659](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241023222411659.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：



代码：

```python
n = int(input())
ls = [int(x) for x in input().split()]
seq = []
average_waiting_time = 0
counted_ls = list(enumerate(ls))
counted_ls.sort(key=lambda x: x[1])
for i, j in counted_ls:
    seq.append(i+1)
    average_waiting_time += j*(n-1)
    n -= 1
average_waiting_time = average_waiting_time/len(ls)
print(' '.join(map(str, seq)))
print('{:.2f}'.format(average_waiting_time))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241023224807278](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241023224807278.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

刚开始在从0还是从1开始上出现了一些问题

代码：

```python
Haab_Calendar = {
    'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5, 'yoxkin': 6,
    'mol': 7, 'chen': 8, 'yax': 9, 'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13,
    'muan': 14, 'pax': 15, 'koyab': 16, 'cumhu': 17, 'uayet': 18
}

Tzolkin_Calendar = {
    0: 'imix', 1: 'ik', 2: 'akbal', 3: 'kan', 4: 'chicchan', 5: 'cimi',
    6: 'manik', 7: 'lamat', 8: 'muluk', 9: 'ok', 10: 'chuen', 11: 'eb',
    12: 'ben', 13: 'ix', 14: 'mem', 15: 'cib', 16: 'caban', 17: 'eznab',
    18: 'canac', 19: 'ahau'
}

def Haab_to_Tzolkin(Haab_date):
    a, b, c = Haab_date.split()
    a = int(a.strip('.'))
    b = Haab_Calendar[b]
    c = int(c)
    total_days = c * 365 + b * 20 + a
    tzolkin_year = total_days // 260
    tzolkin_day = total_days % 260
    tzolkin_num = tzolkin_day % 13 + 1  # 数字从1到13
    tzolkin_name = Tzolkin_Calendar[tzolkin_day % 20]
    return '{} {} {}'.format(tzolkin_num, tzolkin_name, tzolkin_year)

n = int(input())
print(n)
for _ in range(n):
    print(Haab_to_Tzolkin(input()))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241024154720622](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241024154720622.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

用到了一个指针+贪心

代码：

```python
n = int(input())
loc = []
height = []
ans = 2

for _ in range(n):
    x, h = map(int, input().split())
    loc.append(x)
    height.append(h)

k = loc[0]
for i in range(1, n-1):
    if loc[i] - k - 1 >= height[i]:
        ans += 1
        k = loc[i]
    else:
        if loc[i+1] - loc[i] - 1 >= height[i]:
            ans += 1
            k = loc[i] + height[i]
        else:
            k = loc[i]
if n == 1:
    ans = 1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241024163809879](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241024163809879.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

课件中的区间选点问题

代码：

```python
from math import sqrt

def num_of_radar(d,loc):
    ls = []
    for i in range(len(loc)):
        x, y = loc[i]
        if y > d:
            return -1
        ls.append([x-sqrt(d**2-y**2),x+sqrt(d**2-y**2)])
    ls.sort(key=lambda x: x[1])
    ans = 0
    ed = -float('inf')
    for v in ls:
        if ed < v[0]:
            ans += 1
            ed = v[1]
    return ans

case = 1
loc = []
while True:
    n, d = map(int, input().split())
    if n == d == 0:
        break
    for _ in range(n+1):
        rg = list(map(int, input().split()))
        if not rg:
            print('Case {}: {}'.format(case, num_of_radar(d,loc)))
            case += 1
            loc = []
            continue
        else:
            loc.append(rg)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025001936426](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241025001936426.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

课件上的内容非常丰富，学到了双指针、二分查找和区间的算法等，收获颇丰。此外也开始学如何在pycharm里调试程序。

感觉作业题目的难度越来越大，有时想了半天也没有思路。有时可能在代码的细节上出现缺漏，比如忘记把最后一组数据加入列表，或者是某些特殊情况没有考虑到，导致基本的思路是正确的，但总是在细节上掉链子，而由于不熟悉调试的过程，检查起来比较费劲。接下来要多学学怎么调试代码了。

继续跟进每日选做。




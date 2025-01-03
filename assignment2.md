# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==徐贤天，工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：

首先构造出一个二位列表x，用行、列指标i，j分别遍历，如果找到了1就直接退出循环

（第一次写的时候在break和continue的逻辑上出现了问题，想了一会儿才想通）

##### 代码

```python
# 
x = []
for _ in range(5):
    m = list(map(int, input().split()))
    x.append(m)
for i in range(5):
    for j in range(5):
        if x[i][j] == 1:
            break
    else:
        continue #内层循环没有找到规定的数值，则继续进行循环（不执行第十一行的break）
    break #找到‘1’之后，退出外层循环
n = abs(i-2) + abs(j-2)
print(n)
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-09-27 151121](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-27 151121.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：

用数学方法来想：如果a直接被b整除，则直接输出0；如果不整除，则b最大会被放大到n=a//b+1倍，所以结果就是n*b-a

##### 代码

```python
# 
t = int(input())
ret = []
for _ in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        ret.append(0)
    else:
        n = a//b+1
        ret.append(n*b-a)
print('\n'.join(map(str, ret)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![屏幕截图 2024-09-24 170853](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-24 170853.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：

officers特别像游戏里的子弹，每次见到怪物就发射一颗，于是每次循环officers都会减一；当officers=0时怪物就会逃走，使得untreated_crimes_num加一；而输入的正数就是补充的子弹；利用continue跳过officers-1

##### 代码

```python
# 
n = int(input())
nums = list(map(int,input().split()))
untreated_crimes_mun = 0
officers = 0
for i in nums:
    if i < 0 and officers == 0:
        untreated_crimes_mun += 1
        continue
    if i > 0:
        officers += i
        continue
    officers -= 1
print(untreated_crimes_mun)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-26 234529](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-26 234529.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：

想着能不能把原先的[0,l]区间分割成一段一段的。主要是考虑被切割的[a,b]区间与原先的区间的包含关系，需要分类讨论。

（看了答案才发现原来还可以这么写，自己原先的思路有点复杂了）

##### 代码

```python
# 
l, m = map(int, input().split())
r = [(0, l)]
left = 0
for _ in range(m):
    a, b = map(int, input().split())
    new_r = []
    for start, end in r:
        if a <= end and b >= start:
            if a > start:
                new_r.append((start, a - 1))
            if b < end:
                new_r.append((b + 1, end))
        else:
            new_r.append((start, end))
    r = new_r
for start, end in r:
    left += end - start + 1
print(left)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-27 152920](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-27 152920.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：

主要是把原数据的每一个位数提取出来。因为题目把数据限制在三位树，则可以直接用x, y, z = map(int, list(str_n))

##### 代码

```python
# 
a, b = map(int, input().split())
s = []
for n in range(a, b+1):
    str_n = str(n)
    x, y, z = map(int, list(str_n))
    if x**3+y**3+z**3==n:
        s.append(n)
if len(s) > 0:
    print(*s)
else:
    print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-27 110418](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-27 110418.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：

感觉结合x-t图像会理解地更为清楚，把Charley每一次切换到不同速度所用的总共的时间等效到最后的一次碰到的人所用的总时间上；如果起始时间t小于0，则要么不会与Charley相遇（速度太快），要么相遇了也不会变换速度（速度太慢），所以可以直接continue跳过

##### 代码

```python
# 
from math import ceil
while True:
    n = int(input())
    if n == 0:
        break
    time = float('inf')
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        arrival_time = (4.5 / v) * 3600 + t
        if arrival_time < time:
            time = arrival_time
    print(ceil(time))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![屏幕截图 2024-09-27 150546](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-27 150546.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

continue和break的用法更加清晰了，之前还有很多模糊的地方。（gpt太强了）

一个好的算法非常重要，在动手敲代码之前要好好花时间想清楚，感觉很多时候总是无法很快想到简洁的解法，可能还是见到的算法类型不够多？有时该用计算机思维的反而用了math，该用math的反而用了计算机，致使代码量巨大TAT

学到很多新的语法，比如列表解析式、解包运算符等（虽然感觉用到的机会比较少），还有一些函数和方法，有时能够简化运算，有时反而弄巧成拙。

使用列表和元组更加熟练了，很多地方都会用到；但是字典和集合还是没怎么用到，希望接下来多用用。

用OneNote总结了常用数据类型的一些函数和方法，以及遇到问题的基本思路，希望在之后能用到！

加快跟上每日选做！




# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==徐贤天 工学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：



##### 代码

```python
# 
y = int(input())
if y % 3200 == 0:
    print("N")
elif y % 3200 != 0 and y % 400 != 0 and y % 100 == 0:
    print("N")
elif y % 4 == 0:
    print("Y")
else:
    print("N")
```



代码运行截图 ==（至少包含有"Accepted"）==

![](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-10 235349.png)



### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：



##### 代码

```python
# 
a = int(input())
if a % 4 == 0:
    print(int(a/4), int(a/2))
elif a % 2 == 0:
    print(int((a+2)/4), int(a/2))
else:
    print(0, 0)

```



代码运行截图 ==（至少包含有"Accepted"）==

![](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-10 235233.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：只有两种情况：如果长和宽都是奇数，则最终空出一个空；其他情况都可以排满



##### 代码

```python
# 
user_input = input()
values=user_input.split()
value1=int(values[0])
value2=int(values[1])
if value1 % 2 != 0 and value2 % 2 != 0:
    ret=int((value1*value2-1)/2)
else:
    ret=int(value1*value2/2)
print(ret)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-10 234812.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：如果恰好整除，则直接相乘；如果不恰好，则向上取整后相乘



##### 代码

```python
# 
m, n, a = map(int, input().split())
if m % a == 0 and n % a == 0:
    ret=int((m/a)*(n/a))
elif m % a == 0 and n % a != 0:
    ret=int((m/a)*(n//a+1))
elif m % a != 0 and n % a == 0:
    ret=int((m//a+1)*(n/a))
else:
    ret=(m//a+1)*(n//a+1)
print(ret)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-12 171354.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：先把大写字母全部转为小写，然后直接比较



##### 代码

```python
# 
v1 = input().lower()
v2 = input().lower()
if v1 < v2:
    print(-1)
elif v1 > v2:
    print(1)
else:
    print(0)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20240912221525439.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：利用列表实现计数



##### 代码

```python
# 
n = int(input())
sum = 0
for i in range(n):
    a, b, c = map(int, input().split())
    l = [a, b, c]
    m = l.count(1)
    if m >= 2:
        sum +=1
print(sum)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20240912222738817.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==



额外练习了2024fall 每日选做中从0823到0827的800难度题目，从0903到0905的900难度题目，以及中秋的部分题目。

认识到AI工具的强大，好多不懂的问题都可以直接向它提出，解答也非常的清晰。

![](C:\Users\31275\Pictures\Screenshots\屏幕截图 2024-09-20 000432.png)


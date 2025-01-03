# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==徐贤天，工学院==



**说明：**

1）Oct⽉考： AC6==4== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：



代码

```python
k = int(input())
input_str = input()
new_str = ''
for i in input_str:
    if 'A' <= i <='Z':
        index = ord(i) - k
        while index < 65:
            index += 26
        while index > 90:
            index -= 26
        new_str += chr(index)
    if 'a' <= i <='z':
        index = ord(i) - k
        while index < 97:
            index += 26
        while index > 122:
            index -= 26
        new_str += chr(index)
print(new_str)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011225230913](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241011225230913.png)

大致花费时间：15min（刚开始没有注意到可能还会有大写字母，在错误的道路上走了好久）



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：

由于输入的字符串的长度固定，简化了代码

代码

```python
a, b = map(str,input().split())
num1 = int(a[0:2])
num2 = int(b[0:2])
print(num1+num2)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241011230439929](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241011230439929.png)

大致花费时间：2min

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：



代码

```python
n = int(input())
mul = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
last = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}
for _ in range(n):
    input_str = input()
    num = [int(x) for x in input_str[0:17]]
    loc = 0
    s = 0
    for i in num:
        s += i * mul[loc]
        loc += 1
    if input_str[-1] == last[s%11]:
        print('YES')
    else:
        print('NO')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011230800003](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241011230800003.png)

大致花费时间：10min



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python
n = int(input())
while n != 1:
    if n % 2 == 1:
        old = n
        n = n * 3 + 1
        print('{}*3+1={}'.format(old,n))
    else:
        old = n
        n = n // 2
        print('{}/2={}'.format(old,n))
print('End')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241011231050151](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241011231050151.png)

大致花费时间：15min

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：

分为两个模块。

第一个函数从罗马到数字，让i从后往前取，如果遇到比前一个字母小的字母，则减去对应数字，反之则加上对应数字。

第二个函数从数字到罗马，先构造两个一一对应的列表，从大往小整除，如果有就加上对应个数的罗马数字，同时减去对应的阿拉伯数字，完成后i+1.

最后用到了isdigital（）函数，感觉挺好用。

##### 代码

```python
# 
def rom_to_num(n):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    pre_num = 0
    for i in reversed(n):
        if romans[i] < pre_num:
            num -= romans[i]
        else:
            num += romans[i]
            pre_num = romans[i]
    return num

def num_to_rom(n):
    rom = ''
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
               rom += sym[i]
               n -= val[i]
        i += 1
    return rom

n = input()
if n.isdigit():
    print(num_to_rom(int(n)))
else:
    print(rom_to_num(n))
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012001557782](C:\Users\31275\AppData\Roaming\Typora\typora-user-images\image-20241012001557782.png)

大致花费时间：73+min（两次都是Runtime Error，没有找到合适的算法）

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

感觉做题速度还有待提高，熟练度还不够。

从考试第五题发现自己还存在着许多问题。原先想着建一个比较大的字典，把罗马数字分割成很多段，再对应到阿拉伯数字，结果超时（太暴力了）；后来想着把所有的特殊字母单独数出来，又超时。之后就没有想出更好的算法了。思维水平还有待提高吧，见到的算法还不够多，应该要多看看那些优秀的代码之中蕴含的思维。

最近还在赶着每日选做的进度，希望能够加快跟上进度！








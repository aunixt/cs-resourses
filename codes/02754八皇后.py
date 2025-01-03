ans = []
def Queens(seq):
    for j in range(1,9): #在这一行遍历1~8列，j为列数
        for x in range(len(seq)): #找出已经存在的皇后，x为皇后所在行，int(seq[x])为皇后所在列
            if seq[x] == str(j) or abs(j-int(seq[x])) == abs(len(seq)-x): #如果在同一列or行间距=列间距
                break #判断第j列能否摆放皇后
        else: #若j对于每个已存在的皇后都不能被吃
            if len(seq) == 7: #如果已经到了最后一行
                ans.append(seq+str(j)) #将s+str(j)压入ans中
            Queens(seq+str(j)) #进入下一层
Queens('') #生成ans

n = int(input())
for _ in range(n):
    b = int(input())
    print(ans[b-1])


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


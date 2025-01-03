n = int(input())
words = input().split()
result = []
line = ''
length = 0
for word in words:
    if length + len(word) + (1 if length > 0 else 0) > 80:  #判断加上word之后长度是否超过80
        result.append(line)
        line = word     #重置line和length
        length = len(word)
    else:
        if length > 0:
            line += ' '
            length +=1  #为了确保第一行之前没有空格
        line += word
        length += len(word)
if line:    #如果最后一行有word
    result.append(line) #输出最后一行
print('\n'.join(result))

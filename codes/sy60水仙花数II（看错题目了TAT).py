a, b = map(int,input().split())
max_num = int((max(a,b)**(1/3)))
nums = []
for i in range(1,max_num):
    nums.append(i**3)
print(nums)

def daffodils_num_judgement(num):
    length = len(nums)
    for x in range(length):
        for y in range(x,length):
            for z in range(y,length):
                if nums[x]+nums[y]+nums[z]==num:
                    return True
    return False

for num in range(a,b+1):
    if daffodils_num_judgement(num):
        print(num, end=' ')
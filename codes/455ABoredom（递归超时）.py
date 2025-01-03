def most_points(nums,points):
    if not nums:
        ans.append(points)
    for i in set(nums):
        new_points = points + i
        new_nums = [x for x in nums if x != i-1 and x != i+1]
        new_nums.remove(i)
        most_points(new_nums,new_points)

n = int(input())
nums = [int(x) for x in input().split()]
ans = []
most_points(nums,0)
print(max(ans))
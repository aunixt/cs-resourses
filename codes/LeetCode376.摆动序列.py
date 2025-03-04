def wiggleMaxLength(nums):
    n = len(nums)
    up = [1] * n
    down = [1] * n
    for i in range(1,n):
        if nums[i] <= nums[i-1]:
            up[i] = up[i-1]
        else:
            up[i] = max(up[i-1], down[i-1]+1)
        if nums[i] >= nums[i-1]:
            down[i] = down[i-1]
        else:
            down[i] = max(down[i-1], up[i-1]+1)
    print(max(up[n-1], down[n-1]))

nums = eval(input())
wiggleMaxLength(nums)

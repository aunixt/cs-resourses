def kadane(arr):
    max_end_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_end_here = max(x, max_end_here + x)
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far

def max_sub_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = -float('inf')
    for left in range(cols):
        temp = [0]*rows
        for right in range(left,cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum

N = int(input())
nums = []
while len(nums) < N**2:
    s = [int(x) for x in input().split()]
    nums.extend(s)
matrix = [nums[i*N:(i+1)*N] for i in range(N)]
print(max_sub_matrix(matrix))
from collections import defaultdict
m, n = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(m)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
scores = {}
great_num = 0
ans = 0
for i in range(m*n):
    score = input()
    if not score:
        scores[i] = ''
    else:
        scores[i] = [int(x) for x in score.split()]

count_grades = defaultdict(int)
for score in scores.values():
    count_grades[sum(score)] += 1
grades = list(count_grades.keys())
grades.sort(reverse = True)
for i in grades:
    cnt = count_grades[i]
    great_num += cnt
    if great_num > m*n*0.4:
        great_num -= cnt
        break

for x in range(m):
    for y in range(n):
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and scores[matrix[nx][ny]] == scores[matrix[x][y]]:
                ans += 1
                break

print(ans, great_num)
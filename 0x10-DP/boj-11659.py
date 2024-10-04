# 18:25~18:30
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sums = [0]
now_sum = 0
for num in numbers:
    now_sum = now_sum + num
    sums.append(now_sum)


for _ in range(m):
    start, finish = map(int, input().split())
    print(sums[finish] - sums[start - 1])

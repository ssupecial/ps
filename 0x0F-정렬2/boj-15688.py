n = int(input())

import sys

numbers = [int(sys.stdin.readline()) for _ in range(n)]
for num in sorted(numbers):
    print(num)

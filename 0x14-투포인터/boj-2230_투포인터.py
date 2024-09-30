# 9월 30일 18:30~18:45
n, m = list(map(int, input().split()))
numbers = [int(input()) for _ in range(n)]
numbers.sort()
len_n = len(numbers) -1

start = 0
finish = 0

answer = None

while start <= len_n:
    while finish <= len_n and (numbers[finish] - numbers[start]) < m:
        finish += 1

    if finish == len_n + 1: 
        break

    cur = numbers[finish] - numbers[start]
    if cur >= m:
        if answer is None:
            answer = cur
        else:
            answer = min(answer, cur)
    start += 1

print(answer)
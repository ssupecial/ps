# 9월 30일 18:50~
n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
len_n = len(numbers)
finish = 0
sum = 0
answer = len_n + 1
for start in range(len_n):
    while finish < len_n and sum < m:
        sum += numbers[finish]
        finish += 1
        
    if sum >= m:
        count = finish - start
        answer = min(answer, count)

    sum -= numbers[start]

if answer == len_n + 1:
    answer = 0

print(answer)

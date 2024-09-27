# 15:45~16:10
n = int(input())
times = []
for i in range(n):
    s, f = list(map(int, input().split()))
    times.append([s, f])

cur_finish = 0
num = 0
times.sort(key=lambda x: (x[1], x[0]))

for time in times:
    s, f = time
    if s >= cur_finish:
        num += 1
        cur_finish = f

print(num)

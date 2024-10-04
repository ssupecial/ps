import sys

input = sys.stdin.readline
n = int(input())

counts = [0, 0, 1, 1]
previous = [0, 0, 1, 1]

for i in range(4, n + 1):
    tmp = i - 1
    if i % 3 == 0:
        if counts[tmp] > counts[i // 3]:
            tmp = i // 3
    if i % 2 == 0:
        if counts[tmp] > counts[i // 2]:
            tmp = i // 2

    counts.append(counts[tmp] + 1)
    previous.append(tmp)

print(counts[n])

tmp = n
answers = []
while tmp >= 1:
    answers.append(tmp)
    tmp = previous[tmp]

print(" ".join(map(str, answers)))

import sys

n = int(input())
scores = [0] * (n + 1)
answers = [0] * (n + 1)
for i in range(1, n + 1):
    scores[i] = int(sys.stdin.readline())

answers[1] = scores[1]

if n > 1:
    answers[2] = scores[1] + scores[2]
if n > 2:
    answers[3] = scores[1] + scores[3]


for i in range(3, n + 1):
    answers[i] = (
        max(
            [
                answers[i - 2],
                answers[i - 3] + scores[i - 1],
            ]
        )
        + scores[i]
    )

print(answers[n])

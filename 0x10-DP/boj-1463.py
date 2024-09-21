n = int(input())
answers = [-1]

for i in range(1, n + 1):
    temp = []
    if i % 3 == 0:
        temp.append(answers[i // 3])
    if i % 2 == 0:
        temp.append(answers[i // 2])

    temp.append(answers[i - 1])

    answers.append(min(temp) + 1)


print(answers[n])

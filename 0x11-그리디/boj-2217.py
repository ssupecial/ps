n = int(input())
weights = sorted([int(input()) for _ in range(n)])
answers = []
len_weights = len(weights)
for i in range(n):
    answers.append(weights[i] * (len_weights - i))

print(max(answers))

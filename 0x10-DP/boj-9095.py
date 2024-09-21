import sys

n = int(input())
testcases = []
for _ in range(n):
    testcases.append(int(sys.stdin.readline()))

max_testcase = max(testcases)
answers = [0, 1, 2, 4, 7]
for i in range(5, max_testcase + 1):
    answers.append(answers[i - 1] + answers[i - 2] + answers[i - 3])
for testcase in testcases:
    print(answers[testcase])

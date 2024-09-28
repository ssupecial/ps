n = int(input())
r, g, b = list(map(int, input().split()))

result = []
result.append([r, g, b])
for i in range(1, n):
    r, g, b = list(map(int, input().split()))

    # 빨강 선택
    result_r = min(result[i - 1][1], result[i - 1][2]) + r

    # 초록 선택
    result_g = min(result[i - 1][0], result[i - 1][2]) + g

    # 파랑 선택
    result_b = min(result[i - 1][0], result[i - 1][1]) + b

    result.append([result_r, result_g, result_b])

print(min(result[-1]))

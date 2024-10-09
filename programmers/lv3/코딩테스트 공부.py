# 21:45~23:00
def solution(alp, cop, problems):
    max_alp = max([problem[0] for problem in problems] + [alp])
    max_cop = max([problem[1] for problem in problems] + [cop])
    answer = 0

    dp = [[float("inf")] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i < max_alp:
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])

            for needed_alp, needed_cop, plus_alp, plus_cop, cost in problems:
                if i >= needed_alp and j >= needed_cop:
                    next_alp = min(i + plus_alp, max_alp)
                    next_cop = min(j + plus_cop, max_cop)
                    dp[next_alp][next_cop] = min(
                        dp[next_alp][next_cop], dp[i][j] + cost
                    )

    return dp[max_alp][max_cop]


# answer = solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]])
answer = solution(
    0,
    0,
    [
        [4, 3, 1, 1, 100],
        [0, 0, 2, 2, 1],
    ],
)
# answer = solution(
#     0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
# )
print(answer)

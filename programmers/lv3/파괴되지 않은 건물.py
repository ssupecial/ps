# Level 3: 파괴되지 않은 건물
# https://school.programmers.co.kr/learn/courses/30/lessons/92344
# 10.12 실패
def solution(board, skill):
    r = len(board)
    c = len(board[0])
    history = [[0] * (c + 1) for _ in range(r + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:  # 공격
            degree = -degree

        history[r1][c1] += degree
        history[r1][c2 + 1] -= degree
        history[r2 + 1][c1] -= degree
        history[r2 + 1][c2 + 1] += degree

    for i in range(0, r + 1):
        for j in range(1, c + 1):
            history[i][j] = history[i][j - 1] + history[i][j]

    for i in range(0, c + 1):
        for j in range(1, r + 1):
            history[j][i] = history[j - 1][i] + history[j][i]

    answer = 0
    for i in range(0, r):
        for j in range(0, c):
            if board[i][j] + history[i][j] >= 1:
                answer += 1

    return answer


def solution_(board, skill):  # 정확성 통과, 효율성 시간초과
    for type, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if type == 1:
                    board[r][c] -= degree
                elif type == 2:
                    board[r][c] += degree

    answer = 0
    for r in board:
        for c in r:
            if c >= 1:
                answer += 1

    return answer


answer = solution(
    [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
    [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]],
)
answer = solution(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]],
)
print(answer)

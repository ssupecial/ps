def check(m, n, board):
    arr = []
    count = 0
    for i in range(m - 1):
        for j in range(n - 1):
            lu = board[i][j]

            if lu == "X" or lu == "Y":
                continue
            ru = board[i][j + 1]
            ld = board[i + 1][j]
            rd = board[i + 1][j + 1]
            if (lu == ru) and (ru == ld) and (ld == rd):
                arr.append([i, j])
                arr.append([i + 1, j])
                arr.append([i, j + 1])
                arr.append([i + 1, j + 1])
    for i, j in arr:
        if board[i][j] != "X":
            count += 1
            board[i][j] = "X"
    if len(arr) == 0:
        return 0
    return count


def down(m, n, board):

    for j in range(n):
        arr = []
        for i in range(m):
            if board[i][j] != "X":
                arr.append(board[i][j])
        rest_length = m - len(arr)
        for k in range(rest_length):
            board[k][j] = "X"
        for k, word in enumerate(arr):
            board[k + rest_length][j] = word


def solution(m, n, board):
    board = [list(map(str, tmp)) for tmp in board]
    answer = 0
    while True:
        result = check(m, n, board)
        if result == 0:
            break
        answer += result

        down(m, n, board)

    return answer

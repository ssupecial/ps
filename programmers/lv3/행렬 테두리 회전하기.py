# 23:00-23:20
def solution(rows, columns, queries):
    arr = [[(i - 1) * columns + j for j in range(columns + 1)] for i in range(rows + 1)]

    answer = []
    for x1, y1, x2, y2 in queries:
        result = rotation(arr, x1, y1, x2, y2)
        answer.append(result)
    return answer


def rotation(arr, x1, y1, x2, y2):
    lu = arr[x1][y1]
    ru = arr[x1][y2]
    ld = arr[x2][y1]
    rd = arr[x2][y2]

    tmp = [lu, ru, ld, rd]

    for i in range(y2 - 1, y1 - 1, -1):
        tmp.append(arr[x1][i])
        arr[x1][i + 1] = arr[x1][i]

    for i in range(x2 - 1, x1, -1):
        tmp.append(arr[i][y2])
        arr[i + 1][y2] = arr[i][y2]
    arr[x1 + 1][y2] = ru

    for i in range(y1, y2 - 1):
        tmp.append(arr[x2][i + 1])
        arr[x2][i] = arr[x2][i + 1]
    arr[x2][y2 - 1] = rd

    for i in range(x1, x2 - 1):
        tmp.append(arr[i + 1][y1])
        arr[i][y1] = arr[i + 1][y1]
    arr[x2 - 1][y1] = ld

    return min(tmp)


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])

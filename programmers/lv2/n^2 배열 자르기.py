def make_row(rownum, n):
    rownum += 1
    arr = [rownum] * rownum

    for i in range(rownum + 1, n + 1):
        arr.append(i)

    return arr


def solution(n, left, right):
    answer = []

    start_row = left // n
    start_column = left % n
    finish_row = right // n
    finish_column = right % n

    for i in range(start_row, finish_row + 1):
        row = make_row(i, n)
        start = 0
        finish = n - 1
        if i == start_row:
            start = start_column
        if i == finish_row:
            finish = finish_column
        for k in range(start, finish + 1):
            answer.append(row[k])
    return answer

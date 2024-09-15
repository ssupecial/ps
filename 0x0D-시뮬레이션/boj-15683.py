n, m = list(map(int, input().split(" ")))
board = []
cctvs = []
min_size = 999
n_unique = 8

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] != 0 and row[j] != 6:
            cctvs.append((row[j], i, j))


def print_board():
    global board
    print("==" * 20)
    for i in range(n):
        print(" ".join(map(str, board[i])))
    print("==" * 20)


cctvs_len = len(cctvs)


def check():
    global n, m, board
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1

    return count


def mark_right(x, y, n_unique):
    global board, n, m
    for j in range(y + 1, m):
        if board[x][j] == 0:
            board[x][j] = n_unique
        elif board[x][j] == 6:
            break


def mark_left(x, y, n_unique):
    global board, n, m
    for j in range(y - 1, -1, -1):
        if board[x][j] == 0:
            board[x][j] = n_unique
        elif board[x][j] == 6:
            break


def mark_up(x, y, n_unique):
    global board, n, m
    for i in range(x - 1, -1, -1):
        if board[i][y] == 0:
            board[i][y] = n_unique
        elif board[i][y] == 6:
            break


def mark_down(x, y, n_unique):
    global board, n, m
    for i in range(x + 1, n):
        if board[i][y] == 0:
            board[i][y] = n_unique
        elif board[i][y] == 6:
            break


def unmark_right(x, y, n_unique):
    for j in range(y + 1, m):
        if board[x][j] == n_unique:
            board[x][j] = 0
        elif board[x][j] == 6:
            break


def unmark_left(x, y, n_unique):
    for j in range(y - 1, -1, -1):
        if board[x][j] == n_unique:
            board[x][j] = 0
        elif board[x][j] == 6:
            break


def unmark_down(x, y, n_unique):
    for i in range(x + 1, n):
        if board[i][y] == n_unique:
            board[i][y] = 0
        elif board[i][y] == 6:
            break


def unmark_up(x, y, n_unique):
    for i in range(x - 1, -1, -1):
        if board[i][y] == n_unique:
            board[i][y] = 0
        elif board[i][y] == 6:
            break


def mark(cctv_type, direction, x, y, n_unique):
    global cctvs, n, m, boards
    if cctv_type == 1:
        if direction == 0:  # 오른쪽
            mark_right(x, y, n_unique)
        elif direction == 1:  # 왼쪽
            mark_left(x, y, n_unique)
        elif direction == 2:  # 아래
            mark_down(x, y, n_unique)
        elif direction == 3:  # 위
            mark_up(x, y, n_unique)
    elif cctv_type == 2:
        if direction == 0:  # 좌우
            mark_right(x, y, n_unique)
            mark_left(x, y, n_unique)
        elif direction == 1:  # 위아래
            mark_down(x, y, n_unique)
            mark_up(x, y, n_unique)
    elif cctv_type == 3:
        if direction == 0:  # 오른쪽 위
            mark_right(x, y, n_unique)
            mark_up(x, y, n_unique)
        elif direction == 1:  # 오른쪽 아래
            mark_right(x, y, n_unique)
            mark_down(x, y, n_unique)
        elif direction == 2:  # 왼쪽 아래
            mark_left(x, y, n_unique)
            mark_down(x, y, n_unique)
        elif direction == 3:  # 왼쪽 위
            mark_left(x, y, n_unique)
            mark_up(x, y, n_unique)
    elif cctv_type == 4:
        if direction == 0:  # 오른쪽
            mark_right(x, y, n_unique)
            mark_up(x, y, n_unique)
            mark_down(x, y, n_unique)
        elif direction == 1:  # 아래
            mark_right(x, y, n_unique)
            mark_left(x, y, n_unique)
            mark_down(x, y, n_unique)
        elif direction == 2:  # 왼쪽
            mark_left(x, y, n_unique)
            mark_up(x, y, n_unique)
            mark_down(x, y, n_unique)
        elif direction == 3:  # 위
            mark_right(x, y, n_unique)
            mark_left(x, y, n_unique)
            mark_up(x, y, n_unique)
    elif cctv_type == 5:
        mark_right(x, y, n_unique)
        mark_left(x, y, n_unique)
        mark_up(x, y, n_unique)
        mark_down(x, y, n_unique)


def unmark(cctv_type, direction, x, y, n_unique):
    global cctvs, n, m, board
    if cctv_type == 1:
        if direction == 0:  # 오른쪽
            unmark_right(x, y, n_unique)
        elif direction == 1:  # 왼쪽
            unmark_left(x, y, n_unique)
        elif direction == 2:  # 아래
            unmark_down(x, y, n_unique)
        elif direction == 3:  # 위
            unmark_up(x, y, n_unique)
    elif cctv_type == 2:
        if direction == 0:  # 좌우
            unmark_right(x, y, n_unique)
            unmark_left(x, y, n_unique)
        elif direction == 1:  # 위아래
            unmark_down(x, y, n_unique)
            unmark_up(x, y, n_unique)
    elif cctv_type == 3:
        if direction == 0:  # 오른쪽 위
            unmark_right(x, y, n_unique)
            unmark_up(x, y, n_unique)
        elif direction == 1:  # 오른쪽 아래
            unmark_right(x, y, n_unique)
            unmark_down(x, y, n_unique)
        elif direction == 2:  # 왼쪽 아래
            unmark_left(x, y, n_unique)
            unmark_down(x, y, n_unique)
        elif direction == 3:  # 왼쪽 위
            unmark_left(x, y, n_unique)
            unmark_up(x, y, n_unique)
    elif cctv_type == 4:
        if direction == 0:  # 오른쪽
            unmark_right(x, y, n_unique)
            unmark_up(x, y, n_unique)
            unmark_down(x, y, n_unique)
        elif direction == 1:  # 아래
            unmark_right(x, y, n_unique)
            unmark_left(x, y, n_unique)
            unmark_down(x, y, n_unique)
        elif direction == 2:  # 왼쪽
            unmark_left(x, y, n_unique)
            unmark_up(x, y, n_unique)
            unmark_down(x, y, n_unique)
        elif direction == 3:  # 위
            unmark_right(x, y, n_unique)
            unmark_left(x, y, n_unique)
            unmark_up(x, y, n_unique)
    elif cctv_type == 5:
        unmark_right(x, y, n_unique)
        unmark_left(x, y, n_unique)
        unmark_down(x, y, n_unique)
        unmark_up(x, y, n_unique)


def func(depth):
    global cctvs_len, cctvs, min_size, board, n_unique
    if depth == cctvs_len:
        width_blind = check()
        if min_size > width_blind:
            # print_board()
            min_size = width_blind

        return

    cctv_type = cctvs[depth][0]
    x = cctvs[depth][1]
    y = cctvs[depth][2]
    cur_unique = n_unique
    n_unique += 1

    if cctv_type == 1:
        for k in range(4):
            mark(cctv_type, k, x, y, cur_unique)
            func(depth + 1)
            unmark(cctv_type, k, x, y, cur_unique)

    elif cctv_type == 2:
        for k in range(2):
            mark(cctv_type, k, x, y, cur_unique)
            func(depth + 1)
            unmark(cctv_type, k, x, y, cur_unique)

    elif cctv_type == 3:
        for k in range(4):
            mark(cctv_type, k, x, y, cur_unique)
            func(depth + 1)
            unmark(cctv_type, k, x, y, cur_unique)

    elif cctv_type == 4:
        for k in range(4):
            mark(cctv_type, k, x, y, cur_unique)
            func(depth + 1)
            unmark(cctv_type, k, x, y, cur_unique)

    elif cctv_type == 5:
        mark(cctv_type, 0, x, y, cur_unique)
        func(depth + 1)
        unmark(cctv_type, 0, x, y, cur_unique)


func(0)
if min_size == 999:
    min_size = 0

print(min_size)

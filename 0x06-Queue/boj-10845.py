import sys

arr = list()
pos_front = 0
pos_back = 0


def push(x: int):
    global arr
    global pos_back
    arr.append(x)
    pos_back = pos_back + 1


def pop() -> int:
    global arr
    global pos_front
    global pos_back
    if pos_front != pos_back:  # 비어있지 않음
        value = arr[pos_front]
        pos_front += 1
    else:  # 비어있음
        value = -1
    return value


def size() -> int:
    global arr
    global pos_front
    global pos_back
    return pos_back - pos_front


def empty() -> int:
    if size() != 0:
        return 0
    else:
        return 1


def front() -> int:
    global arr
    global pos_front
    global pos_back
    value = arr[pos_front] if size() != 0 else -1
    return value


def back() -> int:
    global arr
    global pos_front
    global pos_back
    value = arr[pos_back - 1] if size() != 0 else -1
    return value


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    for i in range(N):
        ops = list(sys.stdin.readline().rstrip().split(" "))
        if ops[0] == "push":
            push(int(ops[1]))
        elif ops[0] == "front":
            print(front())
        elif ops[0] == "back":
            print(back())
        elif ops[0] == "pop":
            print(pop())
        elif ops[0] == "size":
            print(size())
        elif ops[0] == "empty":
            print(empty())

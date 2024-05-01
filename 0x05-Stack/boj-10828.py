import sys

arr = []
pos = 0


def push(value: int):
    global arr
    global pos
    arr.append(value)

    pos += 1


def pop() -> int:
    global arr
    global pos
    temp = arr[pos - 1]
    arr = arr[: pos - 1]
    pos -= 1
    return temp


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        ops = list(sys.stdin.readline().rstrip().split(" "))
        if ops[0] == "push":
            push(int(ops[1]))
        elif ops[0] == "top":
            print(arr[pos - 1] if pos != 0 else -1)
        elif ops[0] == "size":
            print(pos)
        elif ops[0] == "empty":
            print(1 if pos == 0 else 0)
        elif ops[0] == "pop":
            if pos == 0:
                print(-1)
            else:
                print(pop())

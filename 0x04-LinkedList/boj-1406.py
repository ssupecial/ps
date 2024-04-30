import sys


stack_left = list(sys.stdin.readline().rstrip())
stack_right = list()

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    op = list(sys.stdin.readline().split())
    if op[0] == "P":
        stack_left.append(op[1])
    elif op[0] == "L" and stack_left:
        stack_right.append(stack_left.pop())
    elif op[0] == "D" and stack_right:
        stack_left.append(stack_right.pop())
    elif op[0] == "B":
        if stack_left:
            stack_left.pop()
print("".join(stack_left) + "".join(list(reversed(stack_right))))

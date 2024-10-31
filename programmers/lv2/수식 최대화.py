def calculate(expressions, order):
    for operator in order:
        while operator in expressions:
            index = expressions.index(operator)
            a = expressions[index - 1]
            b = expressions[index + 1]

            expressions = (
                expressions[: index - 1]
                + [eval(f"{a}{operator}{b}")]
                + expressions[index + 2 :]
            )

    return expressions[0]


def solution(expression):
    expressions = []
    tmp = ""
    for c in expression:
        if c.isdigit():
            tmp += c
        else:
            expressions.append(int(tmp))
            tmp = ""
            expressions.append(c)
    expressions.append(int(tmp))

    answer = 0
    from itertools import permutations

    for orders in list(permutations(["*", "-", "+"])):
        result = calculate(expressions, orders)
        if abs(result) > answer:
            answer = abs(result)

    return answer


answer = solution("50*6-3*2")
print(answer)

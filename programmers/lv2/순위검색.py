import bisect


def solution(info, query):
    answer = []

    dicts = {
        "cpp": 0,
        "java": 1,
        "python": 2,
        "-+": 3,
        "-": 2,
        "backend": 0,
        "frontend": 1,
        "junior": 0,
        "senior": 1,
        "chicken": 0,
        "pizza": 1,
    }

    history = [
        [[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)
    ]
    for i in info:
        lan, job, level, food, score = i.replace("and", "").split()

        for j in ["-+", lan]:
            for k in ["-", job]:
                for t in ["-", level]:
                    for p in ["-", food]:
                        history[dicts[j]][dicts[k]][dicts[t]][dicts[p]].append(
                            int(score)
                        )

    for i in range(4):
        for j in range(3):
            for t in range(3):
                for k in range(3):
                    history[i][j][t][k].sort()
    answers = []
    for q in query:
        steps = []
        lan, job, level, food, score = q.replace("and", "").split()

        if lan == "-":
            lan += "+"
        results = history[dicts[lan]][dicts[job]][dicts[level]][dicts[food]]

        num = bisect.bisect_left(results, int(score))
        answers.append(len(results) - num)

    return answers

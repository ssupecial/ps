def update(tables, r, c, value):

    parent_r, parent_c = tables[r][c][1]

    for i in range(1, 51):
        for j in range(1, 51):
            if tables[i][j][1] == [parent_r, parent_c]:
                tables[i][j][0] = value


def merge(tables, r1, c1, r2, c2):

    parent_r1, parent_c1 = tables[r1][c1][1]
    parent_r2, parent_c2 = tables[r2][c2][1]

    value = (
        tables[parent_r1][parent_c1][0]
        if tables[parent_r1][parent_c1][0] != ""
        else tables[parent_r2][parent_c2][0]
    )

    for i in range(1, 51):
        for j in range(1, 51):
            if tables[i][j][1] == [parent_r2, parent_c2]:
                tables[i][j][1] = [parent_r1, parent_c1]

    for i in range(1, 51):
        for j in range(1, 51):
            if tables[i][j][1] == [parent_r1, parent_c1]:
                tables[i][j][0] = value


def unmerge(tables, r, c):
    value = tables[r][c][0]
    parent_r, parent_c = tables[r][c][1]

    for i in range(1, 51):
        for j in range(1, 51):
            if tables[i][j][1] == [parent_r, parent_c]:
                tables[i][j][0] = ""
                tables[i][j][1] = [i, j]

    tables[r][c][0] = value


def solution(commands):
    answer = []
    tables = [[["", [j, i]] for i in range(51)] for j in range(51)]
    for command in commands:
        words = command.split()
        if words[0] == "UPDATE" and len(words) == 4:
            update(tables, int(words[1]), int(words[2]), words[3])

        elif words[0] == "UPDATE" and len(words) == 3:
            for i in range(1, 51):
                for j in range(1, 51):
                    if tables[i][j][0] == words[1]:
                        tables[i][j][0] = words[2]

        elif words[0] == "MERGE" and not (
            words[1] == words[3] and words[2] == words[4]
        ):
            merge(tables, int(words[1]), int(words[2]), int(words[3]), int(words[4]))

        elif words[0] == "UNMERGE":
            unmerge(tables, int(words[1]), int(words[2]))

        elif words[0] == "PRINT":
            value = tables[int(words[1])][int(words[2])][0]
            if value == "":
                answer.append("EMPTY")
            else:
                answer.append(value)

    return answer


answer = solution(
    [
        "UPDATE 1 1 menu",
        "UPDATE 1 2 category",
        "UPDATE 2 1 bibimbap",
        "UPDATE 2 2 korean",
        "UPDATE 2 3 rice",
        "UPDATE 3 1 ramyeon",
        "UPDATE 3 2 korean",
        "UPDATE 3 3 noodle",
        "UPDATE 3 4 instant",
        "UPDATE 4 1 pasta",
        "UPDATE 4 2 italian",
        "UPDATE 4 3 noodle",
        "MERGE 1 2 1 3",
        "MERGE 1 3 1 4",
        "UPDATE korean hansik",
        "UPDATE 1 3 group",
        "UNMERGE 1 4",
        "PRINT 1 3",
        "PRINT 1 4",
    ]
)
print(answer)

answer = solution(
    [
        "UPDATE 1 1 a",
        "UPDATE 1 2 b",
        "UPDATE 2 1 c",
        "UPDATE 2 2 d",
        "MERGE 1 1 1 2",
        "MERGE 2 2 2 1",
        "MERGE 2 1 1 1",
        "PRINT 1 1",
        "UNMERGE 2 2",
        "PRINT 1 1",
    ]
)

print(answer)

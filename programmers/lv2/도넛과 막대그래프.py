def solution(edges):
    in_counts = [0] * (1000000 + 1)
    out_counts = [0] * (1000000 + 1)

    vertexes = []
    for edge in edges:
        f, t = edge
        vertexes.append(f)
        vertexes.append(t)

        in_counts[t] += 1
        out_counts[f] += 1

    vertexes = list(set(vertexes))
    donut = 0
    straight = 0
    eight = 0
    con_vertex = -1

    for key in vertexes:
        if out_counts[key] == 0:
            straight += 1
        elif out_counts[key] == 2:
            if in_counts[key] == 0:
                con_vertex = key
            else:
                eight += 1
        elif out_counts[key] > 2:
            con_vertex = key

    total = out_counts[con_vertex]
    donut = total - (straight + eight)

    return [con_vertex, donut, straight, eight]


answer = solution(
    [
        [4, 11],
        [1, 12],
        [8, 3],
        [12, 7],
        [4, 2],
        [7, 11],
        [4, 8],
        [9, 6],
        [10, 11],
        [6, 10],
        [3, 5],
        [11, 1],
        [5, 3],
        [11, 9],
        [3, 8],
    ]
)
print(answer)

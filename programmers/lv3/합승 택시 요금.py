def find_path(next_edge, cur_edges, edges, dest):
    if next_edge == dest:
        return


def solution(n, s, a, b, fares):
    edges = {}
    for fare in fares:
        e1, e2, fee = fare
        edges[e1] = edges.get(e1, []).append([e2, fee])
        edges[e2] = edges.get(e2, []).append([e1, fee])

    answer = 0
    return answer

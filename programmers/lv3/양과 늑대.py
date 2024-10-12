def solution(info, edges):

    visited = [False] * len(info)
    visited[0] = True
    global max_sheep
    max_sheep = 0

    def func(sheep, wolf):
        global max_sheep
        if sheep > wolf:
            if sheep > max_sheep:
                max_sheep = sheep
        else:  # 같아지면 불가능
            return

        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child] = True
                if info[child] == 0:
                    func(sheep + 1, wolf)
                else:
                    func(sheep, wolf + 1)
                visited[child] = False

    func(1, 0)
    return max_sheep


# solution(
#     [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#     [
#         [0, 1],
#         [1, 2],
#         [1, 4],
#         [0, 8],
#         [8, 7],
#         [9, 10],
#         [9, 11],
#         [4, 3],
#         [6, 5],
#         [4, 6],
#         [8, 9],
#     ],
# )

solution(
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
)

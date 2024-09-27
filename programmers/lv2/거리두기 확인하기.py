# 01:25
def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_adj_people(people):  # people 좌표 목록 받아서 거리가 2이하인 쌍
    arr = []
    for i in range(len(people) - 1):
        for j in range(i + 1, len(people)):
            dist = distance(people[i], people[j])
            if dist <= 2:
                arr.append((people[i], people[j]))

    return arr


def check(place, people1, people2):
    x1, y1 = people1
    x2, y2 = people2

    if x1 == x2:  # 같은 행에 있는 경우
        if abs(y1 - y2) == 1:
            return False
        elif place[x1][(y1 + y2) // 2] == "X":
            return True
        else:
            return False

    elif y1 == y2:  # 같은 열에 있는 경우
        if abs(x1 - x2) == 1:
            return False
        elif place[(x1 + x2) // 2][y1] == "X":
            return True
        else:
            return False

    else:
        if place[x1][y2] == "X" and place[x2][y1] == "X":
            return True
        else:
            return False


def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people.append([i, j])

        arr = get_adj_people(people)
        corr = 1
        for comb in arr:
            if not check(place, comb[0], comb[1]):
                corr = 0
                break
        answer.append(corr)

    return answer


solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)

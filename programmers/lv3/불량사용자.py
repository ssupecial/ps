def check(ban, target):
    if len(ban) != len(target):
        return False

    for i in range(len(ban)):
        if ban[i] == "*":
            continue
        if ban[i] != target[i]:
            return False

    return True


result = []
is_used = []
cur = []


def func(depth):
    global len_banned, result, cur, is_used, banned_users_per_id, dicts_uid
    if depth == len_banned:
        tmp = set(cur)
        if tmp not in result:
            result.append(tmp)
        return

    if banned_users_per_id[depth] == []:
        return
    for uid in banned_users_per_id[depth]:
        if not is_used[dicts_uid[uid]]:
            cur.append(dicts_uid[uid])
            is_used[dicts_uid[uid]] = True
            func(depth + 1)
            cur.pop()
            is_used[dicts_uid[uid]] = False


def solution(user_id, banned_id):
    global banned_users_per_id, dicts_uid
    dicts_uid = {}
    banned_users_per_id = [[] for _ in range(len(banned_id))]
    for i, uid in enumerate(user_id):
        dicts_uid[uid] = i
        for j, bid in enumerate(banned_id):
            if check(bid, uid):
                banned_users_per_id[j].append(uid)

    global len_banned, is_used
    len_banned = len(banned_id)
    is_used = [False] * len(user_id)

    func(0)

    return len(result)


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
answer = solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
)

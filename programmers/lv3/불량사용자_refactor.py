def is_match(ban, target):
    """ban 문자열과 target 문자열이 일치하는지 확인하는 함수"""
    if len(ban) != len(target):
        return False

    for b_char, t_char in zip(ban, target):
        if b_char == "*":
            continue
        if b_char != t_char:
            return False

    return True


def search_combi(
    depth,
    users_per_banned_id,
    user_to_index,
    is_used,
    current_combination,
    all_combinations,
):
    if depth == len(users_per_banned_id):
        tmp = set(current_combination)
        if tmp not in all_combinations:
            all_combinations.append(tmp)
        return

    if users_per_banned_id[depth] == []:
        return
    for uid in users_per_banned_id[depth]:
        if not is_used[user_to_index[uid]]:
            current_combination.append(user_to_index[uid])
            is_used[user_to_index[uid]] = True
            search_combi(
                depth + 1,
                users_per_banned_id,
                user_to_index,
                is_used,
                current_combination,
                all_combinations,
            )
            current_combination.pop()
            is_used[user_to_index[uid]] = False


def solution(user_id, banned_id):
    user_to_index = {uid: i for i, uid in enumerate(user_id)}
    users_per_banned_id = [[] for _ in range(len(banned_id))]

    # 각 금지된 ID에 매칭되는 유저 찾기
    for i, bid in enumerate(banned_id):
        for uid in user_id:
            if is_match(bid, uid):
                users_per_banned_id[i].append(uid)

    is_used = [False] * len(user_id)
    all_combinations = []
    current_combination = []
    search_combi(
        0,
        users_per_banned_id,
        user_to_index,
        is_used,
        current_combination,
        all_combinations,
    )

    return len(all_combinations)


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
answer = solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]
)

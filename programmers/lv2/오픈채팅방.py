# 오픈채팅방
# https://school.programmers.co.kr/learn/courses/30/lessons/42888?language=python3


def solution(records):
    messages = []
    nicknames = {}
    for record in records:
        words = record.split()
        action = words[0]
        if action == "Enter":
            uid = words[1]
            nickname = words[2]
            messages.append((uid, "님이 들어왔습니다."))
            nicknames[uid] = nickname
        elif action == "Leave":
            uid = words[1]
            messages.append((uid, "님이 나갔습니다."))
        elif action == "Change":
            uid = words[1]
            nickname = words[2]
            nicknames[uid] = nickname

    answer = [f"{nicknames[uid]}{action}" for uid, action in messages]

    return answer

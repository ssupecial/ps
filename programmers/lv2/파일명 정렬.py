def convert(s, step):
    i = 0
    len_s = len(s)
    while not s[i].isdigit():
        i += 1
    word = s[:i].lower()

    j = i
    while j < len_s and s[j].isdigit():
        j += 1
    num = int(s[i:j])
    tail = s[j:]
    return (word, num, step, tail, s)


# 15:50~16:00
def solution(files):
    arr = []
    for i, file in enumerate(files):
        arr.append(convert(file, i))

    arr.sort(key=lambda x: (x[0], x[1], x[2]))
    answer = [value[-1] for value in arr]
    return answer


answer = solution(
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
)
print(answer)

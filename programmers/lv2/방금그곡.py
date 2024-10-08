def time_convert(s):
    h, m = map(int, s.split(":"))
    return h * 60 + m


def convert_shap(s):
    return (
        s.replace("C#", "c")
        .replace("D#", "d")
        .replace("F#", "f")
        .replace("G#", "g")
        .replace("A#", "a")
        .replace("B#", "b")
        .replace("E#", "e")
    )


def solution(m, musicinfos):
    arr = []
    for i, musicinfo in enumerate(musicinfos):
        start_time, end_time, song, music = musicinfo.split(",")
        duration = time_convert(end_time) - time_convert(start_time)
        music = convert_shap(music)
        music_len = len(music)
        if duration > music_len:
            music = music * (duration // music_len + 1)
        music = music[:duration]

        arr.append([music, duration, song, i])

    m = convert_shap(m)
    result = []
    for music, duration, song, index in arr:
        if m in music:
            result.append([duration, index, song])
    answer = (
        sorted(result, key=lambda x: (x[0], -x[1]), reverse=True)[0][2]
        if len(result) != 0
        else "(None)"
    )

    return answer


# solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
# solution("ABC", ["12:14,15:00,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
# solution("ABC#D", ["04:00,04:03,NAME,ABC#D"])
# solution("CDCDF", ["13:50,14:02,WORLD,CDCDCDF"])
# solution("A", ["12:00,12:01,Song,BA"])
# solution("BA", ["12:00,12:03,Song,AB"])
# solution("A", ["12:00,12:01,Sing,A", "12:00,12:02,Song,A"])

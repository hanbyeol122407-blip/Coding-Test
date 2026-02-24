def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == 'l':
            answer += "I"
        elif letter =="w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter =="O":
            answer += "0"
        else:
            answer += letter
    if len(answer) < 3:
        while len(answer) < 4:
    # for i in range(4-len(answer)):
    # while len(answer) < 4:
            answer += "o"
            # answer = f'{answer:o<4}'
    if len(answer) > 8:
        answer = answer[:8]
    return answer

# 테스트 케이스
print(solution("WORLDworld"))
print(solution("GO"))
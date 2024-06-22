# range(start, stop, step) -- step : 간격
# cipher안에 code번째 위치에 있는 str 값만 추출하면 됨

def solution(cipher, code):
    answer = ""
    for i in range(code - 1, len(cipher), code):
        answer += cipher[i]
    return answer

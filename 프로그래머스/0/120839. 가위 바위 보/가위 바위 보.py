def solution(rsp):
    answer = ''
    
    # 대응 관계 설정
    win_map = {
        '2': '0',  # 가위(2)를 이기는 것은 바위(0)
        '0': '5',  # 바위(0)를 이기는 것은 보(5)
        '5': '2'   # 보(5)를 이기는 것은 가위(2)
    }
    
    for char in rsp:
        answer += win_map[char]
    
    return answer

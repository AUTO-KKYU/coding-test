# start_num과 end_num 사이의 숫자를 가져와서 추가
# 반복문 사용하여 추가해야 하고 범위 주의
# range 범위의 number를 계속 추가

def solution(start_num, end_num):
    answer = []
    
    for num in range(start_num, end_num + 1):
        answer.append(num)
    
    return answer
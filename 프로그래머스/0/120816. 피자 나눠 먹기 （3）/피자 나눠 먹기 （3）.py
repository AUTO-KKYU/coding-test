def solution(slice, n):
    # 사람 수를 피자 조각 수로 나눈 몫
    answer = n // slice
    
    # 나머지가 있으면 피자 한 판을 더 추가
    if n % slice != 0:
        answer += 1
    
    return answer
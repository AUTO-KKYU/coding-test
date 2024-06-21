# ex) n이하 정수 중에 홀수 인것만 추출하여 배열에 저장

def solution(n):
    answer = []
    
    for i in range(1, n+1):
        if i % 2 == 1:
          answer.append(i)

    return answer
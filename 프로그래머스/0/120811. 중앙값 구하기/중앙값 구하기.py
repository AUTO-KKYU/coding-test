# 먼저 배열 내부를 정렬
# 중앙값 계산 원리
# 배열안의 원소의 개수가 홀수이면 가운데값이 중앙값
# 배열안의 원소의 개수가 짝수이면 가운데 두 값의 평균이 중앙값
# // 를 활용하여 정수 나눗셈 원리 이용 

def solution(array):
    array.sort()
    n = len(array)
    
    if n % 2 == 1:  # 배열의 길이가 홀수인 경우
        return array[n // 2]
    else:  # 배열의 길이가 짝수인 경우
        mid1 = array[n // 2 - 1]
        mid2 = array[n // 2]
        return (mid1 + mid2) / 2

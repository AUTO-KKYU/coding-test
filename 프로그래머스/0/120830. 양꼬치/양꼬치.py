def solution(n, k):
    result = n * 12000 + k * 2000
    service = n // 10
    result -= service * 2000  
    return result

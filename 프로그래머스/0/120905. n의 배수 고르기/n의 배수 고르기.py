def solution(n, numlist):
    answer = []
    
    for index in numlist:
        if index % n == 0:
            answer.append(index)  
    
    return answer
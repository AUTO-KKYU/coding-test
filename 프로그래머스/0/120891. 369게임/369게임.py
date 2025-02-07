def solution(order):
    count = 0
    
    for num in str(order):
        if num in '369':
            count +=1
    return count
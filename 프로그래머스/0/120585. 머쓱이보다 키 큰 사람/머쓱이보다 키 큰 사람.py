def solution(array, height):
    count = 0
    
    for index in array:
        if index > height:
            count += 1
        else:
            count = 0
    return count 
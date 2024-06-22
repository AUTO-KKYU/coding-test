def solution(array):
    frequency = {}
    
    # 빈도수 계산
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 최빈값 찾기
    max_count = 0
    mode = None
    multiple_modes = False
    
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = num
            multiple_modes = False
        elif count == max_count:
            multiple_modes = True
    
    if multiple_modes:
        return -1
    else:
        return mode

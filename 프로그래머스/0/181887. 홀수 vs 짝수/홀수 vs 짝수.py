def solution(num_list):
    sum_odd = 0 
    sum_even = 0  
    
    for idx, num in enumerate(num_list):
        if (idx + 1) % 2 == 1: 
            sum_odd += num
        else: 
            sum_even += num

    return max(sum_odd, sum_even)  

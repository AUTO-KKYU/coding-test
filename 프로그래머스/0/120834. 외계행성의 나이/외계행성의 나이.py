def solution(age):
    answer = ''
    num_to_alpha = "abcdefghij"  
    for digit in str(age):  
        answer += num_to_alpha[int(digit)] 
    return answer

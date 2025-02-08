def solution(s1, s2):
    answer = 0
    
    for str1 in s1:
        if str1 in s2:
            answer += s1.count(str1)
    return answer
            

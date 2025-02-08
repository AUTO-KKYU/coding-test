def solution(s):
    answer = True
    # 문자열 s에서 p와 개수와 y 개수가 같으면 true 다르면 false 
    # 대문사 소문자 구별 x
    s = s.lower()
    
    for char in s:
        if s.count('p') == s.count('y'):
            return True
        else:
            return False
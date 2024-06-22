# str.isdigit() : 문자열 안에 숫자 체크
# str.isdecimal() : 문자열 안에 정수 체크
# str.isalpha() : 문자열 안에 알파벳 체크

def solution(my_string):
    answer = 0
    
    for char in my_string:
        if char.isdigit():  # 문자가 숫자인지 확인
            answer += int(char)  # 숫자를 정수로 변환하여 합산
    
    return answer

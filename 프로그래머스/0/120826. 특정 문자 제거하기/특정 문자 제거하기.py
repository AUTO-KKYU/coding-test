def solution(my_string, letter):
    answer = ''.join(char for char in my_string if char not in letter)
    return answer
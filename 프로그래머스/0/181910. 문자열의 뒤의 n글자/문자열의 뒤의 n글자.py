def solution(my_string, n):
    len_str = len(my_string)
    
    if len_str == n:
        return my_string
    else:
        return my_string[-n:]

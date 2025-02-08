def solution(x):
    a = sum(map(int, str(x)))
    
    if x % a == 0:
        return True
    else:
        return False

def solution(sides):
    a, b, c = sorted(sides)
    
    if c < a + b:
        return 1
    else:
        return 2
            
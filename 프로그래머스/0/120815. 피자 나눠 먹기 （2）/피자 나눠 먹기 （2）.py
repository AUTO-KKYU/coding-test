def solution(n):
    slices = 6
    pizza = 1
    
    while (slices * pizza) % n != 0:
        pizza += 1
        
    return pizza
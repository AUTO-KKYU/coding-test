def solution(seoul):
    for i, name in enumerate(seoul):  
        if name == "Kim":
            return f"김서방은 {i}에 있다" 
    return None 

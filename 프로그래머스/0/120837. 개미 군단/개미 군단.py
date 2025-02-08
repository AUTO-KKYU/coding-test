def solution(hp):
    general_ants = hp // 5
    hp = hp % 5  # 남은 체력
    
    soldier_ants = hp // 3
    hp = hp % 3  # 남은 체력
    
    worker_ants = hp
    
    # 총 필요한 개미 수
    return general_ants + soldier_ants + worker_ants

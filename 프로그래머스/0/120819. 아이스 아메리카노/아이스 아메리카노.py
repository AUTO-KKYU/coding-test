# 단순한 문제 -> 복잡하게 생각 x
# 5,500원 가지고 살 수 있는 잔 수와 남은 돈만 파악하면 되므로
# 몫, 나머지 구조와 같음 

def solution(money):
    # divmod를 사용하여 몫(a)과 나머지(b)를 계산
    a, b = divmod(money, 5500)
    # 결과를 배열에 담아 반환
    return [a, b]

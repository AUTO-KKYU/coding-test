# 방법 1
# import math

# def solution(n):
#     return math.ceil(n / 7)

# 방법 2
def solution(n):
    # n을 7로 나눈 몫과 나머지를 구함
    # quotient : 몫 , remainder : 나머지
    quotient, remainder = divmod(n, 7)
    # 나머지가 0이 아니면 피자 1판 추가
    if remainder != 0:
        quotient += 1
    return quotient
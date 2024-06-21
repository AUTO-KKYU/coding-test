# 조건문의 순서가 중요함
# 만약에 100000이 처음에 if문으로 들어간다면 나머지 300000과 500000은 모두 만족하기 때문에
# 100000에 대한 결과값이 그대로 들어감

def solution(price):
    if price >= 500000:
        price = price - price * 0.20 # price -= price * 0.20
    elif price >= 300000:
        price = price - price * 0.10 # price -= price * 0.10
    elif price >= 100000:
        price = price - price * 0.05 # price -= price * 0.05
    return int(price)
        

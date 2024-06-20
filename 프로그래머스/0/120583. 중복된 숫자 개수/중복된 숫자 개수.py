# 방법 1
def solution(array, n):
    count = 0
    for element in array:
        if element == n:
            count += 1
    return count


# 방법 2

# def solution(array, n):
#     return array.count(n)

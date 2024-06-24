# max() : () 중 최대값 반환
# min() : () 중 최소값 반환
# index() : ()에 위치 찾기 , 중복된 값이 있을 시 가장 최소의 위치 리턴

def solution(array):
    
    max_value = max(array)
    max_index = array.index(max_value) # array에서 max_value의 index 찾기

    return [max_value, max_index]
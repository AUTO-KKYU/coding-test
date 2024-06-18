# index_list에 있는 인덱스 중에 my_string에 있으면 추가

def solution(my_string, index_list):
    answer = ""
    for index in index_list:
        answer += my_string[index]
    return answer
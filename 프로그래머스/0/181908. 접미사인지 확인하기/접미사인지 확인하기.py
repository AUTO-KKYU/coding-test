# is_suffix의 길이만큼 비교하여 접미사 확인
# ex) is_suffix : ana , 3
# len_s = 3
# check = my_string[-3:] = ana

def solution(my_string, is_suffix):
    len_s = len(is_suffix)
    check = my_string[-len_s:]
    

    if check == is_suffix:
        return 1  # 접미사가 맞다면 1을 반환
    else:
        return 0  # 접미사가 아니라면 0을 반환
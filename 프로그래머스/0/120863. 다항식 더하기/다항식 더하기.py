def solution(polynomial):
    numberlist = polynomial.split()

    x= 0 #x앞의 수를 저장할 수
    s= 0 #상수항
    
    for i in numberlist:
        if i[-1] == "x":
            if i[:-1]: #x의 앞에 수가 있을때
                x += int(i[:-1])
            else:
                x += 1 #x의 앞에 수가 없으면 계수가 1이라서 1더하기
        elif i.isdigit(): #숫자형태인지 확인하는 메서드
            s += int(i)

    if x == 1:
        if s > 0 :
            return f"x + {s}"
        else: 
            return f"x"
    elif x > 1:
        if s > 0:
            return f"{x}x + {s}"
        else:
            return f"{x}x"
    else:
        return f"{s}"
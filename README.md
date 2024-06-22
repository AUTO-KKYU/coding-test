# coding-test
코딩 테스트 저장소

*Python3 Coding test tip!*

- 문자열 뒤집기
```sh
string = "Welcome Github!"
print(string[::-1])

# result : !buhtiG emocleW"
```
- 중복 제거
```sh
list = [1,1,2,2,3,4,4,5]
print(list(set(temp)))

# result : [1,2,3,4,5]
```
- 한 줄에 여러 정수(int) or 실수(float) 입력받기
```sh
temp_list = list(map(int, input().split()))
print(temp_list)

# input : 34 2 566 4 7 8 11
# output : [34, 2, 566, 4, 7, 8, 11]
```

- grammer check
```sh
# java & c
if (0 < n && n < 10)
# python
if 0 < n < 10:
```
- 두 변수 값 바꾸기
```sh
a, b = b, a
```

- list의 원소들을 차례로 순회할 때 인덱스까지 가져오기
```sh
temp = ['k', 'o', 'r', 'e', 'a']

for idx, value in enumerate(temp):
    print(idx, value)

# result : 0 'k' 1 'o' ...
```

- 길이가 같은 두 개 이상의 iterable 객체를 동시에 for문 돌리기
```sh
temp1 = [1,2,3]
temp2 = [4,5,6]

for n1, n2 in zip(temp1, temp2):
  print(n1, n2)

# result : 1 2 3 4 5 6
```

- 2차원 리스트 열 추출
```sh
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = list(zip(*a))[0]
print(b)
# (1, 4, 7)

c = list(zip(*a))[1]
print(c)
# (2, 5, 8)

d = list(zip(*a))[2]
print(d)
# (3, 6, 9)
```

- 2차원 리스트 복사
```sh
import copy

# 2차원 배열 생성
original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 얕은 복사
shallow_copied = original[:]
shallow_copied[0][0] = 999
print("얕은 복사 후 원본 배열:", original)  # 변경됨!

# 깊은 복사
deep_copied = copy.deepcopy(original)
deep_copied[0][0] = 111
print("깊은 복사 후 원본 배열:", original)  # 변경되지 않음!
print("깊은 복사된 배열:", deep_copied)
```

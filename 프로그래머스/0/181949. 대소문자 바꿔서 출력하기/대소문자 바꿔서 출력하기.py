str = input()
result = ""

for char in str:
    if 'A' <= char <= 'Z':
        result += char.lower()
    elif 'a' <= char <= 'z':
        result += char.upper()
    else:
        result += char
    

print(result)


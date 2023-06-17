
S = input()
T = input()


flag = False

while T:
    # A 제거
    if T[-1] == 'A':
        T = T[:-1]
    # B 제거, 뒤집기
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    
    if T == S:
        flag = True
        break

if flag:
    print(1)
else:
    print(0)

N = int(input())

serial = []

for _ in range(N):
    serial.append(input())


def num(x):
    sum = 0
    for i in x:
        # 숫자인 경우
        if i.isdigit():
            sum += int(i)
    return sum

# 길이 순 정렬, 숫자의 합 정렬, 사전 순 정렬
serial.sort(key=lambda x : (len(x), num(x), x))

for s in serial:
    print(s)
N = sorted(list(input()), reverse= True)

# 각 자리 수의 합이 3으로 나누어떨어지면 3의 배수
# 30으로 나누어 떨어지려면 마지막에 0이 있어야 한다.

ans = -1

num = int(''.join(N))

if num % 30 == 0:
    ans = num

print(ans)
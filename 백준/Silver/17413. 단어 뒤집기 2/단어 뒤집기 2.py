S = input()

result = ""
tmp = ""
flag = False

for w in S:
    if flag : 
        # 괄호 영역
        tmp += w
        if w == '>':
            result += tmp
            tmp = ""
            flag = False
    else:
        if w == '<':
            flag = True
            tmp += w
        elif w == ' ':
            tmp += w
            result += tmp
            tmp = ""
        else:
            tmp = w + tmp

        
print(result + tmp)
def solution(polynomial):
    tmp = list(polynomial.split())
    a, b = 0, 0
    for i in range(len(tmp)) :
        if 'x' in tmp[i] :
            if tmp[i][:-1] == "" :
                a += 1
            else :
                a += int(tmp[i][:-1])
        elif tmp[i] != "+" :
            b += int(tmp[i])
            
    if a == 0:
        answer = str(b)
    elif b == 0:
        answer = f"{a}x" if a != 1 else "x"
    else:
        answer = f"{a}x + {b}" if a != 1 else f"x + {b}"
    return answer
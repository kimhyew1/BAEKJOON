def solution(s1, s2) :
    n = len(s1)
    cnt = 0
    for i in range(n) :
        if s1[i] in s2 :
            cnt += 1
    return cnt
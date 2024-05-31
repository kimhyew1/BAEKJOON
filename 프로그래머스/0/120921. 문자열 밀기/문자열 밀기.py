def solution(A, B) :
    i = 0 
    n = len(A)
    answer = -1
    while i <= n :
        if A == B :
            answer = i
            break
        else :
            A = A[-1] + A[:-1]
            i += 1
    if (A != B) & (i == n) :
        answer = -1
    return answer
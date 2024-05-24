def solution(common) :
    n = len(common)
    diff = []
    for i in [0, 1] :
        diff.append(common[i+1] - common[i])
    if diff[0] == diff[1] :
        answer = common[n-1] + diff[0]
    else :
        answer = common[n-1] * (common[1] / common[0])
    return answer
def solution(arr, query) :
    answer = arr.copy()
    for ind in range(len(query)) :
        i = query[ind]
        if ind%2 == 0 :
            answer = answer[:i+1]
        else :
            answer = answer[i:]
    return answer
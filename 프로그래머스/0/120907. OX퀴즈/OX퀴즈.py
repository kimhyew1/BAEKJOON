def solution(quiz):
    answer = []
    for i in range(len(quiz)) :
        newquiz = list(quiz[i].split())
        real = int(newquiz[-1])
        tmp = "X"
        if newquiz[1] == "+" :
            infer = int(newquiz[0]) + int(newquiz[2])
        else :
            infer = int(newquiz[0]) - int(newquiz[2])
        if real == infer :
            tmp = "O"
        answer.append(tmp)
    return answer
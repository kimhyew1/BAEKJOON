def solution(l, r) :
    answer = []
    for num in range(l, r+1) :
        string = str(num)
        flag = True
        for i in string :
            if i != '0' and i != '5' :
                flag = False
                break
        if flag :
            answer.append(num)
    
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer
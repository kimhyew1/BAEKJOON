def solution(score) :
    avg_list = []
    rnk = 1
    for i in range(len(score)) :
        avg = (score[i][0] + score[i][1]) / 2
        avg_list.append([i+1, avg, rnk])
    avg_list = sorted(avg_list, key = lambda x: x[1],reverse=True)
    answer = []
    
    tmp = avg_list[0][1]
    for idx in range(len(score)-1) :
        if avg_list[idx+1][1] == tmp :
            avg_list[idx+1][2] = avg_list[idx][2]
        else :
            avg_list[idx+1][2] = idx+2
        tmp = avg_list[idx+1][1]
    avg_list = sorted(avg_list, key = lambda x: x[0])
    
    for ans in range(len(score)) :
        answer.append(avg_list[ans][2])
    
    return answer
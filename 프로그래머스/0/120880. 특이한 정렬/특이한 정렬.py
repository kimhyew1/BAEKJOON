def solution(numlist, n) :
    numlist = sorted(numlist, reverse=True)
    answer = []
    n_list = list()
    
    for i in range(len(numlist)) :
        diff = numlist[i] - n
        n_list.append([numlist[i], diff])
    n_list = sorted(n_list, key = lambda x: abs(x[1]), reverse = False)
    
    for idx in range(len(numlist)) :
        answer.append(n_list[idx][0])
    return answer
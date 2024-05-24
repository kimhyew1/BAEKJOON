def solution(num, total) :
    x = total/num - 1/2 * (num-1) 
    answer = []
    for i in range(num) :
        answer.append(x+i)
    return answer
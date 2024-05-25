def solution(myString, pat) :
    answer = 0
    pat = list(pat)
    newpat = ""
    for i in range(len(pat)) :
        if pat[i] == "A" :
            pat[i] = "B"
        else :
            pat[i] = "A"
    for j in range(len(pat)) :
        newpat += pat[j]
    if newpat in myString :
        answer = 1
    return answer
def solution(hp) :
    ant1 = hp // 5
    hp -= 5 * ant1
    ant2 = hp // 3
    ant3 = hp - 3 * ant2
    answer = ant1 + ant2 + ant3
    
    return answer
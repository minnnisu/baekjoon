def solution(t, p):
    answer = 0

    for start in range(len(t) - len(p) + 1):
        end = start + len(p)
        if(int(t[start:end]) <= int(p)):
            answer += 1
    
    return answer

print(solution("3141592", "271"))
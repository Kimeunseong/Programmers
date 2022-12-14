# 삼총사

# (문제 생략)

import itertools

def solution(number):
    answer = 0
    while number:
        n = number.pop() 
        for i in list(itertools.permutations(number, 2)):
            if sum(i) == n*(-1):
                answer += 1
                
    return answer // 2

print(solution([-2, 3, 0, 2, -5])) # 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 5
print(solution([-1, 1, -1, 1])) # 0
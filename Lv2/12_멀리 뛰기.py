# 멀리 뛰기

# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 
# 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# 1차시도 - 실패(시간초과)

import itertools

def solution(n):
    cnt1 = n % 2    # 1
    cnt2 = n // 2   # 2
    result = 0
    
    while cnt2 >= 0:
        arr = []
        for i in range(cnt1):
            arr.append(1)
        for i in range(cnt2):
            arr.append(2)

        result += len(set(itertools.permutations(arr, len(arr))))

        cnt1 += 2
        cnt2 -= 1
    
    return result

print(solution(3))
print(solution(4))
print(solution(5))
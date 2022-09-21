# 정수 제곱근 판별

# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# n = 121일 경우, 11의 제곱이므로, (11+1)의 제곱인 144가 리턴값이다.
# n = 3일 경우, 제곱이 아니므로, -1이 리턴값이다.

import math

def solution(n):
    if ((math.sqrt(n) * 10) % 10) == 0:
        return (int(math.sqrt(n)) + 1)**2
    else:
        return -1
        

num = 3
print(solution(num))
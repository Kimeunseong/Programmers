# 두 정수 사이의 합

# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.


def solution(a, b):
    if a == b :
        return a
    elif a < b:
        return sum(range(a, b+1))
    else:
        return sum(range(b, a+1))
    
# 다른 방법 - 등차수열의 합공식 이용

def solution2(a, b):
    if a == b:
        return a
    elif a < b:
        return (b-a+1)*(a+b) // 2
    else:
        return (a-b+1)*(b+a) // 2
    
print(solution(-3, 5)) # 12
print(solution(3, 3)) # 3
print(solution(5, 3)) # 12
print()
print(solution2(-3, 5)) # 12
print(solution2(3, 3)) # 3
print(solution2(5, 3), type(solution2(5, 3))) # 12
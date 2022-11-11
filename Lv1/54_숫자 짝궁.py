# 숫자 짝꿍

# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다.
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다.
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해세요.

def solution(X, Y):
    num = ''
    dict_x = {}
    dict_y = {}

    for i in X:
        dict_x[i] = 0
    for i in Y:
        dict_y[i] = 0

    for i in X:
        dict_x[i] += 1
    for i in Y:
        dict_y[i] += 1

    for i in sorted(dict_x, reverse=True):
        if i in dict_y:
            num += i * dict_y[i]
    
    if len(num) == 0:
        return '-1'
    elif int(num) == 0:
        return '0'
    else:
        return num

print(solution("100", "2345")) # '-1'
print(solution("100", "203045")) # '0'
print(solution("100", "123450")) # '10'
print(solution("12321", "42531")) # '321'
print(solution("5525", "1255")) # '552'

# 3개 틀림, 5개 시간초과.
# 52.6 / 100.0
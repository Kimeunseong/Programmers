# 숫자 짝꿍

# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다.
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다.
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해세요.

def solution(X, Y):
    num = ''
    dict_x = {'9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0}
    dict_y = {'9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0}
    dict_x2 = {}

    for i in X:
        dict_x[i] += 1
    for i in Y:
        dict_y[i] += 1
        
    for i in dict_x.keys():
        if dict_x[i] != 0:
            dict_x2[i] = dict_x[i]

    for i in dict_x2.keys():
        num += i * dict_y[i] if dict_x[i] >= dict_y[i] else i * dict_x[i]
    
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
print(solution('10000000000000001000001', '10000000000000001111111111111100000000000'))

# 5개 시간초과(11~15)
# 합계: 73.7 / 100.0
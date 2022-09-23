# 시저 암호

# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

def solution(s, n):
    answer = ''
    
    for i in s:
        alpabet = ord(i)
        
        if alpabet == 32:  # 0. 공백 확인하기
            answer += i
        elif i.isupper(): # 1. 대소문자 판별하기 - 대문자 : 65~90
            answer += chr(alpabet + n - 26) if alpabet + n > 90 else chr(alpabet + n)
        else:          # 1. 대소문자 판별하기 - 소문자 : 97~122
            answer += chr(alpabet + n - 26) if alpabet + n > 122 else chr(alpabet + n)

    return answer
    
print(solution('AB', 1)) # "BC"
print(solution("z", 1)) # "a"
print(solution('a B z', 4)) # "e F d"
print(solution('ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz', 25))
print(solution('abcdefghijklmnopqrstuvwxyz    ', 1))

# 후기 - 와우.. 역대급으로 오래 걸린 문제ㅋㅋㅋㅋ 대문자 소문자를 구분 해야하는걸 왜 생각을 못했을까ㅋㅋ 아무튼 힌트없이 해결했다ㅎ
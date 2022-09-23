# 3진법 뒤집기

# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    temp = '' # 1. n을 3진법으로 바꿈 => temp에 저장
    while n:
        temp = str(n % 3) + temp
        n = n // 3
    temp = temp[::-1] # 2. temp 뒤집는다
    return int(temp, 3) # 3. 뒤집힌 temp를 10진법으로 변환

print(solution(45)) # 7
print(solution(125)) # 229
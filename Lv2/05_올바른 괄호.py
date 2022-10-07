# 올바른 괄호

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    while len(s) != 0:
        if s[0] == ')' or s[-1] == '(' or len(s) % 2 == 1:
            return False
            break
        for i in range(len(s)):
            if i == len(s) - 1:
                break
            elif s[i] == '(' and s[i+1] == ')':
                s = s[:i] + s[i+2:]
                break

        if len(s) == 0 :
            return True
            
            
print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false
print(solution("())(()")) # false

# 테스트 케이스는 통과했지만... 효율성 빵점.. 내일 일어나서 다시 해보자....ㅠㅠㅠ
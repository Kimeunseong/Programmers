# 올바른 괄호

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.

# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

from collections import deque

def solution(s):
    s = deque(s)
    check = []
    if s[0] == ')' or s[-1] == '(' or len(s) % 2 == 1:
        return False
    else:
        while s:
            c = s.popleft()
            if c == '(':
                check.append('(')
            elif c == ')' and check and check[-1] == '(':
                check.pop()
            else:
                return False

    return False if len(check) != 0 else True
    
    
print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false
print(solution("()))((()")) # false
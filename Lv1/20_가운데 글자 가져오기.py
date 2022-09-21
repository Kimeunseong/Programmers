# 가운데 글자 가져오기

# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    return s[len(s)//2-1] + s[len(s)//2] if len(s) % 2 == 0 else s[len(s)//2]

print(solution("abcde")) # c
print(solution("qwer")) # we
print(solution("adfjkejknfsdbkf")) # k
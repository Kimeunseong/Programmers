# 신규 아이디 추천

# 다음은 카카오 아이디의 규칙입니다.
# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
# 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.)
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

from collections import deque

def level1(id1):
    return id1.lower()

def level2(id2):
    symbol = ['-', '_',  '.']
    result = ''
    for i in id2:
        if i.isdigit() or i.isalpha() or i in symbol:
            result += i
    return result

def level3(id3):
    while True:
        if '..' in id3:
            id3 = id3.replace('..', '.')
        else:
            break
    return id3

def level4(id4):
    if len(id4) == 0:
        return id4
    else:
        id_que = deque(id4)
        if id_que[0] == '.':
            id_que.popleft()
        if id_que[-1] == '.':
            id_que.pop()
        return id_que

def level5(id5):
    if len(id5) == 0:
        return 'a'
    else:
        return ''.join(list(id5))

def level6(id6):
    if len(id6) >= 16:
        id6 = id6[:15]
        if id6[-1] == '.':
            list(id6).pop()
    return ''.join(id6)

def solution(new_id):
    answer = level1(new_id)
    answer = level2(answer)
    answer = level3(answer)
    answer = level4(answer)
    answer = level5(answer)
    answer = level6(answer)
    # answer = level7(answer)
    return answer



print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
print(solution("z-+.^.")) # "z--"
# print(solution("=.=")) # aaa"
print(solution("123_.def")) # "123_.def"
print(solution("abcdefghijklmn.p")) # "abcdefghijklmn"
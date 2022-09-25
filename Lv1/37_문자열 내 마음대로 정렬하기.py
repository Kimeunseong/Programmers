# 문자열 내 마음대로 정렬하기

# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    return [i[1] for i in sorted([(i[n], i) for i in strings])]
    
print(solution(["sun", "bed", "car"], 1)) # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2)) # ["abcd", "abce", "cdx"]
print(solution(["aab", "aaa", "aaa"], 1)) # ["aaa", "aaa", "aab"]

# 후기 : 딕셔너리로 풀어보려다가 클래스 객체로 만드는 법도 찾아보고 했지만 결국 문제 푸는건 튜플로 했다ㅋㅋ 그래도 나름 한줄코드라 만족한다ㅎㅎ
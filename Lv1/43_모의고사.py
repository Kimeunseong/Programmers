# 모의고사 - 완전탐색

# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

def solution(answers):
    
    import math

    # std 초기값
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 문제 길이에 맞게 std 설정
    lens = math.ceil(len(answers) / len(std1))
    std1 = std1 * lens
    lens = math.ceil(len(answers) / len(std2))
    std2 = std2 * lens
    lens = math.ceil(len(answers) / len(std3))
    std3 = std3 * lens

    # 학생별 정답을 맞힌 개수 카운트
    cnt1 = cnt2 = cnt3 = 0
    for a, i, j, k in zip(answers, std1, std2, std3):
        if a == i:
            cnt1 += 1
        if a == j:
            cnt2 += 1
        if a == k:
            cnt3 += 1
     
    # 최다 정답자들 추출 후 리턴
    result = []
    total = [cnt1, cnt2, cnt3]
    for i in range(0, 3):
        if total[i] == max(total):
            result.append(i+1)

    return result


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1, 2, 3]
print(solution([1,3,2,4,2,1,3,2,4,2])) # [1, 2, 3]
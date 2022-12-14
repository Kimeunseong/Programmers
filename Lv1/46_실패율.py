# 실패율

# 오렐리를 위해 실패율을 구하는 코드를 완성하라.

# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

def solution(N, stages):
    dict_s ={} 
    stages.sort()

    for i in range(1, N+1):
        if len(stages) == 0: # ZeroDivisionError 방지
            dict_s[i] = 0
        else:
            dict_s[i] = stages.count(i) / len(stages) # i 단계의 실패율 구한 후 dict에 저장
            del stages[:stages.count(i)]              # i단계 실패한 플레이어를 리스트에서 제거
    
    return sorted(dict_s, key = lambda x : dict_s[x], reverse = True) # value 값을 기준으로 내림차순 정렬후, key 값만 리스트 형식으로 반환.
    
    
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]
print(solution(5, [2, 2, 2, 2, 2, 2, 2, 2])) # [2, 1, 3, 4, 5]
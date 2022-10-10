# 프린터

from collections import deque

def solution(priorities, location):
    check = [0 for i in range(len(priorities))] # 요청한 문서의 초기 위치를 나타내는 리스트 생성
    check[location] = 1 # 요청한 문서와 동일한 자리에 1로 표시. 나머지는 0으로 초기화
    print_count = 1     # 요청한 문서가 몇 번째로 출력되는지 확인하는 변수

    # popleft() 사용을 위해 두 리스트를 각각 queue로 설정.
    que_pri = deque(priorities)
    que_check = deque(check)

    while check != 0:
        if que_pri[0] < max(que_pri):      # 대기목록 가장 앞에 있는 문서의 중요도가 최대 중요도보다 작을 경우,
            que_pri.append(que_pri[0])     # 대기목록의 마지막으로 이동.
            que_check.append(que_check[0]) # 위치 리스트도 함께 이동.
            que_pri.popleft()
            que_check.popleft()
        else:                     # 대기목록 가장 앞에 있는 문서의 중요도가 최대 중요도보다 크거나 작을 경우,
            if que_check[0] == 1: # 대기 목록 가장 앞에 있는 문서가 요청한 문서라면, 그대로 break
                break
            que_pri.popleft()     # 아닐 경우, 대기열에서 목록 삭제
            que_check.popleft()
            print_count += 1      # 요청한 문서가 아닌 다른 문서가 인쇄됐으므로, +1

    return print_count

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
# 체육복

# 점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 
# 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
# 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 
# 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
# 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
# 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

from collections import deque

def solution(n, lost, reserve):
    answer = 0
    return answer

print(solution(5, [2,4], [1,3,5])) # 5
print(solution(5, [2,4], [3])) # 4
print(solution(3, [3], [1])) # 2



n = 5
lost = [2, 4]
r = [1,3,5]

have = []
for i in range(1, n+1):
    if i in lost:
        pass
    else:
        have.append(i)
        
print(f'have: {have}')
print(f'lost: {lost}')
print(f'r: {r}')
print('\n')

r2 = r.copy()
for i in r2:
    front = i-1
    if front == 0:
        pass
    else:
        if front in lost:
            have.append(front)
            r.remove(i)
            lost.remove(front)
            
print(f'have: {have}')
print(f'lost: {lost}')
print(f'r: {r}')
print('\n')

r2 = r.copy()
for i in r2:
    back = i+1
    if back == n+1:
        pass
    else:
        if front in lost:
            have.append(back)
            r.remove(i)
            lost.remove(back)
            
print(f'have: {have}')
print(f'lost: {lost}')
print(f'r: {r}')
print('\n')

print(have)
print(len(have))
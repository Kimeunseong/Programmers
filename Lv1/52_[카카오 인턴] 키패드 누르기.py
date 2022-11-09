# [카카오 인턴] 키패드 누르기

# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

def solution(numbers, hand):

    answer = ''
    pad2 = [[1,4,7,10],
            [2,5,8,0],
            [3,6,9,12]]

    targetL_row, targetL_col = 0, 3
    targetR_row, targetR_col = 2, 3

    for i in numbers:
        if i in pad2[0]:
            answer = answer + 'L'
            targetL_row = pad2[0].index(i)
            targetL_col = 0
        elif i in pad2[2]:
            answer = answer + 'R'
            targetR_row = pad2[2].index(i)
            targetR_col = 2
        else:
            cntL, cntR = 0, 0
            targetM_col = pad2[1].index(i)
            targetM_row = 1
            cntL = abs(targetM_row - targetL_row) + abs(targetL_col - targetM_col)
            cntR = abs(targetM_row - targetR_row) + abs(targetR_col - targetM_col)

            if cntL < cntR:
                answer = answer + 'L'
                targetL_row, targetL_col = 1, targetM_col
            elif cntL > cntR:
                answer = answer + 'R'
                targetR_row, targetR_col = 1, targetM_col
            else:
                if hand == 'left':
                    answer = answer + 'L'
                    targetL_row, targetL_col = 1, targetM_col
                elif hand == 'right':
                    answer = answer + 'R'
                    targetR_row, targetR_col = 1, targetM_col
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")) # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"


######################################################

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'

pad2 = [[1,4,7,'*'],
        [2,5,8,0],
        [3,6,9,'#']]

left = pad2[0][3] # '*', 왼손 엄지 초기 위치
right = pad2[2][3] # '#', 오른손 엄지 초기 위치
target_left = 3
target_right = 3

answer = ''

for i in numbers:
    if i in [1, 4, 7]: # 왼손만 사용
        answer = answer + 'L'
        target_left = pad2[0].index(i)
        print(f'target_left = {target_left}, num = {i}')
        left = pad2[0][target_left]
        print(f'left = {left}')
        
    elif i in [3, 6, 9]: # 오른손만 사용
        answer = answer + 'R'
        target_right = pad2[2].index(i)
        print(f'target_right = {target_right}, num = {i}')
        right = pad2[2][target_right]
        print(f'right = {right}')
        
    else:
        cntL, cntR = 0, 0
        target = pad2[1].index(i)
        print(f'target = {target}, num = {i}')
        
        cntL = 1 + abs(target_left - target)
        cntR = 1 + abs(target_right - target)
        print(f'cntL={cntL}, cntR={cntR}')
        
        if cntL < cntR:
            answer = answer + 'L'
        elif cntL > cntR:
            answer = answer + 'R'
        else:
            if hand == 'left':
                answer = answer + 'L'
            elif hand == 'right':
                answer = answer + 'R'
        
print()
print(answer)